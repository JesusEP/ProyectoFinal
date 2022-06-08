from pipes import Template
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render


# def comidas(request):
#     return render(request, 'familia.html')

def index(request):
    return render(request, 'index.html')

# def bebidas(request):
#     return render(request, 'productos.html')

def entradas(request):
    return render(request, 'entradas.html')