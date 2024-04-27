from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, DetalleUsuario

class SignUpUserFormWithEmail(UserCreationForm):
    """ Clase que se encarga de configurar el formuario de registro de usuario """
    email = forms.EmailField(required=True, help_text="Requerido, asegúrese que sea un correo válido")

    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado. Prueba con otro")
        return email

class DetalleUserForm(forms.ModelForm):
    """Clase para el formulario de detalles del perfil"""
    class Meta:
        model = DetalleUsuario
        fields = ('usuario','estado_civil','tipo_documento','genero','etnia','vulnerable')
        widgets = {
            'usuario' : forms.TextInput(attrs={'readonly': False, 'class':'form-control'}), 
            'estado_civil' : forms.Select(attrs={'class':'form-select'}),
            'tipo_documento' : forms.Select(attrs={'class':'form-select'}),
            'genero' : forms.Select(attrs={'class':'form-select'}),
            'etnia' : forms.Select(attrs={'class':'form-select'}),
            'vulnerable' : forms.Select(attrs={'class':'form-select'})
        }