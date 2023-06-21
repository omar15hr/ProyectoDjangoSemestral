from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import TipoForm, Producto, Categoria
from django.contrib import messages

def root(request):
    return redirect(producto_lista)

def producto_lista(request):
    tipos = Tipo.objects.all()

    data = {
        'tipos' : tipos
    }
    return render(request,'crud/producto_lista.html',data)

def producto_nuevo(request): 
    data = {
        'form': TipoForm()
    }

    if request.method == 'POST':
        formulario = TipoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Guardado correctamente")
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    return render(request,'crud/producto_nuevo.html', data)

def producto_modificar(request, id):
    tipo = get_object_or_404(Tipo, id=id)
    data = {
        'form':TipoForm(instance=tipo)
    }

    if request.method == 'POST':
        formulario = TipoForm(data=request.POST, instance=tipo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="producto_lista")
        data["form"] = formulario
    return render(request,'crud/producto_modificar.html',data)

def categoria(request):
    data = {
        'form_categoria' : Categoria(),
        'form_producto' : Producto()
    }

    if request.method == 'POST':
        formulario = Categoria(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario

    if request.method == 'POST':
        formulario = Producto(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request,'crud/categoria.html', data)

def eliminar_producto(request, id):
    tipo = get_object_or_404(Tipo, id=id)
    tipo.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="producto_lista")