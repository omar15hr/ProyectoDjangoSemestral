from django.shortcuts import render, HttpResponse, redirect
from crud.models import *

# Create your views here.
def root(request):
    return redirect('index')

def index(request):
    return render(request,'core/index.html')

def productos(request):
    return render(request,'core/productos.html')

def eventos(request):
    return render(request,'core/eventos.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def contacto(request):
    return render(request,'core/contacto.html')
