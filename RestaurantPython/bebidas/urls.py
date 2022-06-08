from django.urls import URLPattern, path
from bebidas.views import bebidas, crear_bebida

urlpatterns = [
    path('', bebidas, name = 'bebidas'),
    path('crear-bebida/', crear_bebida, name ='crear-bebida'),

]