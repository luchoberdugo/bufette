from django.urls import path 
from .views import SolicitudCreateView, SolicitudesDesatendidasListView, SolicitudActivacionView, SolicitudListView, SolicitudView, SolicitudEditView, DetalleSolicitudCreate, ExpedienteCreateView, ExpedienteListView, PruebasExpedienteView, ActuacionesExpedienteView, ExpedienteInformeView

urlpatterns = [
    path('solicitud_nueva/<int:pk>', SolicitudCreateView.as_view(), name= 'solicitud_nueva'),
    path('solicitud_listar/', SolicitudesDesatendidasListView.as_view(), name= 'solicitud_listar'),
    path('lista_solicitudes_asignadas/', SolicitudListView.as_view(), name= 'listasolicitudasignadas'),
    path('activar_solicitud/<uuid:pk>/', SolicitudActivacionView.as_view(), name='activar_solicitud'),
    path('asignar_abogado/<uuid:pk>/', DetalleSolicitudCreate.as_view(), name= 'asignar_abogado'),
    path('ver_solicitud/<uuid:pk>/', SolicitudView.as_view(), name= 'ver_solicitud'),
    # Rutas de pruebas
    path('pruebas_actos/<uuid:pk>/', PruebasExpedienteView.as_view(), name= 'addpruebas'),
    # Rutas de expediente:
    path('expediente_nuevo/<uuid:pk>', ExpedienteCreateView.as_view(), name= 'expediente_nuevo'),
    path('lista_expedientes/', ExpedienteListView.as_view(), name= 'expediente_listar'),
    # Rutas de actuaciones
    path('agrega_actos/<int:pk>/', ActuacionesExpedienteView.as_view(), name= 'addactuaciones'),
    path('informe_expediente/<int:pk>/', ExpedienteInformeView.as_view(), name= 'informeexpediente' )
]