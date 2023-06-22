from django import forms
from .models import *
from django.forms import ModelForm
from django.forms import ValidationError

class TipoForm(forms.ModelForm):

    nombre = forms.CharField(min_length=5, max_length=20)
    valor = forms.IntegerField(min_value=3990, max_value=19990)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Tipo.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este nombre ya existe")
        return nombre

    class Meta:
        model = Tipo
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control'}),
            'producto':forms.Select(attrs={'class':'form-control'}),
            'categoria':forms.Select(attrs={'class':'form-control'}),
            'valor':forms.TextInput(attrs={'class':'form-control'}),
            'imagen':forms.FileInput(attrs={'class':'form-control'})
        }

class Producto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class Categoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'