from django.urls import path
from . import views

app_name = 'ingressos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('comprar/', views.comprar, name='comprar'),
    path('meus-ingressos/', views.meus_ingressos, name='meus_ingressos'),
    path('validar/<str:codigo>/', views.validar, name='validar'),
    path('categoria/<int:categoria_id>/', views.lista_por_categoria, name='categoria'),
]