from django.contrib import admin
from comidas.models import Comidas

@admin.register(Comidas)
class ComidasAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'descripcion']


