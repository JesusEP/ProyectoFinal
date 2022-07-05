from audioop import reverse
from multiprocessing import context
from django.shortcuts import render
from comidas.models import Comidas
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

def comidas(request):
    comidas = Comidas.objects.all()
    context = {'comidas':comidas}
    return render(request, 'comidas.html', context=context)

# def crear_Comida(request):
#     if request.method == "GET":
#         form = Comidas_form()
#         context = {'form':form}
#         return render(request, 'crear_Comida.html', context=context)
#     else:
#         form = Comidas_form(request.POST)
#         if form.is_valid():
#             nueva_Comida = Comidas.objects.create(
#                 nombre = form.cleaned_data['nombre'],
#                 descripcion = form.cleaned_data['descripcion'],
#                 precio = form.cleaned_data['precio'],
#             )
#             context ={'nueva_Comida':nueva_Comida}
#     return render(request, 'crear_Comida.html', context=context)

def detalle_comida(request, pk):
    try:
        comida = Comidas.objects.get(id=pk)
        context = {'comida':comida}
        return render(request, 'detalle_Comida.html', context=context)
    except:
        context = {'error': 'El producto no existe'}
        return render(request, 'Comidas.html', context=context)

def eliminar_comida(request, pk):
    try:
        if request.method == 'GET':
            comida = Comidas.objects.get(id=pk)
            context = {'comida':comida}
        else:
            comida = Comidas.objects.get(id=pk)
            comida.delete()
            context = {'message':'Producto eliminado correctamente'}
        return render(request, 'eliminar_comida.html', context=context)
    except:
        context = {'error': 'El producto no existe'}
        return render(request, 'eliminar_comida.html', context=context)

class Crear_comida(LoginRequiredMixin, CreateView):
    model = Comidas
    template_name = 'crear_comida.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('detalle-comida', kwargs={'pk':self.object.pk})

class Editar_comida(LoginRequiredMixin, UpdateView):
    model = Comidas
    template_name = 'editar_comida.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle-comida', kwargs={'pk':self.object.pk})