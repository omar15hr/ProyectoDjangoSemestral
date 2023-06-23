from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import ProductoForm, TipoProductoForm
from django.contrib import messages

def root(request):
    return redirect(producto_lista)

def producto_list(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request,'crud/producto_list.html',data)

def productos(request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request,'crud/productos.html',data)

def producto_new(request): 
    data = {
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Guardado correctamente")
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request,'crud/producto_new.html', data)

def producto_edit(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    data = {
        'form':ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="producto_list")
        data["form"] = formulario
    return render(request,'crud/producto_edit.html',data)

def tipoProducto_new(request):
    data = {
        'form_tipoProducto' : TipoProductoForm()
    }
    if request.method == 'POST':
        formulario = TipoProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request,'crud/tipoProducto_new.html', data)

def producto_delete(request, idProducto):
    producto = get_object_or_404(Producto, idProducto=idProducto)
    producto.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="producto_list")