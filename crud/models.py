from django.db import models

# Create your models here.


class Customer(models.Model):
    rutCustomer = models.IntegerField(primary_key=True,verbose_name='Rut',max_length=8)
    dvRutCustomer = models.CharField(verbose_name='DvRut',max_length=1)
    nameCustomer = models.CharField(verbose_name='Nombre',max_length=100)
    telephoneCustomer = models.IntegerField(verbose_name="Teléfono",max_length=9)
    emailCustomer = models.EmailField(verbose_name='Email',max_length=100)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        ordering = ['rutCustomer']

    def __str__(self) -> str:
        return self.rutCustomer

class Product(models.Model):
    idProduct = models.IntegerField(primary_key=True,verbose_name='Código Producto',max_length=6)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['idProduct']

    def __str__(self) -> str:
        return self.idProduct

class Order(models.Model):
    idOrder = models.IntegerField(primary_key=True,verbose_name='Id Pedido',max_length=6)
    rutCustomer = models.ForeignKey(Customer,verbose_name='Rut',on_delete=models.CASCADE)
    idProduct = models.ForeignKey(Product,verbose_name='Código Producto',on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
        ordering = ['idOrder,rutCustomer,idProduct']

    def __str__(self) -> str:
        return self.idOrder


