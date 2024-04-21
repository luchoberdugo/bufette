from django.db import models

# Create your models here.
from django.db import models


class Departamento(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Departamentos'

    def __str__(self) -> str:
        return f'{self.name}'


class Ciudad(models.Model):
    name = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Ciudades'

    def __str__(self):
        return f'{self.name}'
