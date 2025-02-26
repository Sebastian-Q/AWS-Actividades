from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import AlumnoViewSet, crud

router = SimpleRouter()
router.register(r'api', AlumnoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('crud/', crud, name='crud_alumnos'),
]