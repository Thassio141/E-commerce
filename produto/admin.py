from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','nome_produto','slug','imagem','descricao','preco','qtd_produto')