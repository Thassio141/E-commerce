from django.db import models


class Produto(models.Model):
    nome_produto = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )

    imagem = models.ImageField(upload_to='media/%Y/%m/%d/')

    slug = models.SlugField(
        max_length = 255,
    )

    descricao = models.TextField(
        max_length=5000,
        null=False,
        blank=False
    )
    
    preco= models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )
    
    qtd_produto = models.IntegerField(
        default=0,
        null=False,
        blank=False,
    )


