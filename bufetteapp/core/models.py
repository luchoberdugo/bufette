from django.db import models
# Importamos la libreria de texto enriquecido:
from ckeditor.fields import RichTextField

# Create your models here.
class Contacto(models.Model):
    nombre = models.CharField('Nombre', max_length=200)
    correo = models.EmailField('Correo Electrónico', blank=False, null=False)
    mensaje = models.TextField('Mensaje', null=False, blank=False)
    creado_el = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    modificado = models.DateField(auto_now=True, verbose_name="Ultima Modificación")

    class Meta:
        ordering = ['-creado_el']  # Ordenar por fecha de creacion
        verbose_name = 'Contacto'
    
class Nosotros(models.Model):
    mision = RichTextField('Misión', null=False, blank=False, unique=True)
    vision = RichTextField('Visión', null=False, blank=False, unique=True)
    creado_el = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    modificado = models.DateField(auto_now=True, verbose_name="Ultima Modificación")

    class Meta:
        verbose_name = 'Nosotros'
        verbose_name_plural = 'Nosotros'


class Servicios(models.Model):
    nombre_servicio = models.CharField("Nombre del servicio", max_length=150)
    descripcion_corta = RichTextField("Descripción del servicio", max_length=250)
    creado_el = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    modificado = models.DateField(auto_now=True, verbose_name="Ultima Modificación")

    class Meta:
        ordering = ['-creado_el']  # Ordenar por fecha de creacion
        verbose_name = 'Servicio'