from django.urls import path
from . import views

app_name = 'restaurantes'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:restaurante_id>/', views.detalhe, name='detalhe'),
    path('categoria/<int:categoria_id>/', views.lista_por_categoria, name='categoria'),
    path('area/<int:area_id>/', views.lista_por_area, name='area'),
    path('cardapio/<int:restaurante_id>/', views.cardapio, name='cardapio'),
]