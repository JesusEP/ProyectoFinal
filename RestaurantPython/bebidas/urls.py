from django.urls import URLPattern, path
from bebidas.views import bebidas, detalle_bebida, eliminar_bebida, Crear_bebida, Editar_bebida

urlpatterns = [
    path('', bebidas, name = 'bebidas'),
    path('crear-bebida/', Crear_bebida.as_view(), name ='crear-bebida'),
    path('editar-bebida/<int:pk>/', Editar_bebida.as_view(), name ='editar-bebida'),
    path('detalle-bebida/<int:pk>/', detalle_bebida, name ='detalle-bebida'),
    path('eliminar-bebida/<int:pk>/', eliminar_bebida, name ='eliminar-bebida'),
]