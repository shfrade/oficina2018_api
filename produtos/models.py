from django.db import models


# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=120)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)
