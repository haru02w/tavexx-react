from django.db import models


# Create your models here.
class OperationModel(models.Model):
    class Meta:
        ordering = ["data"]

    class TypeChoices(models.TextChoices):
        DEPOSIT = "deposito"
        WITHDRAWAL = "saque"

    descricao = models.CharField(max_length=256)
    tag = models.CharField(max_length=64)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(choices=TypeChoices.choices, max_length=10)
    data = models.DateTimeField(auto_now=True)
