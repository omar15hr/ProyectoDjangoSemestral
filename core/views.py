from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

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
    data = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado."
        else:
            data["form"] = formulario

    return render(request,'core/contacto.html', data)

def contacto_list(request):
    # formulario = Formulario.objects.all()
    # data = {
    #     'formulario' : formulario
    # }
    return render(request, 'core/contacto_list.html')