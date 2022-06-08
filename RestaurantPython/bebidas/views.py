from django.shortcuts import render
from django.http import HttpResponse
from bebidas.models import Bebidas
from bebidas.forms import Bebidas_form

# Create your views here.

def bebidas(request):
    bebidas = Bebidas.objects.all()
    context = {'bebidas':bebidas}
    return render(request, 'bebidas.html', context=context)

def crear_bebida(request):
    if request.method == "GET":
        form = Bebidas_form()
        context = {'form':form}
        return render(request, 'crear_bebida.html', context=context)
    else:
        form = Bebidas_form(request.POST)
        if form.is_valid():
            nueva_bebida = Bebidas.objects.create(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
            )
            context ={'nueva_bebida':nueva_bebida}
    return render(request, 'crear_bebida.html', context=context)

