from django import forms

class Bebidas_form(forms.Form):
    nombre = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=50)
    precio = forms.FloatField()
    activo = forms.BooleanField()