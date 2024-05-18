from django.urls import path
from .views import DashboardUserView, SignUpUserView, AddDetailUserView, UserListView, UserEditView, UserActivateOrDeactivateView, AddIdProfessionalView, PerfilUserView

urlpatterns = [
    path('inicio/', DashboardUserView.as_view(), name= 'dashboard'),
    path('registro/', SignUpUserView.as_view(), name= 'registro'),
    path('detalle_usuario/', AddDetailUserView.as_view(), name= 'detalle_usuario'),
    path('usuarios/', UserListView.as_view(), name= 'listausuario'),
    path('editar_usuario/<int:pk>', UserEditView.as_view(), name= 'editausuario'),
    path('editar_estado/<int:pk>', UserActivateOrDeactivateView.as_view(), name= 'editaestado'),
    path('add_idprofesional/', AddIdProfessionalView.as_view(), name= 'tarjeta_profesional'),
    path('perfil_usuario/', PerfilUserView.as_view(), name= 'perfil_usuario'),
]