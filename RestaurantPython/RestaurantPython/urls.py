from unicodedata import name
from django.contrib import admin
from django.urls import path, include, URLPattern
#from RestaurantPython.views import perfiles
from RestaurantPython.views import index, busqueda, login_view, logout_view, register_view
from django.conf import settings
from django.conf.urls.static import static
from perfiles.views import UserEditForm


                                                                        
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
    path('perfiles/',  UserEditForm.as_view(), name= 'Perfiles')
]
