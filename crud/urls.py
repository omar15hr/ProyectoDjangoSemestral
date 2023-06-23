from django.urls import path 
from .views import *

urlpatterns = [
    path('', producto_list),
    path('productos/', productos, name='productos'),
    path('producto_list/', producto_list, name='producto_list'),
    path('producto_new/', producto_new, name='producto_new'),
    path('producto_edit/<idProducto>/', producto_edit, name='producto_edit'),
    path('producto_delete/<idProducto>/', producto_delete, name="producto_delete"),
    path('tipoProducto_new', tipoProducto_new,name='tipoProducto_new'),
]