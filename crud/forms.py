from django import forms
from django.forms import ModelForm
from .models import *
from django.forms import ValidationError

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

