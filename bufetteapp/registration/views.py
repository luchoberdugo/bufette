from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
# Importamos el formulario:
from .forms import SignUpUserFormWithEmail, DetalleUserForm
# importamos el modelo de datos:
from .models import Usuario

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin

# Importamos paquete de resolución de urls:
from django.urls import reverse_lazy

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
        return reverse_lazy('dashboard') + '?completado'
    
@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    """ Clase para ver el listado de usuarios """
    model = Usuario
    template_name = 'registration/userlist.html'
    paginate_by = 5

    # Método para filtrar:
    def get_queryset(self):
        qs = super().get_queryset()         # De entrada capturamos todos los datos
        filtro = self.request.GET.get('query')

        if filtro :
            qs = qs.filter(first_name__icontains=filtro)
        return qs
        



