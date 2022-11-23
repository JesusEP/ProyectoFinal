from audioop import reverse
from multiprocessing import context
from urllib import request
from django.shortcuts import render
from perfiles.models import User_profile
from django.views.generic import CreateView, UpdateView
from django.urls import reverse

# Create your views here.
class UserEditForm(request):
    email = forms.EmailFIeld(label= 'Modificar E-Mail')
    password1 = forms.Charfield(label= 'Contraseña', Widget=forms.PasswordInput)
    password2 = forms.Charfield(label= 'Repita contraseña', Widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ['email','password1','password2']
