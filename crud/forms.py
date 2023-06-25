from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import ValidationError

class TipoClienteForm(models.Model):
    model: TipoCliente
    fields =[
        'idTipoCliente',
        'nombreTC',
    ]
    labels = {
        'idTipoCliente':'Código Tipo Cliente',
        'nombreTC':'Descripción Cliente',
    }
    widgets = {
        'idTipoCliente':forms.TextInput(attrs={'class':'form-control','type':'number'}),
        'nombreTC':forms.TextInput(attrs={'class':'form-control'}),
    }


class ClienteForm(ModelForm):
    model: Cliente
    fields = [
        'rutCliente',
        'dvRutCliente',
        'nombreCliente',
        'telefonoCliente',
        'emailCliente',
        'idTipoCliente',
    ]
    labels = {
        'rutCliente':'Rut Cliente',
        'dvRutCliente':'DvRut Cliente',
        'nombreCliente':'Nombre Cliente',
        'telefonoCliente':'Teléfono Cliente',
        'emailCliente':'Email Cliente',
        'idTipoCliente':'Código Tipo Cliente',

    }
    widgets = {
        'rutCliente':forms.TextInput(attrs={'class':'form-control','type':'number'}),
        'dvRutCliente':forms.TextInput(attrs={'class':'form-control'}),
        'nombreCliente':forms.TextInput(attrs={'class':'form-control'}),
        'telefonoCliente':forms.TextInput(attrs={'class':'form-control','type':'number'}),
        'emailCliente':forms.EmailField(attrs={'class':'form-control'}),
        'idTipoCliente':forms.TextInput(attrs={'class':'form-control','type':'number'}),
    }

class TipoProductoForm(models.Model):
    model: TipoProducto
    fields =[
        'idTipoProducto',
        'nombreTP',
    ]
    labels = {
        'idTipoProducto':'Código Tipo Producto',
        'nombreTP':'Descripción Producto',
    }
    widgets = {
        'idTipoProducto':forms.TextInput(attrs={'class':'form-control','type':'number'}),
        'nombreTP':forms.TextInput(attrs={'class':'form-control'}),
    }

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'nombreProducto':forms.TextInput(attrs={'class':'form-control'}),
            'precioProducto':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'imagenProducto':forms.FileInput(attrs={'class':'form-control'}),
            'TipoProducto':forms.Select(attrs={'class':'form-control'})
        }

class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = '__all__'
        widgets = {
            'nombreTP':forms.TextInput(attrs={'class':'form-control'})
        }

