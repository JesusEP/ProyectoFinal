from django.contrib import admin
from django.urls import path, include
from RestaurantPython.views import index
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bebidas/', include('familia.urls')),
    # path('comidas/', include('productos.urls')),
    path('entradas/', include('entradas.urls')),
    path('', index, name = 'index')
]
