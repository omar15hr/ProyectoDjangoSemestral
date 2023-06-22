from rest_framework import serializers
from crud.models import * 
from dataclasses import field

class TipoSerializer(serializers.ModelSerializer):
    # nombre_producto = serializers.CharField(read_only=True, source="producto.producto")
    # nombre_categoria = serializers.CharField(read_only=True, source="categoria.categoria")
    nombre = serializers.CharField(required=True, min_length=3)

    def validate_nombre(self,value):
        existe = Tipo.objects.filter(nombre__iexact=value).exists()

        if existe:
            raise serializers.ValidationError("Este plato ya existe")
        
        return value


    class Meta:
        model = Tipo 
        fields = (
            'id','nombre', 'producto', 'categoria', 'valor', 'imagen', 'created_at', 'updated_at'
        )

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = (
            'id','producto', 'created_at', 'updated_at'
        )

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = (
            'id','categoria', 'created_at', 'updated_at'
        )