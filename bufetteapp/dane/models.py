from django.db import models

# Create your models here.
from django.db import models


class Departamento(models.Model):
    name = models.CharField(max_length=255)


class Ciudad(models.Model):
    name = models.CharField(max_length=255)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
        