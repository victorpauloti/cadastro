from django.contrib import admin
from usuarios.models import Cadastro, Filho
# Register your models here.


class ListandoCadastros(admin.ModelAdmin):
    list_display = ("nome_marido", "cpf_marido", "dt_nasc_marido", "nome_esposa","cpf_esposa", "dt_nasc_esposa", "email", "celular", "numero_parcelas", "data_cadastro")

admin.site.register(Cadastro, ListandoCadastros)

class ListandoFilhos(admin.ModelAdmin):
    list_display = ("nome", "idade")

admin.site.register(Filho, ListandoFilhos)