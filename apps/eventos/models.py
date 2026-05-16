from django.db import models

# Create your models here.

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    lugar = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre