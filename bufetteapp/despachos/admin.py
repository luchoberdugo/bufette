from django.contrib import admin
from  .models import TipoDespacho, Despacho

class  TipoDespachoAdmin(admin.ModelAdmin):
    search_fields = ['nombre_tipo_despacho']                                            # Campos por búsqueda
    list_display = ['id','nombre_tipo_despacho','creado_el','modificado']               # Campos a mostrar en el panel 
    list_filter = ['nombre_tipo_despacho','creado_el','modificado']                     # Filtros
    list_per_page = 10                                                                  # Paginación

class DespachoAdmin(admin.ModelAdmin):
    search_fields = ['tipo_despacho','nombre_despacho']                                             # Campos por búsqueda
    list_display = ['id','tipo_despacho','nombre_despacho','creado_el','modificado']                # Campos a mostrar en el panel 
    list_filter = ['tipo_despacho','nombre_despacho','creado_el','modificado']                      # Filtros
    list_per_page = 10                                                                              # Paginación

# Register your models here.
admin.site.register(TipoDespacho, TipoDespachoAdmin)
admin.site.register(Despacho, DespachoAdmin)
