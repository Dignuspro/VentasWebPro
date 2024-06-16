from django.shortcuts import render, redirect
from .forms import VentaForm
from .models import Venta

def index(request):
    ventas = Venta.objects.filter(usuario=request.user).order_by('-fecha')
    return render(request, 'ventasapp/index.html', {'ventas': ventas})

def add_venta(request):
    if request.method == 'POST':
        form = VentaForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.usuario = request.user
            venta.save()
            return redirect('index')
    else:
        form = VentaForm()
    return render(request, 'ventasapp/add_venta.html', {'form': form})
