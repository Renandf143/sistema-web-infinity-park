from django.urls import path
from . import views

app_name = 'ingressos'

urlpatterns = [
    path('', views.lista_ingressos, name='lista'),
    path('<int:id>/', views.detalhe_ingresso, name='detalhe'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('checkout/', views.checkout, name='checkout'),
    path('meus-ingressos/', views.meus_ingressos, name='meus_ingressos'),
    path('compra-sucesso/<str:codigo>/', views.compra_sucesso, name='compra_sucesso'),
    
    # AJAX endpoints
    path('ajax/adicionar-carrinho/', views.adicionar_carrinho, name='adicionar_carrinho'),
    path('ajax/remover-carrinho/', views.remover_carrinho, name='remover_carrinho'),
    path('ajax/aplicar-promocao/', views.aplicar_promocao, name='aplicar_promocao'),
    path('ajax/verificar-promocao/', views.verificar_promocao, name='verificar_promocao'),
]