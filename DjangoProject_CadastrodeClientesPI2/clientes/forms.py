# clientes/forms.py
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nome', 'cpf', 'endereco', 'numero', 'bairro', 'cidade',
            'estado', 'telefone', 'email', 'produto', 'numero_pedido'
        ]
