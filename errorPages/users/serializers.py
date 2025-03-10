from rest_framework_simplejwt.serializers import TokenObtainPairSerializer;
from rest_framework import serializers;
from .models import CustomUser;

class CustomTokenPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        #Agregar más atributos
        return token    
    
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__' #['email', 'password']
        