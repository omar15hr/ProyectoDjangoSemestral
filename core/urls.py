from django.urls import path
from .views import *

urlpatterns = [
    path('', root),
    path('index/', index, name='index'),
    path('productos/', productos, name='productos'),
    path('eventos/', eventos, name='eventos'),
    path('nosotros/', nosotros, name='nosotros'),
    path('contacto/', contacto, name='contacto'),
    path('contacto_list/', contacto_list, name='contacto_list')
]