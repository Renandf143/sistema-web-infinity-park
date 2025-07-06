from django.urls import path
from . import views

app_name = 'servicos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:servico_id>/', views.detalhe, name='detalhe'),
    path('categoria/<int:categoria_id>/', views.lista_por_categoria, name='categoria'),
    path('mapa/', views.mapa_servicos, name='mapa'),
]