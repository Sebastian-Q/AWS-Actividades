from django.shortcuts import render, redirect
from .models import Producto
from .forms import productoForm
from django.http import JsonResponse
import json

# Agregar un producto
def agregarProducto(request):
    #Primero checamos como llegamos a esta función
    if request.method == 'POST':
        #LLegamos aqui por el envio de esta funcion
        forms = productoForm(request.POST) #Esto genera un formulario llena con inormación
        if forms.is_valid():
            forms.save()
            return redirect('ver') #Esto redirige a la lista de productos
    else:
        forms = productoForm() #Esto genera un formulario vacio
    return render(request, 'agregar.html', {'form':forms})

#Ver los productos
def ver_productos(request):
    productos = Producto.objects.all()
    return render(request, 'ver.html', {'productos':productos})

#Devuelve en JSON
def lista_productos(request):
    productos = Producto.objects.all()
    #Para enviar un JSON debemos escribir los datos
    #Es un diccionario usando llaves

    data = [
        {
            'nombre': p.nombre,
            'precio': p.precio,
            'imagen': p.imagen
        }
        for p in productos
    ]
    return JsonResponse(data, safe=False)

def json_view(request):
    return render(request, 'json.html')

#@crsf_exempt <-- No es seguro hacer esto (no lo hagas) solo pa pruebas
def registrar_producto(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nuevo_producto = Producto.objects.create(
                nombre = data['nombre'],
                precio = data['precio'],
                imagen = data['imagen']
            )
            return JsonResponse({
                'mensaje':'Registrado exitoso',
                'id': nuevo_producto.id
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