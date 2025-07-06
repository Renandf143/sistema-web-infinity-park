from django.urls import path
from . import views

app_name = 'hoteis'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:hotel_id>/', views.detalhe, name='detalhe'),
    path('categoria/<int:categoria_id>/', views.lista_por_categoria, name='categoria'),
    path('reservas/', views.reservas, name='reservas'),
    path('reservar/<int:hotel_id>/', views.reservar, name='reservar'),
]