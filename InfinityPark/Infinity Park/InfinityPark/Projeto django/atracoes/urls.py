from django.urls import path
from . import views

app_name = 'atracoes'

urlpatterns = [
    path('', views.home, name='home'),
    path('lista/', views.lista_atracoes, name='lista'),
    path('mapa/', views.mapa_parque, name='mapa'),
    path('favoritos/', views.meus_favoritos, name='favoritos'),
    path('<int:atracao_id>/', views.detalhe_atracao, name='detalhe'),
    path('<int:atracao_id>/favoritar/', views.toggle_favorito, name='favoritar'),
    path('<int:atracao_id>/avaliar/', views.avaliar_atracao, name='avaliar'),
    path('buscar/', views.buscar_atracoes, name='buscar'),
    path('api/wait-times/', views.api_tempos_espera, name='api_wait_times'),
]