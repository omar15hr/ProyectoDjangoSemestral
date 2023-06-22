from django.db import models 
import os

# Create your models here.
class Producto(models.Model):
    producto = models.CharField(verbose_name='Producto', max_length=20)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'
        ordering = ['producto']
    
    def __str__(self) -> str: 
        return self.producto

class Categoria(models.Model):
    categoria = models.CharField(verbose_name='Categoria', max_length=20)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['categoria']

    def __str__(self) -> str:
        return self.categoria

class Tipo(models.Model):
    nombre = models.CharField(verbose_name='Nombre', max_length=20)
    producto = models.ForeignKey(Producto, verbose_name='Producto', on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE)
    valor = models.IntegerField(verbose_name='Valor unitario')
    imagen = models.ImageField(verbose_name='Imagen', upload_to='platos', null=True,blank=True)
    created_at = models.DateTimeField(verbose_name='Fecha registro',auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha actualización',auto_now=True)

    class Meta:
        verbose_name = 'tipo'
        verbose_name_plural = 'tipos'
        ordering = ['nombre','producto']

    def __str__(self) -> str:
        return self.nombre