from multiprocessing import context
from pipes import Template
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from entradas.models import Entradas
from bebidas.models import Bebidas
from comidas.models import Comidas

def comidas(request):
     return render(request, 'familia.html')

def index(request):
    return render(request, 'index.html')

def bebidas(request):
     return render(request, 'productos.html')

def entradas(request):
    return render(request, 'entradas.html')

def busqueda(request):
    buscar_entradas = Entradas.objects.filter(nombre__icontains = request.GET['search'])
    buscar_bebidas = Bebidas.objects.filter(nombre__icontains = request.GET['search'])
    buscar_comidas = Comidas.objects.filter(nombre__icontains = request.GET['search'])
    context = {'buscar_entradas':buscar_entradas, 'buscar_bebidas':buscar_bebidas, 'buscar_comidas':buscar_comidas}
    return render(request, 'busqueda.html', context=context)