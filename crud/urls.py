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
    path('tipoProducto_list/', tipoProducto_list, name='tipoProducto_list'),
    path('tipoProducto_delete/<idTipoProducto>/', tipoProducto_delete, name="tipoProducto_delete"),
    path('tipoProducto_edit/<idTipoProducto>/', tipoProducto_edit, name='tipoProducto_edit'),
    path('tipoCliente_new', tipoCliente_new,name='tipoCliente_new'),
    path('tipoCliente_list/', tipoCliente_list, name='tipoCliente_list'),
    path('tipoCliente_delete/<rutCliente>/', tipoCliente_delete, name="tipoCliente_delete"),
    path('tipoCliente_edit/<rutCliente>/', tipoCliente_edit, name='tipoCliente_edit'),
    path('clientes/', clientes, name='clientes'),
    path('cliente_list/', cliente_list, name='cliente_list'),
    path('cliente_new/', cliente_new, name='cliente_new'),
    path('cliente_edit/<rutCliente>/', cliente_edit, name='cliente_edit'),
    path('cliente_delete/<rutCliente>/', cliente_delete, name="cliente_delete"),
]