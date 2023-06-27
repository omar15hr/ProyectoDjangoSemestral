from rest_framework import serializers
from crud.models import * 
from dataclasses import field

class ProductoSerializer(serializers.ModelSerializer):
    # nombre_producto = serializers.CharField(read_only=True, source="producto.producto")
    # nombre_categoria = serializers.CharField(read_only=True, source="categoria.categoria")
    nombreProducto = serializers.CharField(required=True, min_length=3)

    def validate_nombre(self,value):
        existe = Producto.objects.filter(nombreProducto__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este producto ya existe")
        
        return value


    class Meta:
        model = Producto 
        fields = '__all__'

class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class TipoClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
