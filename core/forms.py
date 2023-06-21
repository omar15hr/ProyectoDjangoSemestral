from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'
        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingrese su nombre y apellido'}),
            'correo':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese su correo electronico'}),
            'fecha_reserva':forms.SelectDateWidget(attrs={'class':'form-control','placeholder':'Ingrese la fecha de reserva'}),
            'cantidad_personas':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la cantidad de personas'}),
            'comentario':forms.Textarea(attrs={'class':'form-control','placeholder':'Agregue un comentario'}),
        }