from django import forms
from .models import *

class TipoForm(forms.ModelForm):

    class Meta:
        model = Tipo
        fields = '__all__'

class Producto(forms.ModelForm):

    class Meta:
        model = Producto
        fields = '__all__'

class Categoria(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'