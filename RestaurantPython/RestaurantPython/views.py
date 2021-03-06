from importlib.metadata import files
from multiprocessing import context
from pipes import Template
from re import template
from django.shortcuts import render, redirect
from usuarios.models import User_profile
from entradas.models import Entradas
from bebidas.models import Bebidas
from comidas.models import Comidas
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from RestaurantPython.forms import User_registration_form, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                context = {'message':f'Bienvenido {username}'}
                return render(request, 'index.html', context = context)
            else:  
                context = {'errors':'Usuario o contraseña incorrectos'}
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

def logout_view(request):
    logout(request)
    return redirect('/')

def perfil(request):
    return render(request, 'perfil.html')

def register_view(request):
    if request.method == 'POST':
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            context = {'message':f'Usuario creado correctamente, bienvenid@ {username}'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_registration_form()
            context = {'errors':errors, 'form':form}
            return render(request, 'auth/register.html', context = context )   
    else:
        form = User_registration_form()
        context = {'form': form}
        return render(request, 'auth/register.html', context = context )     



def comidas(request):
    return render(request, 'comidas.html')

def index(request):
    # print(request.user)
    # print(request.user.is_authenticated)
    return render(request, 'index.html')

def bebidas(request):
    return render(request, 'bebidas.html')

def entradas(request):
    return render(request, 'entradas.html')

def busqueda(request):
    buscar_entradas = Entradas.objects.filter(nombre__icontains = request.GET['search'])
    buscar_bebidas = Bebidas.objects.filter(nombre__icontains = request.GET['search'])
    buscar_comidas = Comidas.objects.filter(nombre__icontains = request.GET['search'])
    context = {'buscar_entradas':buscar_entradas, 'buscar_bebidas':buscar_bebidas, 'buscar_comidas':buscar_comidas}
    return render(request, 'busqueda.html', context=context)

def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        miForm = UserEditForm(request.POST, request.FILES)
        if miForm.is_valid():
            informacion = miForm.cleaned_data
            usuario.nombre = informacion['nombre']
            usuario.apellido = informacion['apellido']
            usuario.sitio_web = informacion['sitio_web']
            usuario.telefono = informacion['telefono']
            usuario.foto_de_perfil = informacion['foto_de_perfil']
            usuario.save()
            return render (request, 'perfil.html')
    else:
        miForm=UserEditForm(initial={'email':usuario.email})
    return render(request, 'editar_perfil.html', {'miForm':miForm, 'usuario':usuario})

class Editar_perfil(LoginRequiredMixin, UpdateView):
    model = User_profile
    template_name = 'editar_perfil.html'
    fields = '__all__'
