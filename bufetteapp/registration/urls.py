from django.urls import path
from .views import DashboardUserView

urlpatterns = [
    path('inicio/', DashboardUserView.as_view(), name= 'dashboard'),
]