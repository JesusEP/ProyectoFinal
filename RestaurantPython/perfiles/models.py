from django.db import models
from django.contrib.auth.models import User

class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to='profile_image')
    
    class Meta:
        verbose_name = 'perfil'
        verbose_name_plural = 'perfiles'