from django.db import models

class Entradas(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=50, blank=True, null=True)
    precio = models.FloatField()
    is_active = models.BooleanField(default=True)
    class Meta:
        verbose_name = 'entrada'
        verbose_name_plural = 'entradas'