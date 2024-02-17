from django.contrib import admin
from .models import Contacto, Nosotros, Servicios

# Register your models here.
admin.site.register(Contacto)
admin.site.register(Nosotros)
admin.site.register(Servicios)