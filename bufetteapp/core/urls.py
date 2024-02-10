from django.urls import path 
from .views import IndexPageView, NosotrosPageView, ContactoPageView

urlpatterns =[
    path('', IndexPageView.as_view(), name= 'inicio'),
    path('nosotros/',NosotrosPageView.as_view(), name='nosotros'),
    path('contacto/', ContactoPageView.as_view(), name='contacto'),
]

