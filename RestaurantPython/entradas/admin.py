from django.contrib import admin
from entradas.models import Entradas

@admin.register(Entradas)
class EntradasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion']

