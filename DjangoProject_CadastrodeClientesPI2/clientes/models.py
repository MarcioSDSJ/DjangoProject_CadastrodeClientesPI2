# clientes/models.py
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, unique=True)  # Formato: 000.000.000-00
    endereco = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)  # Exemplo: SP, RJ
    telefone = models.CharField(max_length=15)  # Formato: (XX) XXXXX-XXXX
    email = models.EmailField()
    produto = models.CharField(max_length=255)
    numero_pedido = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome
