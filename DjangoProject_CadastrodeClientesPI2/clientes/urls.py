# clientes/urls.py
from django.urls import path
from . import views  # Importa as views do aplicativo

urlpatterns = [
    path('login/', views.login_view, name='login'),              # Rota para login
    path('cadastro/', views.cadastro_cliente_view, name='cadastro_cliente'),  # Cadastro de clientes
    path('lista/', views.lista_clientes_view, name='lista_clientes'),         # Lista de clientes
    path('idex/', views.index, name='index'),  # Página inicial do app
]

# clientes/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Bem-vindo ao app Clientes!")
