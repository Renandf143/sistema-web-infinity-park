
#!/usr/bin/env python3
"""
Script para configurar e executar o Infinity Park completo
"""

import os
import sys
import subprocess
import django
from django.conf import settings
from django.core.management import execute_from_command_line

def setup_django():
    """Configurar Django"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
    django.setup()

def criar_superuser():
    """Criar superusuário admin"""
    from django.contrib.auth.models import User
    
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@infinitypark.com', 'admin123')
        print("✅ Superusuário 'admin' criado com sucesso!")
    else:
        print("✅ Superusuário 'admin' já existe")

def popular_dados_completos():
    """Popular banco com dados completos do Infinity Park"""
    from django.core.management import call_command
    from atracoes.models import *
    
    print("📊 Populando dados do Infinity Park...")
    
    # Criar categorias
    categorias = [
        {'nome': 'Montanha-Russa', 'descricao': 'Aventuras radicais em alta velocidade', 'cor': '#FF6B6B'},
        {'nome': 'Aquática', 'descricao': 'Diversão refrescante com água', 'cor': '#4ECDC4'},
        {'nome': 'Família', 'descricao': 'Diversão para toda a família', 'cor': '#45B7D1'},
        {'nome': 'Radical', 'descricao': 'Para os mais corajosos', 'cor': '#FF8C42'},
        {'nome': 'Infantil', 'descricao': 'Especiais para crianças', 'cor': '#FFD93D'},
        {'nome': 'Simulador', 'descricao': 'Experiências imersivas', 'cor': '#A8E6CF'},
        {'nome': 'Show', 'descricao': 'Espetáculos e apresentações', 'cor': '#DDA0DD'},
    ]
    
    for cat_data in categorias:
        categoria, created = CategoriaAtracao.objects.get_or_create(
            nome=cat_data['nome'],
            defaults=cat_data
        )
    
    # Criar áreas
    areas = [
        {'nome': 'Adventureland', 'descricao': 'Terra da aventura e exploração', 'imagem': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'},
        {'nome': 'Fantasyland', 'descricao': 'O mundo mágico dos contos de fadas', 'imagem': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'},
        {'nome': 'Tomorrowland', 'descricao': 'O futuro está aqui', 'imagem': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'},
        {'nome': 'Frontierland', 'descricao': 'A fronteira do velho oeste', 'imagem': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'},
        {'nome': 'Main Street', 'descricao': 'A rua principal do parque', 'imagem': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'},
    ]
    
    for area_data in areas:
        area, created = AreaParque.objects.get_or_create(
            nome=area_data['nome'],
            defaults=area_data
        )
    
    # Criar atrações
    atracoes_data = [
        {
            'nome': 'Thunder Mountain',
            'descricao': 'Uma montanha-russa emocionante através de uma mina abandonada',
            'categoria': 'Montanha-Russa',
            'area': 'Frontierland',
            'altura_minima': 120,
            'duracao': 180,
            'nivel_emocao': 4,
            'imagem_principal': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'
        },
        {
            'nome': 'Pirates of the Caribbean',
            'descricao': 'Aventure-se no mundo dos piratas do Caribe',
            'categoria': 'Família',
            'area': 'Adventureland',
            'altura_minima': 0,
            'duracao': 420,
            'nivel_emocao': 2,
            'imagem_principal': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'
        },
        {
            'nome': 'Space Mountain',
            'descricao': 'Uma jornada espacial no escuro',
            'categoria': 'Montanha-Russa',
            'area': 'Tomorrowland',
            'altura_minima': 110,
            'duracao': 150,
            'nivel_emocao': 4,
            'imagem_principal': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'
        },
        {
            'nome': 'Splash Mountain',
            'descricao': 'Descida radical com muito splash!',
            'categoria': 'Aquática',
            'area': 'Frontierland',
            'altura_minima': 100,
            'duracao': 600,
            'nivel_emocao': 3,
            'imagem_principal': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'
        },
        {
            'nome': 'Haunted Mansion',
            'descricao': 'Uma mansão assombrada cheia de fantasmas',
            'categoria': 'Família',
            'area': 'Fantasyland',
            'altura_minima': 0,
            'duracao': 480,
            'nivel_emocao': 2,
            'imagem_principal': 'https://images.unsplash.com/photo-1544984243-ec57ea16fe25?w=800'
        },
    ]
    
    for atracao_data in atracoes_data:
        categoria = CategoriaAtracao.objects.get(nome=atracao_data['categoria'])
        area = AreaParque.objects.get(nome=atracao_data['area'])
        
        atracao, created = Atracao.objects.get_or_create(
            nome=atracao_data['nome'],
            defaults={
                'descricao': atracao_data['descricao'],
                'categoria': categoria,
                'area': area,
                'altura_minima': atracao_data['altura_minima'],
                'duracao': atracao_data['duracao'],
                'nivel_emocao': atracao_data['nivel_emocao'],
                'imagem_principal': atracao_data['imagem_principal'],
                'ativo': True,
                'tempo_espera': 15,
                'avaliacao': 4.5,
                'numero_avaliacoes': 1250,
                'acessivel_cadeirante': True,
                'fast_pass_disponivel': True,
            }
        )
    
    print("✅ Dados do Infinity Park populados com sucesso!")

def main():
    print("\n🎢 CONFIGURANDO INFINITY PARK COMPLETO 🎢")
    print("=" * 50)
    
    # Mudar para o diretório correto
    os.chdir('/home/runner/BookingClone/InfinityPark/WebMola/InfinityPark/DjangoHelloWorld')
    
    # Configurar Django
    setup_django()
    
    # Fazer migrações
    print("🔧 Executando migrações...")
    execute_from_command_line(['manage.py', 'makemigrations'])
    execute_from_command_line(['manage.py', 'migrate'])
    
    # Criar superusuário
    criar_superuser()
    
    # Popular dados
    popular_dados_completos()
    
    # Coletar arquivos estáticos
    print("📁 Coletando arquivos estáticos...")
    execute_from_command_line(['manage.py', 'collectstatic', '--noinput'])
    
    print("\n🚀 INFINITY PARK CONFIGURADO COM SUCESSO!")
    print("=" * 50)
    print("🌐 Acesse: http://localhost:5000")
    print("👤 Admin: http://localhost:5000/admin/ (admin/admin123)")
    print("=" * 50)
    
    # Iniciar servidor
    print("🚀 Iniciando servidor...")
    execute_from_command_line(['manage.py', 'runserver', '0.0.0.0:5000'])

if __name__ == '__main__':
    main()
