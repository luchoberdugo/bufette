from django import forms
from django.contrib.auth.models import Group
from registration.models import Usuario
from .models import Solicitud, DetalleSolicitud, Expediente, Pruebas, Actuaciones

class SolicitudForm(forms.ModelForm):
    """ Clase para el formulario de la solicitud """
    class Meta:
        model = Solicitud
        fields = 'usuario', 'fecha_solicitud', 'departamento', 'ciudad', 'descripcion_hechos', 'tipo_orientacion', 'decision_adoptada', 'observacion_adicional', 'estado_solicitud'     
        widgets = {
            'fecha_solicitud' : forms.DateInput(attrs={'type':'date', 'class': 'form-control'}),
            'departamento' : forms.Select(attrs={'class':'form-select', 'onchange':'filterMunicipalities()'}),
            'ciudad' : forms.Select(attrs={'class':'form-select'}),
            'descripcion_hechos' : forms.Textarea(attrs={'class':'form-control col-md-12', 'rows':'3'}),
            'tipo_orientacion' : forms.Textarea(attrs={'class':'form-control col-md-12', 'rows':'3'}),
            'decision_adoptada' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'observacion_adicional' : forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'estado_solicitud' : forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class DetalleSolicitudForm(forms.ModelForm):
    """ Clase para el formulario del detalle de la solicitud """
    class Meta:
        model = DetalleSolicitud
        fields = 'abogado', 'solicitud', 'observacion', 'estado'
        widgets = {
            'abogado': forms.Select(attrs={'class':'form-select'}),
            'observacion': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'estado': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    def __init__(self, *args, **kwargs):
        """ Método constructor para el filtro de abogados  """
        super().__init__(*args, **kwargs)
        abogado_filtro = Group.objects.get(name='Abogados')
        self.fields['abogado'].queryset = Usuario.objects.filter(groups = abogado_filtro, is_active=True)


class ExpedienteForm(forms.ModelForm):
    """ Clase para el formulario del expediente """
    class Meta:
        model = Expediente
        fields = 'radicado', 'fecha_radicado', 'hora_radicado', 'solicitud', 'despacho', 'archivo' 
        widgets = {
            'radicado': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_radicado': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_radicado': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'despacho': forms.Select(attrs={'class': 'form-select'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
        }

class PruebasForm(forms.ModelForm):
    """ Clase para el formulario de Pruebas """
    class Meta:
        model = Pruebas
        fields = 'solicitud','nombre_prueba','descripcion','archivo'
        widgets = {
            'nombre_prueba': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
        }

class ActuacionesForm(forms.ModelForm):
    """ Clase para el formulario de Actuaciones """
    class Meta:
        model = Actuaciones
        fields = ('expediente','nota_seguimiento', 'archivo')
        widgets = {
            'nota_seguimiento': forms.Textarea(attrs={'class':'form-control', 'rows':'3'}),
            'archivo': forms.FileInput(attrs={'class': 'form-control', 'type': 'file'})
        }