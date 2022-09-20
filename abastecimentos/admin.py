from django.contrib import admin
from abastecimentos.models import (
    Funcionario,
    Veiculo,
    Bomba,
    Abastecimento,
    CompraCombustivel,
)

# Register your models here.
admin.site.register(Funcionario)
admin.site.register(Veiculo)
admin.site.register(Bomba)
admin.site.register(Abastecimento)
admin.site.register(CompraCombustivel)
