from django.urls import path
from .views import DashboardUserView, SignUpUserView, AddDetailUserView, UserListView, UserEditView

urlpatterns = [
    path('inicio/', DashboardUserView.as_view(), name= 'dashboard'),
    path('registro/', SignUpUserView.as_view(), name= 'registro'),
    path('detalle_usuario/', AddDetailUserView.as_view(), name= 'detalle_usuario'),
    path('usuarios/', UserListView.as_view(), name= 'listausuario'),
    path('editar_usuario/<int:pk>', UserEditView.as_view(), name= 'editausuario'),
]