from django.contrib import admin
from galeria.models import Fotografia
#from usuarios.models import Cadastro


# personalisar admin galeria
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda",  "publicado", "data_fotografia")
    list_display_links = ("id", "nome") # hiperlink
    search_fields = ("nome",) # campo de busca
    list_filter = ("categoria",)
    list_editable = ("publicado",)
    list_per_page = 10

# class ListandoCadastros(admin.ModelAdmin):
#     list_display = ("nome_marido", "nome_esposa", "email", "celular", "numero_parcelas", "data_cadastro")

admin.site.register(Fotografia, ListandoFotografias)
#admin.site.register(Cadastro, ListandoCadastros)
