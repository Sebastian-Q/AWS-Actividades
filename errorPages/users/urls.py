from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

router = SimpleRouter()
#router.register('users', UserViewSet)

router.register(r'api', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #Esta es la ruta de iniciar sesion
    path('token/', CustomTokenObtainPairView.as_view(), name='obtain_pair'),
    path('token/refresh', TokenObtainPairView.as_view, name='refresh_token'),
]