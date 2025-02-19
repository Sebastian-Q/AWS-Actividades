from django.urls import path
from .views import *

urlpatterns = [
    path('consultar/', ver_categorias, name='consultar'),
    path('registrar/', agregarCategoria, name='registrar'),
    path('api/get/', lista_categorias, name='lista'),
    path('json/', json_view, name='json'),
    path('api/post/', registrar_categoria, name='post'),
]