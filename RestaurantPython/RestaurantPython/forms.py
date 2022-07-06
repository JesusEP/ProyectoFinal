from dataclasses import fields
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from usuarios.models import  User_profile

class User_registration_form(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k: '' for k in fields}


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = "__all__"