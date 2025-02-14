from django.db import models

from datetime import datetime

## Classe que representa uma tabela no banco de dados
class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ("PISCINA", "Piscina"),
        ("ACOMODAÇÕES", "Acomodações"),
        ("LAZER", "Laser"),
        ("GASTRONOMIA", "Gastronomia")
        ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default="")
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"