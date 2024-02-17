from django.contrib import admin
from .models import Contacto, Nosotros, Servicios

# Class de administrador:
class ContactoAdmin(admin.ModelAdmin):
    """
        Clase para la modificación de la vista del panel de administración de django para el contacto 
    """
    search_fields = ['nombre']                                          # Campos por búsqueda
    list_display = ['id','nombre','correo','creado_el','modificado']    # Campos a mostrar en el panel 
    list_filter = ['nombre','creado_el','modificado']                   # Filtros
    list_per_page = 10                                                  # Paginación

class NosotrosAdmin(admin.ModelAdmin):
    """
        Clase para la modificación de la vista del panel de administración de django para nosotros
    """
    search_fields = ['mision', 'vision']                                # Campos de búsqueda
    
class ServiciosAdmin(admin.ModelAdmin):
    """ 
        Clase para la modificación de la vista del panel de administración de django para servicios
    """
    search_fields = ['nombre_servicio','descripcion_corta','creado_el','modificado']        # Campos por búsqueda
    list_display = ['id','nombre_servicio','descripcion_corta','creado_el','modificado']    # Campos a mostrar en el panel 
    list_filter = ['nombre_servicio','creado_el','modificado']                              # Filtros
    list_per_page = 10                                                                      # Paginación

# Register your models here.
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Nosotros, NosotrosAdmin)
admin.site.register(Servicios, ServiciosAdmin)


'nombre_servicio','descripcion_corta','creado_el','modificado'