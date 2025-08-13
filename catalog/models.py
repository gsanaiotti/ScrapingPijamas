from django.db import models

class Product(models.Model):
    nome_loja = models.CharField(max_length=30)
    nome_produto = models.CharField(max_length=100)
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)
    url_produto = models.URLField()
    url_foto = models.URLField()
    status_ativo = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome_produto} - {self.nome_loja}"