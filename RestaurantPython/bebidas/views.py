from audioop import reverse
from multiprocessing import context
from django.shortcuts import render
from bebidas.models import Bebidas
from django.views.generic import CreateView, UpdateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

def bebidas(request):
    bebidas = Bebidas.objects.all()
    context = {'bebidas':bebidas}
    return render(request, 'bebidas.html', context=context)

# def crear_bebida(request):
#     if request.method == "GET":
#         form = Bebidas_form()
#         context = {'form':form}
#         return render(request, 'crear_bebida.html', context=context)
#     else:
#         form = Bebidas_form(request.POST)
#         if form.is_valid():
#             nueva_bebida = Bebidas.objects.create(
#                 nombre = form.cleaned_data['nombre'],
#                 descripcion = form.cleaned_data['descripcion'],
#                 precio = form.cleaned_data['precio'],
#             )
#             context ={'nueva_bebida':nueva_bebida}
#     return render(request, 'crear_bebida.html', context=context)

def detalle_bebida(request, pk):
    try:
        bebida = Bebidas.objects.get(id=pk)
        context = {'bebida':bebida}
        return render(request, 'detalle_bebida.html', context=context)
    except:
        context = {'error': 'El producto no existe'}
        return render(request, 'bebidas.html', context=context)

def eliminar_bebida(request, pk):
    try:
        if request.method == 'GET':
            bebida = Bebidas.objects.get(id=pk)
            context = {'bebida':bebida}
        else:
            bebida = Bebidas.objects.get(id=pk)
            bebida.delete()
            context = {'message':'Producto eliminado correctamente'}
        return render(request, 'eliminar_bebida.html', context=context)
    except:
        context = {'error': 'El producto no existe'}
        return render(request, 'eliminar_bebida.html', context=context)

class Crear_bebida(LoginRequiredMixin, CreateView):
    model = Bebidas
    template_name = 'crear_bebida.html'
    fields ='__all__'

    def get_success_url(self):
        return reverse('detalle-bebida', kwargs={'pk':self.object.pk})

class Editar_bebida(LoginRequiredMixin, UpdateView):
    model = Bebidas
    template_name = 'editar_bebida.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('detalle-bebida', kwargs={'pk':self.object.pk})