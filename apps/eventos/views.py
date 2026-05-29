from django.shortcuts import render
from .models import Evento

# Create your views here.

def lista_eventos(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista.html', {
        'eventos': eventos
    })