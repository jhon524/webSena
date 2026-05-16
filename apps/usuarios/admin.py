from django.contrib import admin

# Register your models here.
from .models import Rol, Usuario
admin.site.register(Rol),
admin.site.register(Usuario)