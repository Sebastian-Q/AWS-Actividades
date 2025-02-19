from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Categoria
from .forms import categoriaForm
from django.http import JsonResponse
import json

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

#@crsf_exempt <-- No es seguro hacer esto (no lo hagas) solo pa pruebas
def registrar_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nueva_categoria = Categoria.objects.create(
                nombre = data['nombre'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje':'Registrado exitoso',
                'id': nueva_categoria.id
            }, status=201
            )
        except Exception as e:
            return JsonResponse({
                'error': str(e)
            }, status=400)
    return JsonResponse({
        'error': 'Método no es POST'
    }, status=405
    )