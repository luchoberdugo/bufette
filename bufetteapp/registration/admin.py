from django.contrib import admin
from .models import TipoDocumento, Genero, Etnias, Vulnerabilidades, Usuario, TipoTelefono, TelefonoUser, DetalleUsuario, TarjetaProfesional, EstadoCivil

# Clases para visualizar comodamente en el admin:
class TipoDocumentoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_documento']
    list_display = ['nombre_documento', 'created', 'modified']
    list_per_page = 10

class GeneroAdmin(admin.ModelAdmin):
    search_fields = ['nombre_genero']
    list_display = ['nombre_genero', 'created', 'modified']
    list_per_page = 10

class EtniasAdmin(admin.ModelAdmin):
    search_fields = ['nombre_etnia']
    list_display = ['nombre_etnia', 'created', 'modified']
    list_per_page = 10

class VulnerabilidadesAdmin(admin.ModelAdmin):
    search_fields = ['nombre_vulnerabilidad']
    list_display = ['nombre_vulnerabilidad', 'created', 'modified']
    list_per_page = 10

class UsuarioAdmin(admin.ModelAdmin):
    search_fields = ['email', 'first_name', 'last_name', 'numero_identificacion',]
    list_display = ['email', 'first_name', 'last_name', 'numero_identificacion', 'created', 'modified']
    list_per_page = 10

class TipoTelefonoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_tipo']
    list_display = ['nombre_tipo', 'created', 'modified']
    list_per_page = 10

class TelefonoAdmin(admin.ModelAdmin):
    search_fields = ['numero_tel']
    list_display = ['numero_tel', 'created', 'modified']
    list_per_page = 10

# Register your models here.
admin.site.register(TelefonoUser, TelefonoAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(TipoTelefono, TipoTelefonoAdmin)
admin.site.register(TipoDocumento, TipoDocumentoAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Etnias, EtniasAdmin)
admin.site.register(Vulnerabilidades, VulnerabilidadesAdmin)
admin.site.register(DetalleUsuario)
admin.site.register(TarjetaProfesional)
admin.site.register(EstadoCivil)
