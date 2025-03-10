#API REST CON DjangoRESTFRAMEWORK

from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    renderer_classes = [JSONRenderer]
    #http_method_names = ['GET', 'POST']

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    #Sobreescribir el método para la obteción de permisos
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'DELETE']:
            #Retornar la función que checa si tenemos sesión
            return [IsAuthenticated()]
        #Dar acceso al otro método (GET)
        return []

#Clase adiccional para obtener el par de tokens
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenPairSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenPairSerializer