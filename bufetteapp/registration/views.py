from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
# Importamos el formulario:
from .forms import SignUpUserFormWithEmail, DetalleUserForm
from django import forms
# importamos el modelo de datos:
from .models import Usuario

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Importamos paquete de resolución de urls:
from django.urls import reverse_lazy

# Create your views here.
@method_decorator(login_required, name='dispatch')
class DashboardUserView(TemplateView):
    template_name = 'registration/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class SignUpUserView(CreateView):
    form_class = SignUpUserFormWithEmail
    template_name = 'registration/registro.html'

    def get_success_url(self) -> str:
        email = self.object.email 
        # Agrega el correo electrónico a la URL de redirección
        return reverse_lazy('detalle_usuario') + f'?email={email}'      # Se cambia el parámetro de url para poder buscar el id mas adelante en la pantala siguiente
    
    # Arrastramos el formulario:
    def get_form(self, form_class= None):
        form = super(SignUpUserView, self).get_form()
        # Agregando Estilos:
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nickname', 'class': 'form-control text-lowercase'})
        form.fields['numero_identificacion'].widget = forms.TextInput(attrs={'placeholder':'Número de Identificación', 'class': 'form-control'})
        form.fields['nacionalidad'].widget = forms.TextInput(attrs={'placeholder':'Nacionalidad', 'class': 'form-control text-capitalize'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'placeholder':'Nombres', 'class': 'form-control text-capitalize'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'placeholder':'Apellidos', 'class': 'form-control text-capitalize'})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'Correo Electrónico', 'class': 'form-control text-lowercase'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña', 'class': 'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Confirme Contraseña', 'class': 'form-control'})

        return form
    
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
            user_id = usuario.id                            # Capturamos el id de la consulta anterior   
        except Usuario.DoesNotExist:
            user_id = None
        
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
        



