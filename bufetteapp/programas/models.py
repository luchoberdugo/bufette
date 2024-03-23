from django.db import models

# Create your models here.

class TipoPrograma(models.Model):
    nombre_tipo_programa =  models.CharField("Tipo de Programa", max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Tipo de Programa"
        verbose_name_plural="Tipo de Programa"
    
    def __str__(self):
        return self.nombre_tipo_programa
    
class Programa(models.Model):
    tipo_programa = models.ForeignKey(TipoPrograma, on_delete=models.CASCADE, verbose_name='Tipo de Programa')
    nombre_programa = models.CharField('Nombre del Programa',max_length=200, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Programas"
        verbose_name_plural="Programas"

    def  __str__(self):
       return f'{self.nombre_programa}'    

class DetallePrograma(models.Model):
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE, verbose_name='Programa')
    acto_juridico =  models.CharField('Acto Jurídico' ,max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Detalle de Programa"
        verbose_name_plural="Detalles de Programa"

    def  __str__(self):
        return f'{self.acto_juridico}'
    

