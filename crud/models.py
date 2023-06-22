from django.db import models
import os

# Create your models here.

class TipoCliente(models.Model):
    idTipoCliente = models.IntegerField(primary_key=True,verbose_name='Código Tipo Cliente')
    nombreTC = models.CharField(verbose_name='Descripción Cliente',max_length=30)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'tipoCliente'
        verbose_name_plural = 'tipoClientes'
        ordering = ['idTipoCliente']

    def __str__(self) -> str:
        return self.idTipoCliente

class Cliente(models.Model):
    rutCliente = models.IntegerField(primary_key=True,verbose_name='Rut Cliente')
    dvRutCliente = models.CharField(verbose_name='DvRut Cliente',max_length=1)
    nombreCliente = models.CharField(verbose_name='Nombre Cliente',max_length=100)
    telefonoCliente = models.IntegerField(verbose_name="Teléfono Cliente")
    emailCiente = models.EmailField(verbose_name='Email Cliente',max_length=100)
    idTipoCliente = models.ForeignKey(TipoCliente,verbose_name='Código Tipo Cliente',on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['rutCliente']

    def __str__(self) -> str:
        return self.rutCliente
    
class TipoProducto(models.Model):
    idTipoProducto = models.IntegerField(primary_key=True,verbose_name='Código Tipo Producto')
    nombreTP = models.CharField(verbose_name='Descripción Producto',max_length=30)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'tipoProducto'
        verbose_name_plural = 'tipoProductos'
        ordering = ['idTipoProducto']

    def __str__(self) -> str:
        return self.idTipoProducto
    
    
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True,verbose_name='Código Producto')
    nombreProducto = models.CharField(verbose_name='Nombre Producto',max_length=50)
    precioProducto = models.IntegerField(verbose_name='Precio')
    stockProducto = models.IntegerField(verbose_name='Cantidad')
    idTipoProducto = models.ForeignKey(TipoProducto,verbose_name='Código Tipo Producto',on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['idProducto','nombreProducto']

    def __str__(self) -> str:
        return self.idProducto
    

