from django.shortcuts import render, HttpResponse, redirect
from django.urls import resolve
from crud.models import *

# Create your views here.
def root(request):
    return redirect('index')

def index(request):
    return render(request,'core/index.html')

def productos(request):
    mostrar_en_navbar = True
    return render(request,'core/productos.html', {'mostrar_en_navbar': mostrar_en_navbar})

def eventos(request):
    return render(request,'core/eventos.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def contacto(request):
    return render(request,'core/contacto.html')
