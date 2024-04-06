from django.contrib import admin
from .models import TipoPrograma, Programa, DetallePrograma

# Register your models here.
admin.site.register(TipoPrograma)
admin.site.register(Programa)
admin.site.register(DetallePrograma)