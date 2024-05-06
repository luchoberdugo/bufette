from django import forms
from django.http import JsonResponse
from .models import Usuario, DetalleUsuario
# Importaciones para traer un grupo desde el formulario:
from django.contrib.auth.models import Group

class SignUpUserFormWithEmail(forms.ModelForm):
    """ Clase que se encarga de configurar el formuario de registro de usuario """
    email = forms.EmailField(required=True, help_text="Requerido, asegúrese que sea un correo válido")
    # Consulta para filtrar los grupos creados:
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label="Perfiles:")

    class Meta:
        model = Usuario
        fields = 'username', 'first_name', 'last_name', 'email', 'nacionalidad', 'numero_identificacion', 'password',  'groups', 'is_active', 'is_staff', 'is_superuser'
        widgets = {
            'groups':  forms.Select(attrs={'class':'form-select'}),  
            'username':  forms.TextInput(attrs={'class':'form-control'}),  
            'numero_identificacion':  forms.NumberInput(attrs={'class':'form-control'}),  
            'nacionalidad':  forms.TextInput(attrs={'class':'form-control'}),  
            'first_name':  forms.TextInput(attrs={'class':'form-control'}),  
            'last_name':  forms.TextInput(attrs={'class':'form-control'}),  
            'email':  forms.EmailInput(attrs={'class':'form-control'}),  
            'password':  forms.PasswordInput(attrs={'class':'form-control'})  
        }
        labels = {
            'is_active': '¿Es usuario activo?',
            'is_staff': '¿Es usuario staff?',
            'is_superuser': '¿Es usuario administrador?',
            'groups': 'Perfil de Usuario'
        }
        exclude = ['last_login', 'date_joined',]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo ya está registrado. Prueba con otro")
        return email
    
    def save(self, commit= True):
        """ Método save para guardar toda la info del formulario, incluso agrega el usuario a un grupo determinado """
        data = {}
        form = super()
        try:
            if form.is_valid():
                # Guardar el password:
                pass_user = self.cleaned_data['password'] 
                user_form = form.save(commit=False)
                
                if user_form.pk is None:
                    user_form.set_password(pass_user)
                else:
                    user = Usuario.objects.get(pk=user_form.pk)
                    if user.password != pass_user:
                        user_form.set_password(pass_user)
                    
                user_form.save()
                user_form.groups.clear()
                grupo = self.cleaned_data['groups']
                # for grupo in self.cleaned_data['groups']:
                user_form.groups.add(grupo)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class UserUtilForm(forms.ModelForm):
    # Consulta para filtrar los grupos creados:
    groups = forms.ModelChoiceField(queryset=Group.objects.all(), empty_label="Perfiles:")
    class Meta:
        model = Usuario
        fields = 'username', 'first_name', 'last_name', 'nacionalidad', 'numero_identificacion', 'groups', 'is_active'
        widgets = {
            'groups':  forms.Select(attrs={'class':'form-select'}),  
            'username':  forms.TextInput(attrs={'class':'form-control'}),  
            'numero_identificacion':  forms.NumberInput(attrs={'class':'form-control'}),  
            'nacionalidad':  forms.TextInput(attrs={'class':'form-control'}),  
            'first_name':  forms.TextInput(attrs={'class':'form-control'}),  
            'last_name':  forms.TextInput(attrs={'class':'form-control'}),  
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'})  
        }
        labels = {
            'is_active': '¿Es usuario activo?',
            'groups': 'Perfil de Usuario'
        }
        exclude = ['email','last_login', 'date_joined','is_staff', 'is_superuser']

    def save(self, commit= True):
        """ Método save para guardar toda la info del formulario, incluso agrega el usuario a un grupo determinado """
        data = {}
        form = super()
        try:
            user_form = form.save(commit=False)
            if form.is_valid():
                user_form.save()
                user_form.groups.clear()
                grupo = self.cleaned_data['groups']
                # for grupo in self.cleaned_data['groups']:
                user_form.groups.add(grupo)
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class DetalleUserForm(forms.ModelForm):
    """Clase para el formulario de detalles del perfil"""
    class Meta:
        model = DetalleUsuario
        fields = ('usuario','fecha_nacimiento','fecha_expedicion','estado_civil','tipo_documento','genero','etnia','vulnerable')
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}), 
            'fecha_expedicion': forms.DateInput(attrs={'type':'date', 'class': 'form-control'}), 
            'estado_civil' : forms.Select(attrs={'class':'form-select'}),
            'tipo_documento' : forms.Select(attrs={'class':'form-select'}),
            'genero' : forms.Select(attrs={'class':'form-select'}),
            'etnia' : forms.Select(attrs={'class':'form-select'}),
            'vulnerable' : forms.Select(attrs={'class':'form-select'})
        }