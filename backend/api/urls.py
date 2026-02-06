from django.urls import path
from .views import *

urlpatterns = [
    path('usuarios', listar_usuarios),
    path('users', UsuarioView.as_view()),
    path('usuario/<int:pk>', UsuarioDetailView.as_view()),

    path('Imoveis', ImovelView.as_view()),
    path('Imovel/<int:pk>', ImovelDetailView.as_view()),

    path('Contratos', ContratoView.as_view()),
    path('Contrato/<int:pk>', ContratoDetailView.as_view()),

    path('Pagamentos', PagamentoView.as_view()),
    path('Pagamento/<int:pk>', PagamentoDetailView.as_view())

]