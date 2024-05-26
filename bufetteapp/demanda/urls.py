from django.urls import path 
from .views import SolicitudCreateView, SolicitudesDesatendidasListView, SolicitudActivacionView, SolicitudListView, SolicitudView, SolicitudEditView, DetalleSolicitudCreate, ExpedienteCreateView, ExpedienteListView

urlpatterns = [
    path('solicitud_nueva/<int:pk>', SolicitudCreateView.as_view(), name= 'solicitud_nueva'),
    path('solicitud_listar/', SolicitudesDesatendidasListView.as_view(), name= 'solicitud_listar'),
    path('lista_solicitudes_asignadas/', SolicitudListView.as_view(), name= 'listasolicitudasignadas'),
    path('activar_solicitud/<uuid:pk>', SolicitudActivacionView.as_view(), name='activar_solicitud'),
    path('asignar_abogado/<uuid:pk>', DetalleSolicitudCreate.as_view(), name= 'asignar_abogado'),
    # Rutas de expediente:
    path('expediente_nuevo/<uuid:pk>', ExpedienteCreateView.as_view(), name= 'expediente_nuevo'),
    path('lista_expedientes/', ExpedienteListView.as_view(), name= 'expediente_listar'),
]