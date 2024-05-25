from django import forms
from registration.models import Usuario
from .models import Solicitud, DetalleSolicitud, Expediente, Pruebas, Actuaciones

class SolicitudForm(forms.ModelForm):
    """ Clase para el formulario de la solicitud """
    class Meta:
        model = Solicitud
        fields = 'usuario', 'fecha_solicitud', 'descripcion_hechos', 'tipo_orientacion', 'decision_adoptada', 'observacion_adicional'         
        widgets = {
            'fecha_solicitud' : forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            'descripcion_hechos' : forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'tipo_orientacion' : forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'decision_adoptada' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observacion_adicional' : forms.Textarea(attrs={'class':'form-control', 'rows':'3'})
        }

class DetalleSolicitudForm(forms.ModelForm):
    """ Clase para el formulario del detalle de la solicitud """
    abogado = forms.ModelChoiceField(queryset=Usuario.objects.filter(groups='Abogados'))
    class Meta:
        model = DetalleSolicitud
        fields = 'abogado', 'solicitud', 'observación', 'estado'
        widgets = {
            'abogado': forms.Select(attrs={'class':'form-select'}),
            'observacion': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class ExpedienteForm(forms.ModelForm):
    """ Clase para el formulario del expediente """
    class Meta:
        model = Expediente
        fields = 'radicado', 'fecha_radicado', 'hora_radicado', 'solicitud', 'despacho', 'archivo' 
        widgets = {
            'radicado': forms.TextInput(attrs={'class': ''}),
            'fecha_radicado': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_radicado': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'despacho': forms.Select(attrs={'class': 'form-select'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
        }

class PruebasForm(forms.ModelForm):
    """ Clase para el formulario de Pruebas """
    class Meta:
        model = Pruebas
        fields = 'expediente','nombre_prueba','descripcion','archivo'
        widgets = {
            'nombre_prueba': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
        }

class ActuacionesForm(forms.ModelForm):
    """ Clase para el formulario de Actuaciones """
    class Meta:
        model = Actuaciones
        fields = ('expediente','nota_seguimiento')
        widgets = {
            'nota_seguimiento': forms.Textarea(attrs={'class':'form-control', 'rows':'3'})
        }