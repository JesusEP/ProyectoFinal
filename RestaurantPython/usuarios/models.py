from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='perfil_usuario')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=20, blank=True, null=True)
    sitio_web = models.URLField(max_length=40, blank=True, null=True)
    foto_de_perfil = models.ImageField(upload_to='fotos_perfil', null=True, blank=True)
    class Meta:
            verbose_name = 'perfil'
            verbose_name_plural = 'perfiles'