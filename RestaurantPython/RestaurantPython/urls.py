from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from RestaurantPython.views import Editar_perfil
from RestaurantPython.views import index, busqueda, login_view, logout_view, register_view, perfil, editar_perfil
from contacto.views import Enviar_solicitud
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
    path('logout/', logout_view, name = 'logout'),
    path('register/', register_view, name = 'register'),
    path('perfil/', perfil, name = 'perfil'),
    path('editar-perfil/', editar_perfil, name = 'editar perfil'),
    path('contacto/', Enviar_solicitud.as_view(), name ='contacto')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)