from multiprocessing import context
from pipes import Template
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render
from entradas.models import Entradas
from bebidas.models import Bebidas
from comidas.models import Comidas
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}!! :)'}
                return render(request, 'index.html', context = context)
            else:  
                context = {'errors':'No hay ningun usuario con esas credenciales!!!'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors':errors, 'form':form} 
            return render(request, 'auth/login.html', context = context)       

    else:
        form = AuthenticationForm()
        context = {'form':form}
        return render(request, 'auth/login.html', context = context )              


def comidas(request):
     return render(request, 'familia.html')

def index(request):
    print(request.user)
    print(request.user.is_authenticated)
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