from django.shortcuts import render
from audioop import reverse
from contacto.forms import Contacto_form
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class Enviar_solicitud(LoginRequiredMixin, CreateView):
    model = Contacto_form
    template_name = 'contacto.html'
    fields ='__all__'

