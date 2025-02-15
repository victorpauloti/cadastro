from django.db import models

from datetime import datetime

class Cadastro(models.Model):
    nome_marido = models.CharField(max_length=100)
    nome_esposa = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    celular = models.CharField(max_length=14)  # O formato pode ser tratado diretamente no frontend
    numero_parcelas = models.IntegerField()  # Este pode ter um valor de 1 a 7
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'{self.nome_marido} e {self.nome_esposa}'

# verificar dados estao no javascritp
class Filho(models.Model):
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='filhos')  # Relaciona os filhos ao cadastro
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()

    def __str__(self):
        return f'{self.nome}, {self.idade} anos'


