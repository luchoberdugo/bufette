# Importamos un serializador único como identificador:
import uuid
from django.db import models
# Importamos la libreria de texto enriquecido:
from ckeditor.fields import RichTextField
# Para este módulo es necesario importar  el modelo User de Django, y el módulo de programa,
from registration.models import Usuario
# Mas adelante importamos el de despacho
from despachos.models import Despacho

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

# Tabla de Expediente:
class Expediente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # 05e9a559-6d59-4656-96c3-3c1db236eea8
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario demandante o acusado')
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, verbose_name='Solicitud')
    despacho = models.ForeignKey(Despacho, on_delete=models.CASCADE, verbose_name='Despacho')
    radicado = RichTextField(verbose_name='Radicado')
    fecha_radicado = models.DateField(verbose_name="Fecha de radicado")
    
    class Meta:
        verbose_name = 'Expediente'
        verbose_name_plural = 'Expedientes'

    def __str__(self) -> str:
        return f'{self.id} - {self.usuario}'

# Tabla de Actuaciones:
class Actuaciones(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # 05e9a559-6d59-4656-96c3-3c1db236eea8
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE, verbose_name='Expediente')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario demandante o acusado')
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE, verbose_name='Solicitud')
    nota_seguimiento = RichTextField(verbose_name='Notas de Seguimiento')
        
    class Meta:
        verbose_name = 'Actuación'
        verbose_name_plural = 'Actuaciones'

    def __str__(self) -> str:
        return f'{self.id} - {self.usuario}'
    
# Tabla de Pruebas:
class Pruebas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # 05e9a559-6d59-4656-96c3-3c1db236eea8
    expediente = models.ForeignKey(Expediente, on_delete=models.CASCADE, verbose_name='Expediente')
    nombre_pruebas = RichTextField(verbose_name='Nombre de Prueba')
    descripcion = RichTextField(verbose_name='Descripción')
    soporte = RichTextField(verbose_name='Soporte')

        
    class Meta:
        verbose_name = 'Prueba'
        verbose_name_plural = 'Pruebas'

    def __str__(self) -> str:
        return f'{self.id} - {self.usuario}'
