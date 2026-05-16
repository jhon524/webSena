from django.contrib import admin

# Register your models here.
from .models import Categoria, Publicacion, Multimedia, Detalle
admin.site.register(Categoria),
admin.site.register(Publicacion),
admin.site.register(Multimedia),
admin.site.register(Detalle)
