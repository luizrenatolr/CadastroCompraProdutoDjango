from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Produto(models.Model):
    #Como dois produtos não podem ter o mesmo nome, nome é chave primária de produto.
    nome = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.nome

class Compra(models.Model):
    #Compra tem como chave estrangeira a chave primária do produto relacionado.
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(null=False, default=1, validators=[MinValueValidator(1)])
    preco_de_compra = models.FloatField(null=False, default=0.01, validators=[MinValueValidator(0.01)])
    preco_medio = models.FloatField(null=False)

    #Método save calcula automaticamente preço médio em uma compra
    #além de salvar no Banco de Dados.
    def save(self, *args, **kwargs):
        #Preço médio é o preço total da compra dividio pela quantidade do produto comprado.
        self.preco_medio = self.preco_de_compra/self.quantidade
        super(Compra, self).save(*args , **kwargs)