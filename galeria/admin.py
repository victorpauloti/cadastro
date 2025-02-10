from django.contrib import admin
from galeria.models import Fotografia


# personalisar admin galeria
class ListandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda",  "publicado", "data_fotografia")
    list_display_links = ("id", "nome") # hiperlink
    search_fields = ("nome",) # campo de busca
    list_filter = ("categoria",)
    list_editable = ("publicado",)
    list_per_page = 10

admin.site.register(Fotografia, ListandoFotografias)
