from django.urls import path
from . import views

app_name = 'usuarios'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('minha-conta/', views.minha_conta, name='minha_conta'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('alterar-senha/', views.alterar_senha, name='alterar_senha'),
    path('minhas-compras/', views.minhas_compras, name='minhas_compras'),
    path('ajax/verificar-username/', views.verificar_username, name='verificar_username'),
    path('ajax/verificar-email/', views.verificar_email, name='verificar_email'),
]