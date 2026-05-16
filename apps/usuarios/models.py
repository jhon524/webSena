from django.db import models

# Create your models here.

class Rol(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)

    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre