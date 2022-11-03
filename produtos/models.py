from django.db import models

# Create your models here.
class Produtos(models.Model):
    
    titulo = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    img = models.ImageField()
    valor = models.DecimalField(decimal_places=2, max_digits= 6)
    descricao = models.TextField(max_length=5000)