from django.db import models

# Create your models here.
class TipoDespacho(models.Model):
    nombre_tipo_despacho = models.CharField('Tipo de Despacho', max_length=50, unique=True)
    creado_el = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    modificado = models.DateField(auto_now=True, verbose_name="Ultima Modificación")

    class Meta:
        verbose_name = 'Tipo de Despacho'
        ordering = ('nombre_tipo_despacho',)

    def __str__(self) -> str:
        return f'{self.nombreTipoDespacho}'
    
class Despacho(models.Model):
    tipo_despacho = models.ForeignKey(TipoDespacho, on_delete=models.CASCADE)
    nombre_despacho = models.CharField('Despacho', max_length=250)
    creado_el = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    modificado = models.DateField(auto_now=True, verbose_name="Ultima Modificación")

    class Meta:
        verbose_name = 'Despacho'
        ordering = ('-creado_el',)

    def __str__(self) -> str:
        return f'{self.nombre_despacho}'