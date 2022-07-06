from django import forms
from contacto.models import Contacto

class Contacto_form(forms.Form):
    class Meta:
        model = Contacto
        fields = "__all__"