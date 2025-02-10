from django.contrib import admin
from django.urls import path, include

# indicar as urls.py das apps criadas
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('', include('usuarios.urls')),
]
