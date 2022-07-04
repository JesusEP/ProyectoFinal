from django.contrib import admin

# Register your models here.
from bebidas.models import Bebidas

@admin.register(Bebidas)
class BebidasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion']
