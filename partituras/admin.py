from django.contrib import admin
from .models import Partitura

@admin.register(Partitura)
class PartituraAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'compositor', 'genero', 'dificultad', 'visibilidad', 'usuario')
    list_filter = ('genero', 'dificultad', 'visibilidad')
    search_fields = ('titulo', 'compositor', 'arreglista')