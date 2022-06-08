from django.urls import URLPattern, path
from entradas.views import entradas, crear_entrada

urlpatterns = [
    path('', entradas, name = 'entradas'),
    path('crear-entrada/', crear_entrada, name='crear-entrada'),
] 