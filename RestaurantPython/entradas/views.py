from django.shortcuts import render
from django.http import HttpResponse
from entradas.models import Entradas
from entradas.forms import Entradas_form

def entradas(request):
    entradas = Entradas.objects.all()
    context = {'entradas':entradas}
    return render(request, 'entradas.html', context=context)

def crear_entrada(request):
    if request.method == "GET":
        form = Entradas_form()
        context = {'form':form}
        return render(request, 'crear_entrada.html', context=context)
    else:
        form = Entradas_form(request.POST)
        if form.is_valid():
            nueva_entrada = Entradas.objects.create(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
            )
            context ={'nueva_entrada':nueva_entrada}
    return render(request, 'crear_entrada.html', context=context)
