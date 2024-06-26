# Importamos un serializador único como identificador:
import uuid
from django.db import models
# Importamos la libreria de texto enriquecido:
from ckeditor.fields import RichTextField
# Para este módulo es necesario importar  el modelo User de Django, y el módulo de programa,
from registration.models import Usuario
# Mas adelante importamos el de despacho
from despachos.models import Despacho
from dane.models import Departamento, Ciudad

# Función para subir archivos:
def subir_archivo(instance, nombre_archivo):
    return "documentos/procesos/{sol}/{id}/{filename}".format( sol = instance.solicitud, id = instance.radicado, filename = nombre_archivo)

def subir_pruebas(instance, nombre_archivo):
    return "documentos/procesos/{id}/pruebas/{filename}".format( id = instance.solicitud, filename = nombre_archivo)


def subir_acto(instance, nombre_archivo):
    return "documentos/procesos/{sol}/{id}/actuaciones/{filename}".format( sol = instance.expediente.solicitud, id = instance.expediente, filename = nombre_archivo)

# Create your models here.
class Solicitud(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # 05e9a559-6d59-4656-96c3-3c1db236eea8
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Usuario demandante o acusado')
    fecha_solicitud = models.DateField(verbose_name="Fecha de solicitud")
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, verbose_name='Departamento de los hechos', null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, verbose_name='Ciudad de los hechos', null=True)
    descripcion_hechos = RichTextField(verbose_name='Descripción de los Hechos')
    tipo_orientacion = RichTextField(verbose_name='Orientación Brindada')
    decision_adoptada = models.BooleanField(default = True, verbose_name='Decisión Adoptada')
    observacion_adicional = RichTextField(verbose_name='Observaciones')
    estado_solicitud = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'

    def __str__(self) -> str:
        return f'{self.id}'
    

class DetalleSolicitud(models.Model):
    """
        Clase que representa a una solicitud individual con su respectivo abogado,
        y se relaciona con la clase Solicitud para poder agregarle detalles a estas.
    """
    abogado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    solicitud = models.OneToOneField(Solicitud, on_delete=models.CASCADE, related_name='detalle')
    observacion = RichTextField()
    estado = models.BooleanField('Estado de Solicitud', default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Detalle de Solicitudes'

    def __str__(self) -> str:
        return f'{self.abogado}'
    

class Pruebas(models.Model):
    """ Modelo para cargar los documentos que se usan como soporte para probar inocencia o culpabilidad """
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    nombre_prueba = models.CharField('Nombre de prueba', max_length=100)
    descripcion = RichTextField(null=True, blank=True)
    archivo = models.FileField(upload_to=subir_pruebas, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Pruebas'

    def __str__(self):
        return f"{self.nombre_prueba}"


class Expediente(models.Model):
    """ Clase para guardar los documentos """
    radicado = models.PositiveBigIntegerField("Número de radicado")
    fecha_radicado = models.DateField(verbose_name="Fecha de radicado")
    hora_radicado = models.TimeField(verbose_name="Hora de radicado")
    solicitud = models.ForeignKey(Solicitud, on_delete=models.CASCADE)
    despacho = models.OneToOneField(Despacho, on_delete=models.CASCADE)
    archivo = models.FileField(upload_to=subir_archivo, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Expedientes'

    def __str__(self):
        return f'{self.radicado}'


class Actuaciones(models.Model):
    """ Modelo para registrar las actuaciones realizadas por el personal del Despacho """
    expediente = models.ForeignKey(Expediente, on_delete=models.PROTECT)  # PROTECT impide borrar un expediente mientras tenga una actuacion
    nota_seguimiento = RichTextField(verbose_name="Observación")
    archivo = models.FileField(upload_to=subir_acto, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Actuaciones'
    
    def __str__(self):
        return f"{self.expediente} {self.created}"