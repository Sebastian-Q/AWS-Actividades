from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse

def agregarCategoria(request):
    if request.method == 'POST':
        forms = categoriaForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('consultar')
    else:
        forms = categoriaForm()
    return render(request, 'registrar.html', {'form':forms})

def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias':categorias})

def lista_categorias(request):
    categorias = Categoria.objects.all()
    data = [
        {
            'nombre': c.nombre,
            'imagen': c.imagen
        }
        for c in categorias
    ]
    return JsonResponse(data, safe=False)

def json_view(request):
    return render(request, 'jsonCategoria.html')