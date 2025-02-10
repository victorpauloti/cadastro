from django.shortcuts import render
from galeria.models import Fotografia
from django.shortcuts import get_object_or_404

# Nesse arquivo é onde inserimos toda lógica relacionada às rotas

def index(request):
    fotografias = Fotografia.objects.order_by("-data_fotografia").filter(publicado=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})


