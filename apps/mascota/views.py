from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.mascota.forms import MascotaForm

# Create your views here.

def index(request):
    #return HttpResponse('Index mascota')
    return render(request, 'mascota/Mascota.html')


def mascota_view(request):
    if request.method == 'POST':
        form = MascotaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form=MascotaForm()       
    return render(request, 'mascota/mascota_form.html',{'form':form})
