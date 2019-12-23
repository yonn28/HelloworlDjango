from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.forms import MascotaForm
from django.db import models
from .models import Mascota
from  django.views.generic import ListView, CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

def index(request):
    #return HttpResponse('Index mascota')
    return render(request, 'mascota/Mascota.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar') ## no se puede colocar el prefijo porque no lo toma, faltaba el App name!!!
    else:
        form=MascotaForm()       
    return render(request, 'mascota/mascota_form.html',{'form':form})

def mascota_list(request):
    mascota=Mascota.objects.all()
    contexto = {'mascotas':mascota}
    return render(request, 'mascota/mascota_list.html',contexto)

def mascota_edit(request, pk):
    mascota=Mascota.objects.get(id=pk)
    if request.method == 'GET':
        form=MascotaForm(instance=mascota)
    else:
        form=MascotaForm(request.POST,instance=mascota)
        if form.is_valid():
            form.save()
        return redirect('mascota:mascota_listar')
    return render(request,'mascota/mascota_form.html',{'form':form})

def mascota_delete(request, pk):
    mascota=Mascota.objects.get(id=pk)
    if request.method == 'POST':
        mascota.delete()
        return redirect('mascota:mascota_listar')
    return render(request,'mascota/mascota_delete.html',{'mascota':mascota})

class MascotaList(ListView):
    model=Mascota
    template_name='mascota/mascota_list.html'

class MascotaCreate(CreateView):
    model=Mascota
    form_class=MascotaForm
    template_name='mascota/mascota_form.html'
    success_url=reverse_lazy('mascota:mascota_listar')

class MascotaUpdate(UpdateView):
    model=Mascota
    form_class=MascotaForm
    template_name='mascota/mascota_form.html'
    success_url=reverse_lazy('mascota:mascota_listar')
 
class MascotaDelete(DeleteView):
    model=Mascota
    template_name='mascota/mascota_delete.html'
    success_url=reverse_lazy('mascota:mascota_listar')