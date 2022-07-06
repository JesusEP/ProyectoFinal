from django.db import models

class Contacto(models.Model):
    nombre = models.CharField(max_length=30)
    email = models.EmailField(max_length=50, blank=True, null=True)
    asunto = models.CharField(max_length=30, blank=True, null=True)
    mensaje = models.TextField(max_length=600, blank=True, null=True)
    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'