from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    fecha_reserva = models.CharField(max_length=10)
    cantidad_personas = models.CharField(max_length=2)
    comentario = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre
    