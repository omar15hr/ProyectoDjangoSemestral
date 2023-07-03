from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import ValidationError

class TipoClienteForm(forms.ModelForm):
    class Meta:
        model = TipoCliente
        fields =[
            'nombreTC',
        ]
        widgets = {
            'nombreTC':forms.TextInput(attrs={'class':'form-control'}),
        }


class ClienteForm(forms.ModelForm):

    nombreCliente = forms.CharField(min_length=1, max_length=20)
    dvRutCliente = forms.CharField(min_length=1, max_length=1)
    rutCliente = forms.CharField(min_length=7, max_length=8)
    emailCliente = forms.EmailField(min_length=11,max_length=30)
    telefonoCliente = forms.IntegerField(min_value=900000000, max_value=999999999)

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'rutCliente':forms.TextInput(attrs={'class':'form-control'}),
            'dvRutCliente':forms.TextInput(attrs={'class':'form-control'}),
            'nombreCliente':forms.TextInput(attrs={'class':'form-control'}),
            'telefonoCliente':forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'emailCliente':forms.EmailInput(attrs={'class':'form-control'}),
            'nombreTC':forms.Select(attrs={'class':'form-control'}),
        }

class ProductoForm(forms.ModelForm):

    nombreProducto = forms.CharField(min_length=5, max_length=20)
    precioProducto = forms.IntegerField(min_value=3990, max_value=19990)

    def clean_nombre(self):
        nombreProducto = self.cleaned_data["nombre"]
        existe = Producto.objects.filter(nombre__iexact=nombreProducto).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombreProducto

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

