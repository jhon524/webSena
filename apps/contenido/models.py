from django.db import models

# Create your models here.
from apps.usuarios.models import Usuario

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Publicacion(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class Multimedia(models.Model):
    archivo = models.FileField(upload_to='multimedia/')
    tipo = models.CharField(max_length=50)

    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo


class Detalle(models.Model):
    descripcion = models.TextField()

    publicacion = models.OneToOneField(
        Publicacion,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Detalle {self.publicacion.titulo}"