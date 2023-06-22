from django.shortcuts import render, HttpResponse
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view  
from rest_framework import viewsets

from crud.models import *
from .serializers import *

from django.http.response import JsonResponse

class TipoViewset(viewsets.ModelViewSet):
    queryset = Tipo.objects.all()
    serializer_class = TipoSerializer

    def get_queryset(self):
        tipos = Tipo.objects.all()

        nombre = self.request.GET.get('nombre')

        if nombre:
            tipos = tipos.filter(nombre__contains=nombre) #Sin el contains para que el filtro funcione exacto al nombre
        
        return tipos

class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer