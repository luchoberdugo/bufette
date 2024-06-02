from django.urls import path 
from .views import FiltroCiudades

urlpatterns =[
    path('ciudades/', FiltroCiudades.as_view(), name= 'ciudades'),
]

