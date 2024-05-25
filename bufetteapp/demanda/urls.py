from django.urls import path 
from .views import SolicitudCreateView, SolicitudListView, SolicitudView, SolicitudEditView

urlpatterns = [
    path('solicitud_nueva/<int:pk>', SolicitudCreateView.as_view(), name= 'solicitud_nueva'),
    path('lista_solicitudes/', SolicitudListView.as_view(), name= 'listasolicitud'),
    # path(),
    # path(),
]