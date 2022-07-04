from django.urls import URLPattern, path
from comidas.views import comidas, detalle_comida, eliminar_comida, Crear_comida, Editar_comida

urlpatterns = [
    path('', comidas, name = 'comidas'),
    path('crear-comida/', Crear_comida.as_view(), name ='crear-comida'),
    path('editar-comida/<int:pk>/', Editar_comida.as_view(), name ='editar-comida'),
    path('detalle-comida/<int:pk>/', detalle_comida, name ='detalle-comida'),
    path('eliminar-comida/<int:pk>/', eliminar_comida, name ='eliminar-comida'),
]