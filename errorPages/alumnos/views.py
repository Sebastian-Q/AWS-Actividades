from .models import Alumno
from .serializers import AlumnoSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from .form import alumnoForm
from django.shortcuts import render

class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    renderer_classes = [JSONRenderer]
    #http_method_names = ['get', 'post', 'put', 'delete']


def crud(request):
    form = alumnoForm()
    return render(request, 'quintero_sebastian.html', {'form': form})