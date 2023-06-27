from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('tipoProducto', TipoProductoViewset)
router.register('cliente', ClienteViewset)
router.register('tipoCliente', TipoClienteViewset)


urlpatterns = [
    path('', include(router.urls)),
]