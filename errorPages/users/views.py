#API REST CON DjangoRESTFRAMEWORK

from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from django.contrib.auth.models import User
from .forms import CustomUserCreationForm as CustomUserForm
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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



class CustomUserFormAPI(APIView):
    def get(self, request, *args, **kwargs):
        form = CustomUserForm()
        fields = [
            {
                'name': field,  # Se agrega 'name' para identificarlo en el frontend
                'label': form[field].label,
                'input': form[field].field.widget.attrs,
                'type': form[field].field.widget.input_type,
            }
            for field in form.fields
        ]
        return Response(fields)
    
    def post(self, request, *args, **kwargs):
        print('request.data: ', request.data)
        form = CustomUserForm(request.data)
        if form.is_valid():
            user_data = form.cleaned_data
            print('user_data: ', user_data)
            User = get_user_model()
            user = User.objects.create_user(
                email=user_data['email'],
                password=user_data['password1'], #Establecer la contraseña
                name=user_data['name'],
                surname=user_data['surname'],
                control_number=user_data['control_number'],
                age=user_data['age'],
                tel=user_data['tel'],
            )
            return Response({'message': 'Usuario creado con éxito'},status=status.HTTP_201_CREATED)
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
