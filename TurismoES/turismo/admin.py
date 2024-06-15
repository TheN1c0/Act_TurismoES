from django.contrib import admin
from .models import Genero, Alumno, Servicios
# Register your models here.
admin.site.register(Genero)

admin.site.register(Alumno)
admin.site.register(Servicios)