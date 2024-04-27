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
        return reverse_lazy('detalle_usuario') + '?registrado'
    
    # Arrastramos el formulario:
    def get_form(self, form_class= None):
        form = super(SignUpUserView, self).get_form()
        # Agregando Estilos:
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'Nickname', 'class': 'form-control'})
        form.fields['first_name'].widget = forms.TextInput(attrs={'placeholder':'Nombres', 'class': 'form-control'})
        form.fields['last_name'].widget = forms.TextInput(attrs={'placeholder':'Apellidos', 'class': 'form-control'})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'Correo Electrónico', 'class': 'form-control'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'placeholder':'Contraseña', 'class': 'form-control'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'placeholder':'Confirme Contraseña', 'class': 'form-control'})

        return form
    
class AddDetailUserView(CreateView):
    """ Clase para agregar datos en el detalle del usuario """
    template_name = 'registration/detalleuser.html'
    form_class = DetalleUserForm

    def get_success_url(self) -> str:
        return reverse_lazy('dashboard') + '?completado'
    
@method_decorator(login_required, name='dispatch')
class UserListView(ListView):
    """ Clase para ver el listado de usuarios """
    model = Usuario
    template_name = 'registration/userlist.html'
    paginate_by = 19

