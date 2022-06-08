from django.shortcuts import render
from django.http import HttpResponse
from comidas.models import Comidas
from comidas.forms import Comidas_form

def comidas(request):
    comidas = Comidas.objects.all()
    context = {'comidas':comidas}
    return render(request, 'comidas.html', context=context)

def crear_comida(request):
    if request.method == "GET":
        form = Comidas_form()
        context = {'form':form}
        return render(request, 'crear_comida.html', context=context)
    else:
        form = Comidas_form(request.POST)
        if form.is_valid():
            nueva_comida = Comidas.objects.create(
                nombre = form.cleaned_data['nombre'],
                descripcion = form.cleaned_data['descripcion'],
                precio = form.cleaned_data['precio'],
            )
            context ={'nueva_comida':nueva_comida}
    return render(request, 'crear_comida.html', context=context)

