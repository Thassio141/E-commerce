from .models import Produto
from django import forms

class AdicionarProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome_produto','slug','imagem','descricao','preco','qtd_produto']
