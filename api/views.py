from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view  
from rest_framework import viewsets

from crud.models import *
from .serializers import *

from django.http.response import JsonResponse

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def get_queryset(self):
        productos = Producto.objects.all()

        nombreProducto = self.request.GET.get('nombreProducto')

        if nombreProducto:
            productos = productos.filter(nombreProducto__contains=nombreProducto) #Sin el contains para que el filtro funcione exacto al nombre
        
        return productos

class TipoProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer