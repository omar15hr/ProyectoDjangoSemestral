from django.urls import path 
from .views import *

urlpatterns = [
    path('', root),
    path('productos/', productos, name='productos'),
    path('producto_lista/', producto_lista, name='producto_lista'),
    path('producto_nuevo/', producto_nuevo, name='producto_nuevo'),
    path('producto_modificar/<id>/', producto_modificar, name='producto_modificar'),
    path('categoria/', categoria, name='categoria'),
    path('eliminar_producto/<id>/', eliminar_producto, name="eliminar_producto"),
]