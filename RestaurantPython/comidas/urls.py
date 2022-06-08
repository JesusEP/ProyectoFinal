from django.urls import URLPattern, path
from comidas.views import comidas, crear_comida

urlpatterns = [
    path('', comidas, name = 'comidas'),
    path('crear-comida/', crear_comida, name ='crear-comida'),

]