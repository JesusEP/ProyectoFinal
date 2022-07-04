from django.urls import URLPattern, path
from entradas.views import entradas, detalle_entrada, eliminar_entrada, Crear_entrada, Editar_entrada

urlpatterns = [
    path('', entradas, name = 'entradas'),
    path('crear-entrada/', Crear_entrada.as_view(), name ='crear-entrada'),
    path('editar-entrada/<int:pk>/', Editar_entrada.as_view(), name ='editar-entrada'),
    path('detalle-entrada/<int:pk>/', detalle_entrada, name ='detalle-entrada'),
    path('eliminar-entrada/<int:pk>/', eliminar_entrada, name ='eliminar-entrada'),
]