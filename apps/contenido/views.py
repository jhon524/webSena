from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Publicacion

def lista_publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request, 'publicaciones/lista.html', {
        'publicaciones': publicaciones
    })


def detalle_publicacion(request, id):
    publicacion = get_object_or_404(Publicacion, id=id)
    return render(request, 'publicaciones/detalle.html', {
        'publicacion': publicacion
    })