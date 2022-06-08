from django import forms

class Entradas_form(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=50)
    precio = forms.FloatField()
    is_active = forms.BooleanField()