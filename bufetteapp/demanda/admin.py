from django.contrib import admin
from .models import Solicitud, DetalleSolicitud, Expediente, Pruebas, Actuaciones

# Register your models here.
admin.site.register(Solicitud)
admin.site.register(DetalleSolicitud)
admin.site.register(Expediente)
admin.site.register(Pruebas)
admin.site.register(Actuaciones)