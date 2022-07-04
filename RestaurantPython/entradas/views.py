from audioop import reverse
from multiprocessing import context
from django.shortcuts import render
from entradas.models import Entradas
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

def entradas(request):
    entradas = Entradas.objects.all()
    context = {'entradas':entradas}
    return render(request, 'entradas.html', context=context)

# def crear_entrada(request):
#     if request.method == "GET":
#         form = entradas_form()
#         context = {'form':form}
#         return render(request, 'crear_entrada.html', context=context)
#     else:
#         form = entradas_form(request.POST)
#         if form.is_valid():
#             nueva_entrada = entradas.objects.create(
#                 nombre = form.cleaned_data['nombre'],
#                 descripcion = form.cleaned_data['descripcion'],
#                 precio = form.cleaned_data['precio'],
#             )
#             context ={'nueva_entrada':nueva_entrada}
#     return render(request, 'crear_entrada.html', context=context)

def detalle_entrada(request, pk):
    try:
        entrada = Entradas.objects.get(id=pk)
        context = {'entrada':entrada}
        return render(request, 'detalle_entrada.html', context=context)
    except:
        context = {'error': 'El producto no existe'}
        return render(request, 'entradas.html', context=context)

def eliminar_entrada(request, pk):
    try:
        if request.method == 'GET':
            entrada = Entradas.objects.get(id=pk)
            context = {'entrada':entrada}
        else:
            entrada = Entradas.objects.get(id=pk)
            entrada.delete()
            context = {'message':'Producto eliminado correctamente'}
        return render(request, 'eliminar_entrada.html', context=context)
    except:
        context = {'error': 'El producto no existe'}
        return render(request, 'eliminar_entrada.html', context=context)

class Crear_entrada(LoginRequiredMixin, CreateView):
    model = Entradas
    template_name = 'crear_entrada.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('detalle-entrada', kwargs={'pk':self.object.pk})

class Editar_entrada(LoginRequiredMixin, UpdateView):
    model = Entradas
    template_name = 'editar_entrada.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle-entrada', kwargs={'pk':self.object.pk})