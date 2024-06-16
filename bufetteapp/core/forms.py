from django import forms
from .models import Contacto

# creamos la clase de formulario:
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = 'nombre', 'correo', 'mensaje'
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.EmailInput(attrs={'class':'form-control'}),
            'mensaje': forms.Textarea(attrs={'class':'form-control', 'rows':'4'})
        }
    
    def clean(self):
        """ método para normalizar el formato del texto """
        cleaned_data = super().clean()
        # Capturamos los valores de los input
        correo = cleaned_data.get('correo')
        nombre = cleaned_data.get('nombre')
        # Normalizamos de acuerdo al formato de texto:
        cleaned_data['correo'] = correo.lower()
        cleaned_data['nombre'] = nombre.title()

        return cleaned_data
