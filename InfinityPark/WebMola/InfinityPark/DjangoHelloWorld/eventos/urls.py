from django.urls import path
from . import views

app_name = 'eventos'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('<int:evento_id>/', views.detalhe, name='detalhe'),
    path('categoria/<int:categoria_id>/', views.lista_por_categoria, name='categoria'),
    path('hoje/', views.eventos_hoje, name='hoje'),
    path('calendario/', views.calendario, name='calendario'),
]