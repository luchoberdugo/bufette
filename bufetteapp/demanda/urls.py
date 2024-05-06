from django.urls import path
from .views import SolicitudDemanda

urlpatterns = [
    path('demanda/', SolicitudDemanda.as_view(), name= 'demanda'),
    # path('registro/', SignUpUserView.as_view(), name= 'registro'),
    # path('detalle_usuario/', AddDetailUserView.as_view(), name= 'detalle_usuario'),
    # path('usuarios/', UserListView.as_view(), name= 'listausuario'),
]