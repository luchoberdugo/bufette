# Importamos un serializador único como identificador:
import uuid
from django.db import models
# Importamos la libreria de texto enriquecido:
from ckeditor.fields import RichTextField
# Para este módulo es necesario importar  el modelo User de Django, y el módulo de programa,
from registration.models import Usuario
# Mas adelante importamos el de despacho

# Create your models here.
class Solicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # 05e9a559-6d59-4656-96c3-3c1db236eea8
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario demandante o acusado')
    fecha_solicitud = models.DateField(verbose_name="Fecha de solicitud")
    descripcion_hechos = RichTextField(verbose_name='Descripción de los Hechos')
    tipo_orientacion = RichTextField(verbose_name='Orientación Brindada')
    decision_adoptada = models.BooleanField(default = True, verbose_name='Decisión Adoptada')
    observacion_adicional = RichTextField(verbose_name='Observaciones')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

    def __str__(self) -> str:
        return f'{self.id} - {self.usuario}'