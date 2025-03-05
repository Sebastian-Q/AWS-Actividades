from .models import Producto
from .serializers import ProductoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer

from .forms import productoForm
from django.shortcuts import render

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    renderer_classes = [JSONRenderer]

def agregar_producto(request):
    form = productoForm()
    return render(request, 'agregar.html', {'form': form})

def prueba_view(request):
    return render(request, 'prueba.html')