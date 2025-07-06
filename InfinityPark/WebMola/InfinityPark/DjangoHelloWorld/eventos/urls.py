from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.lista_eventos, name='lista'),
    path('<int:id>/', views.detalhe_evento, name='detalhe'),
    path('favoritos/', views.eventos_favoritos, name='favoritos'),
    path('calendario/', views.calendario_eventos, name='calendario'),
    path('buscar/', views.buscar_eventos, name='buscar'),
    path('avaliar/<int:id>/', views.avaliar_evento, name='avaliar'),
    path('favorito/<int:id>/', views.toggle_favorito, name='toggle_favorito'),
]