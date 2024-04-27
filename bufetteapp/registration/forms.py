from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, DetalleUsuario
# Importaciones para traer un grupo desde el formulario:
from django.contrib.auth.models import Group

class SignUpUserFormWithEmail(UserCreationForm):
    """ Clase que se encarga de configurar el formuario de registro de usuario """
    email = forms.EmailField(required=True, help_text="Requerido, asegúrese que sea un correo válido")
    # Consulta para filtrar los grupos creados:
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label="Selecciona un grupo")

    class Meta:
        model = Usuario
        fields = ('username', 'groups', 'first_name', 'last_name', 'email', 'nacionalidad', 'numero_identificacion', 'password1', 'password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado. Prueba con otro")
        return email

class DetalleUserForm(forms.ModelForm):
    """Clase para el formulario de detalles del perfil"""
    class Meta:
        model = DetalleUsuario
        fields = ('fecha_nacimiento','fecha_expedicion','estado_civil','tipo_documento','genero','etnia','vulnerable')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}), 
            'fecha_expedicion': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}), 
            'estado_civil' : forms.Select(attrs={'class':'form-select'}),
            'tipo_documento' : forms.Select(attrs={'class':'form-select'}),
            'genero' : forms.Select(attrs={'class':'form-select'}),
            'etnia' : forms.Select(attrs={'class':'form-select'}),
            'vulnerable' : forms.Select(attrs={'class':'form-select'})
        }