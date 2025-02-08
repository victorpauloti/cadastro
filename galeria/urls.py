from django.urls import path
from galeria.views import index, imagem

# criar uma lista para manter as urls da app galeria
urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem')
]