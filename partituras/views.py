from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Partitura
from .forms import PartituraForm

@login_required
def menu(request):
    """
    Vista para mostrar el menu de partituras.
    """
    partituras = Partitura.objects.filter(usuario=request.user)
    return render(request, 'menu.html', {'partituras': partituras})

def catalogo(request):
    """
    Vista para mostrar el catálogo de partituras del usuario.
    """
    partituras = Partitura.objects.filter(usuario=request.user)
    return render(request, 'catalogo.html', {'partituras': partituras})

@login_required
def subir_partitura(request):
    """
    Vista para subir una nueva partitura.
    """
    if request.method == 'POST':
        form = PartituraForm(request.POST, request.FILES)
        if form.is_valid():
            partitura = form.save(commit=False)
            partitura.usuario = request.user  # Asignar el usuario autenticado
            partitura.save()
            return redirect('catalogo')  # Redirigir al catálogo
    else:
        form = PartituraForm()
    
    return render(request, 'subir_partitura.html', {'form': form})

@login_required
def actualizar_partitura(request, partitura_id):
    """
    Vista para actualizar una partitura existente.
    """
    partitura = get_object_or_404(Partitura, pk=partitura_id, usuario=request.user)
    if request.method == 'POST':
        form = PartituraForm(request.POST, request.FILES, instance=partitura)
        if form.is_valid():
            form.save()
            return redirect('catalogo')  # Redirigir al catálogo
    else:
        form = PartituraForm(instance=partitura)
    
    return render(request, 'actualizar_partitura.html', {'form': form, 'partitura': partitura})

@login_required
def eliminar_partitura(request, partitura_id):
    """
    Vista para eliminar una partitura.
    """
    partitura = get_object_or_404(Partitura, pk=partitura_id, usuario=request.user)
    if request.method == 'POST':
        partitura.delete()
        return redirect('catalogo')  # Redirigir al catálogo
    return render(request, 'eliminar_partitura.html', {'partitura': partitura})

@login_required
def visualizar_partitura(request, partitura_id):
    """
    Vista para visualizar los detalles de una partitura.
    """
    partitura = get_object_or_404(Partitura, pk=partitura_id, usuario=request.user)
    return render(request, 'visualizar_partitura.html', {'partitura': partitura})