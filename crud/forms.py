from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = [
            'idProducto',
            'nombreProducto',
            'precioProducto',
            'stockProducto',
            'idTipoProducto',
        ]
        labels = {
            'idProducto':'Código Producto',
            'nombreProducto':'Nombre Producto',
            'precioProducto':'Precio',
            'stockProducto':'Cantidad',
            'idTipoProducto':'Código Producto',
        }
        widgets = {
            'idProducto':forms.TextInput(attrs={'class':'form-control'}),
            'nombreProducto':forms.TextInput(attrs={'class':'form-control'}),
            'precioProducto':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'stockProducto':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'idTipoProducto':forms.TextInput(attrs={'class':'form-control','type':'number'})
        }

