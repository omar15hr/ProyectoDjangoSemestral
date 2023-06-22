from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tipo', TipoViewset)
router.register('producto', ProductoViewset)
router.register('categoria', CategoriaViewset)


urlpatterns = [
    path('', include(router.urls)),
]