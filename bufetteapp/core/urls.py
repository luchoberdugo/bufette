from django.urls import path 
from .views import IndexPageView, NosotrosPageView

urlpatterns =[
    path('', IndexPageView.as_view(), name= 'inicio'),
    path('nosotros/',NosotrosPageView.as_view(), name='nosotros'),
]
