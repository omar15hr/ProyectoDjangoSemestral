from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import *
from .forms import ProductoForm, TipoProductoForm, TipoClienteForm, ClienteForm
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

def tipoCliente_new(request):
    data = {
        'form_tipoCliente' : TipoClienteForm()
    }
    if request.method == 'POST':
        formulario = TipoClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request,'crud/tipocliente_new.html', data)

def tipoCliente_delete(request, idTipoCliente):
    tipocliente = get_object_or_404(TipoCliente, idTipoCliente=idTipoCliente)
    tipocliente.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="tipocliente_list")

def cliente_new(request):
    data = {
        'form_cliente' : ClienteForm()
    } 
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, 'crud/cliente_new.html', data)

def cliente_delete(request, rutCliente):
    cliente = get_object_or_404(Cliente, rutCliente=rutCliente)
    cliente.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="cliente_list")

def cliente_list(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes' : clientes
    }
    return render(request,'crud/cliente_list.html',data)

def clientes(request):
    clientes = Cliente.objects.all()
    data = {
        'clientes' : clientes
    }
    return render(request,'crud/clientes.html',data)

def cliente_edit(request, rutCliente):
    cliente = get_object_or_404(Cliente, rutCliente=rutCliente)
    data = {
        'form_cliente':ClienteForm(instance=cliente)
    }
    if request.method == 'POST':
        formulario = ClienteForm(data=request.POST, instance=cliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="cliente_list")
        data["form"] = formulario
    return render(request,'crud/cliente_edit.html',data)

def tipoProducto_list(request):
    tipoProductos = TipoProducto.objects.all()
    data = {
        'tipoProductos' : tipoProductos
    }
    return render(request,'crud/tipoProducto_list.html',data)

def tipoProducto_delete(request, idTipoProducto):
    tipoProducto = get_object_or_404(TipoProducto, idTipoProducto=idTipoProducto)
    tipoProducto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="tipoProducto_list")

def tipoProducto_edit(request, idTipoProducto):
    tipoProducto = get_object_or_404(TipoProducto, idTipoProducto=idTipoProducto)
    data = {
        'form':TipoProductoForm(instance=tipoProducto)
    }
    if request.method == 'POST':
        formulario = TipoProducto(data=request.POST, instance=tipoProducto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="tipoProducto_list")
        data["form"] = formulario
    return render(request,'crud/tipoProducto_edit.html',data)

def tipoCliente_edit(request, idTipoCliente):
    tipoCliente = get_object_or_404(TipoCliente, idTipoCliente=idTipoCliente)
    data = {
        'form':TipoClienteForm(instance=tipoCliente)
    }
    if request.method == 'POST':
        formulario = TipoCliente(data=request.POST, instance=tipoCliente, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Modificado correctamente")
            return redirect(to="tipoCliente_list")
        data["form"] = formulario
    return render(request,'crud/tipoCliente_edit.html',data)

def tipoCliente_list(request):
    tipoCliente = TipoCliente.objects.all()
    data = {
        'tipoCliente' : tipoCliente
    }
    return render(request,'crud/tipoCliente_list.html',data)
