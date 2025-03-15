from django.db import models

from datetime import datetime

class Cadastro(models.Model):
    nome_marido = models.CharField(max_length=100)
    cpf_marido = models.CharField(max_length=15)  # O formato pode ser tratado diretamente no frontend 123.123.123-12
    dt_nasc_marido = models.CharField(max_length=10)
    nome_esposa = models.CharField(max_length=100)
    cpf_esposa = models.CharField(max_length=15)
    dt_nasc_esposa = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    celular = models.CharField(max_length=14)  # O formato pode ser tratado diretamente no frontend 19 91234-1234
    numero_parcelas = models.IntegerField()  # Este pode ter um valor de 1 a 7
    data_cadastro = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f'{self.nome_marido} e {self.nome_esposa}'

# verificar dados estao no javascritp
class Filho(models.Model):
    # Relaciona o filho ao cadastro que contém os dados do casal
    cadastro = models.ForeignKey(Cadastro, on_delete=models.CASCADE, related_name='filhos')  # Relaciona os filhos ao cadastro
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    cpf_marido = models.CharField(max_length=11)  # Campo para armazenar o CPF do marido

    def __str__(self):
            """
            Retorna uma representação legível do objeto Filho, incluindo o CPF do marido.
            Este método presume que o model Cadastro possua o atributo 'cpf_marido'.
            """
            return f'{self.nome}, {self.idade} anos (CPF marido: {self.cadastro.cpf_marido})'
    
    def save(self, *args, **kwargs):
        # Preenche o cpf_marido com o valor do cadastro relacionado
        if not self.cpf_marido:
            self.cpf_marido = self.cadastro.cpf_marido
        super().save(*args, **kwargs)


