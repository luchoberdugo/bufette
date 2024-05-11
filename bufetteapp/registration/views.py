from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, View
# Importamos el formulario:
from .forms import SignUpUserFormWithEmail, DetalleUserForm, UserUtilForm
# importamos el modelo de datos:
from .models import Usuario
from django.db.models import Q

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model

# Importamos paquete de resolución de urls:
from django.urls import reverse_lazy

# ---------------------------------  CRUD DE USUARIO COMPLETO ---------------------------------

# Create your views here.
@method_decorator(login_required, name='dispatch')
class DashboardUserView(TemplateView):
    template_name = 'registration/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class SignUpUserView(LoginRequiredMixin, CreateView):
    form_class = SignUpUserFormWithEmail
    template_name = 'registration/registro.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        # Agrega el correo electrónico a la URL de redirección
        email = self.request.POST["email"]
        print(email)
        return reverse_lazy('detalle_usuario') + f'?email={email}'      # Se cambia el parámetro de url para poder buscar el id mas adelante en la pantala siguiente

    
class AddDetailUserView(CreateView):
    """ Clase para agregar datos en el detalle del usuario """
    template_name = 'registration/detalleuser.html'
    form_class = DetalleUserForm
    
    def get(self, request, *args, **kwargs):
        """ Con este método get vamos a capturar el id del usuario, 
            tambien podemos tener todo el usuario para pintarlo en la pantalla """
        # Capturamos el email del usuario guardado:
        email = request.GET.get('email')
        # Consultamos en la bd y capturamos el id:
        try:
            usuario = Usuario.objects.get(email=email)      # Buscamos el usuario que tenga el email que pasamos en la url
        except Usuario.DoesNotExist:
            usuario = None
        
        return render(request, self.template_name, {'usuario': usuario, 'form': self.form_class})

    def get_success_url(self) -> str:
        """ Redirige al dashboard una vez que se completa el formulario """
        return reverse_lazy('dashboard') + '?completado'
    
@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    """ Clase para ver el listado de usuarios """
    model = Usuario
    template_name = 'registration/userlist.html'
    paginate_by = 10

    # Método para filtrar:
    def get_queryset(self):
        qs = super().get_queryset()         # De entrada capturamos todos los datos
        filtro = self.request.GET.get('query')

        if filtro :
            qs = qs.filter(
                Q(first_name__icontains=filtro) | Q(last_name__icontains=filtro)
            )
        return qs.order_by('groups__name','-is_active')

class UserEditView(UpdateView):
    template_name = 'registration/useredit.html'
    form_class = UserUtilForm

    def get_object(self):
        user_obj, created = Usuario.objects.get_or_create(id=self.kwargs['pk'])
        return user_obj 

    def get_success_url(self) -> str:
        """ Redirige al dashboard una vez que se completa el formulario """
        return reverse_lazy('dashboard') + '?completado'
    

class UserActivateOrDeactivateView(View):
    
    def get(self, request, pk):
        user = get_user_model().objects.get(id=pk)

        if user.is_active:
            user.is_active = False
        else:
            user.is_active = True
        
        user.save()

        return redirect('listausuario')
        
# ---------------------------------  CRUD DE USUARIO COMPLETO ---------------------------------





