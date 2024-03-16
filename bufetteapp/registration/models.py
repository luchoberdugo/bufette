from django.db import models
from django.contrib.auth.models import AbstractUser
# Decoradores de usuario:
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class TipoDocumento(models.Model):
    """ Modelo para el tipo de documento que se utiliza en la tabla de personas"""
    nombre_documento = models.CharField("Nombre del Documento", max_length=20)  # Campo para almacenar el nombre del tipo de documento 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Tipo Documento"
        verbose_name_plural = "Tipos de Documento"

    def  __str__(self):
        return f'{self.nombre_documento}'

class EstadoCivil(models.Model):
    """ Modelo para el tipo de documento que se utiliza en la tabla de personas"""
    estado_civil = models.CharField("Estado Civil", max_length=20)  # Campo para almacenar el nombre del tipo de documento 
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Estados Civiles"
        verbose_name_plural = "Estados Civiles"

    def  __str__(self):
        return f'{self.estado_civil}'

class Genero(models.Model):
    """ Modelo para genero, de una persona"""
    nombre_genero = models.CharField("Nombre del género", max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Género'
        verbose_name_plural = 'Géneros'

    def __str__(self):
        return f'{self.nombre_genero}'

class Etnias(models.Model):
    """ Modelo para las etnias a las que pertenece una persona."""
    nombre_etnia = models.CharField('Nombre de la Etnia',max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:     
        verbose_name='Etnia'
        verbose_name_plural='Etnias'
        
    def __str__(self):
        return f'{self.nombre_etnia}'

class Vulnerabilidades(models.Model):
    nombre_vulnerabilidad = models.CharField("Grupo Vulnerabilidad", max_length = 50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Vulnerabilidades'
        verbose_name_plural = 'Vulnerabilidades'

    def __str__(self):
        return f'{self.nombre_vulnerabilidad}'

class Usuario(AbstractUser):
    """ Clase para registrar a los usuarios del sistema"""
    email = models.EmailField("Correo Electrónico", unique = True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    nacionalidad = models.CharField("Nacionalidad", max_length = 50)
    numero_identificacion = models.CharField("Número de Identificación", max_length = 25)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class DetalleUsuario(models.Model):
    """ """
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    estado_civil = models.ForeignKey(EstadoCivil, on_delete=models.CASCADE, verbose_name="Estado Civil")
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, verbose_name = "Tipo de Documento")
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, verbose_name="Género", blank=True)
    etnia = models.ForeignKey(Etnias, on_delete=models.CASCADE, verbose_name="Pertenencia Étnica", blank=True)
    vulnerable = models.ForeignKey(Vulnerabilidades, on_delete=models.CASCADE, verbose_name="Vulnerabilidad", blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Detalle de Usuarios'
        verbose_name_plural = 'Detalle de Usuarios'

    def __str__(self):
        return f'{self.usuario}'

class TipoTelefono(models.Model):
    """ Modelo para los tipos de teléfonos que puede tener una persona."""
    nombre_tipo = models.CharField("Nombre del Tipo", max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Tipo Teléfono"
        verbose_name_plural = "Tipos de Teléfonos"
        
    def __str__(self):
        return f'{self.nombre_tipo}'
        
class TelefonoUser(models.Model):
    """ Modelo para relacionar a un usuario con sus telefonos."""
    numero_tel = models.CharField("Numero Teléfonico", max_length = 25)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    tipo_telefono = models.ForeignKey(TipoTelefono, on_delete=models.CASCADE, verbose_name="Tipo de Teléfono")
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Teléfonos'
        verbose_name_plural = 'Teléfonos'

    def __str__(self):
        return f'{self.numero_tel}'

#################################### Funcionalidad para el ingreso y registro de Usuarios: ####################################
@receiver(post_save, sender=Usuario)
def perfilUsuarioSeguro(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Usuario.objects.get_or_create(id = instance.id) #