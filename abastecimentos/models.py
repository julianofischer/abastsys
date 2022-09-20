from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False)


class Veiculo(models.Model):
    placa = models.CharField(max_length=7, null=False, blank=False)
    descricao = models.CharField(max_length=100, null=False, blank=False)
    capacidade_tanque = models.IntegerField(null=False)


class Bomba(models.Model):
    tipo_combustivel = models.CharField(max_length=100)
    qtdd_estoque = models.IntegerField()
    capacidade = models.IntegerField()


class Abastecimento(models.Model):
    data = models.DateField()
    qtdd_litr = models.IntegerField()
    km_odometro = models.IntegerField()
    functionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)


class CompraCombustivel(models.Model):
    data = models.DateField()
    qtdd_litros = models.IntegerField()
    preco_litro = models.DecimalField(max_digits=5, decimal_places=2)
