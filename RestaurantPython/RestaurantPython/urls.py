from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from RestaurantPython.views import index, busqueda, login_view
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('bebidas/', include('bebidas.urls')),
    path('comidas/', include('comidas.urls')),
    path('entradas/', include('entradas.urls')),
    path('busqueda/', busqueda, name = 'busqueda'),
    path('', index, name = 'index'),
    path('login/', login_view, name = 'login'),
]
