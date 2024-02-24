from django import forms

# creamos la clase de formulario:
class ContactoForm(forms.Form):
    nombre = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    correo = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    mensaje= forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'4'}))