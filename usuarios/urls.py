from django.urls import path
from usuarios.views import login, cadastro

# criar uma lista para manter as urls da app os path vem das views.py do app
urlpatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro')
]