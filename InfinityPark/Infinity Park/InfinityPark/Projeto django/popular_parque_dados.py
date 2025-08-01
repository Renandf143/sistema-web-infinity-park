#!/usr/bin/env python3
"""
Script para popular o banco de dados do Infinity Park com dados reais de parque de diversões
"""

import os
import sys
import django
from datetime import time, datetime

# Configurar Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from atracoes.models import (
    CategoriaAtracao, AreaParque, Atracao, ServicoParque, 
    AvaliacaoAtracao, FavoritoUsuario, TempoEspera
)
from django.contrib.auth.models import User

def criar_categorias():
    # categorias que pensei pro parque
    categorias = [
        {
            'nome': 'Montanha-Russa',
            'descricao': 'Emoção e adrenalina em alta velocidade com loops e quedas',
            'tipo': 'montanha_russa',
            'icone': 'zap',
            'cor': '#DC2626'
        },
        {
            'nome': 'Aventura Aquática',
            'descricao': 'Diversão refrescante com água e descidas molhadas',
            'tipo': 'aquatica',
            'icone': 'waves',
            'cor': '#2563EB'
        },
        {
            'nome': 'Família',
            'descricao': 'Diversão para toda a família, crianças e adultos',
            'tipo': 'familia',
            'icone': 'users',
            'cor': '#16A34A'
        },
        {
            'nome': 'Radical',
            'descricao': 'Para os mais corajosos e aventureiros',
            'tipo': 'radical',
            'icone': 'flame',
            'cor': '#EA580C'
        },
        {
            'nome': 'Infantil',
            'descricao': 'Perfeito para crianças pequenas',
            'tipo': 'infantil',
            'icone': 'baby',
            'cor': '#7C3AED'
        },
        {
            'nome': 'Simulador',
            'descricao': 'Experiências imersivas com tecnologia avançada',
            'tipo': 'simulador',
            'icone': 'gamepad-2',
            'cor': '#059669'
        },
        {
            'nome': 'Show',
            'descricao': 'Espetáculos e apresentações ao vivo',
            'tipo': 'show',
            'icone': 'music',
            'cor': '#DB2777'
        }
    ]
    
    for cat_data in categorias:
        categoria, created = CategoriaAtracao.objects.get_or_create(
            nome=cat_data['nome'],
            defaults=cat_data
        )
        if created:
            print(f"✓ Categoria criada: {categoria.nome}")

def criar_areas():
    """Criar áreas temáticas do parque"""
    areas = [
        {
            'nome': 'Adventureland',
            'descricao': 'Uma terra de aventuras exóticas e mistérios antigos, onde cada esquina esconde uma nova descoberta',
            'tema': 'adventureland',
            'imagem': 'https://images.unsplash.com/photo-1544474333-d2833eb5b8cc?w=800',
            'coordenadas_mapa': {'x': 100, 'y': 150, 'width': 300, 'height': 200},
            'cor': '#8B4513'
        },
        {
            'nome': 'Fantasyland',
            'descricao': 'O reino mágico dos contos de fadas, onde os sonhos se tornam realidade',
            'tema': 'fantasyland',
            'imagem': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800',
            'coordenadas_mapa': {'x': 450, 'y': 100, 'width': 350, 'height': 250},
            'cor': '#9370DB'
        },
        {
            'nome': 'Tomorrowland',
            'descricao': 'O futuro está aqui com tecnologia e inovação de ponta',
            'tema': 'tomorrowland',
            'imagem': 'https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800',
            'coordenadas_mapa': {'x': 200, 'y': 400, 'width': 300, 'height': 200},
            'cor': '#4169E1'
        },
        {
            'nome': 'Frontierland',
            'descricao': 'O selvagem oeste americano ganha vida com aventuras do velho oeste',
            'tema': 'frontierland',
            'imagem': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
            'coordenadas_mapa': {'x': 550, 'y': 400, 'width': 250, 'height': 200},
            'cor': '#D2691E'
        },
        {
            'nome': 'Main Street',
            'descricao': 'A charmosa rua principal que te transporta para o início do século XX',
            'tema': 'main_street',
            'imagem': 'https://images.unsplash.com/photo-1568127856048-b6de45b15f93?w=800',
            'coordenadas_mapa': {'x': 300, 'y': 50, 'width': 200, 'height': 100},
            'cor': '#CD853F'
        }
    ]
    
    for area_data in areas:
        area, created = AreaParque.objects.get_or_create(
            nome=area_data['nome'],
            defaults=area_data
        )
        if created:
            print(f"✓ Área criada: {area.nome}")

def criar_atracoes():
    """Criar atrações do parque com dados realistas"""
    
    # Obter referências das categorias e áreas
    cat_montanha = CategoriaAtracao.objects.get(tipo='montanha_russa')
    cat_aquatica = CategoriaAtracao.objects.get(tipo='aquatica')
    cat_familia = CategoriaAtracao.objects.get(tipo='familia')
    cat_radical = CategoriaAtracao.objects.get(tipo='radical')
    cat_infantil = CategoriaAtracao.objects.get(tipo='infantil')
    cat_simulador = CategoriaAtracao.objects.get(tipo='simulador')
    cat_show = CategoriaAtracao.objects.get(tipo='show')
    
    area_adventure = AreaParque.objects.get(tema='adventureland')
    area_fantasy = AreaParque.objects.get(tema='fantasyland')
    area_tomorrow = AreaParque.objects.get(tema='tomorrowland')
    area_frontier = AreaParque.objects.get(tema='frontierland')
    area_main = AreaParque.objects.get(tema='main_street')
    
    atracoes = [
        # ADVENTURELAND
        {
            'nome': 'Pirates of the Caribbean',
            'descricao': 'Navegue pelos mares perigosos e descubra tesouros escondidos nesta aventura épica pelos sete mares. Enfrente piratas, tempestades e criaturas marinhas misteriosas em uma jornada inesquecível.',
            'descricao_curta': 'Aventura naval épica com piratas e tesouros escondidos',
            'categoria': cat_familia,
            'area': area_adventure,
            'imagem_principal': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800',
                'https://images.unsplash.com/photo-1520637836862-4d197d17c27a?w=800',
                'https://images.unsplash.com/photo-1544474333-d2833eb5b8cc?w=800'
            ],
            'coordenadas_mapa': {'x': 150, 'y': 180},
            'altura_minima': 100,
            'duracao': 8,
            'capacidade': 24,
            'nivel_emocao': 2,
            'tempo_espera': 35,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': True,
            'acesso_deficiente_auditivo': True,
            'avaliacao': 4.8,
            'numero_avaliacoes': 2847,
            'horario_abertura': time(9, 0),
            'horario_fechamento': time(22, 0)
        },
        {
            'nome': 'Jungle Cruise',
            'descricao': 'Uma jornada hilária pelos rios mais perigosos do mundo com nossos guias especializados em piadas ruins e aventuras incríveis. Prepare-se para muitas risadas!',
            'descricao_curta': 'Cruzeiro cômico pela selva selvagem',
            'categoria': cat_familia,
            'area': area_adventure,
            'imagem_principal': 'https://images.unsplash.com/photo-1566073771259-6a8506099945?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1544474333-d2833eb5b8cc?w=800',
                'https://images.unsplash.com/photo-1520637836862-4d197d17c27a?w=800'
            ],
            'coordenadas_mapa': {'x': 200, 'y': 220},
            'altura_minima': 80,
            'duracao': 10,
            'capacidade': 32,
            'nivel_emocao': 1,
            'tempo_espera': 25,
            'fast_pass_disponivel': False,
            'acessivel_cadeirante': True,
            'acesso_deficiente_auditivo': True,
            'acesso_deficiente_visual': True,
            'avaliacao': 4.5,
            'numero_avaliacoes': 1923,
            'horario_abertura': time(9, 0),
            'horario_fechamento': time(22, 0)
        },
        {
            'nome': 'Splash Mountain',
            'descricao': 'Prepare-se para se molhar! Uma descida emocionante de 20 metros em uma aventura aquática inesquecível com direito a fotos no final da grande queda.',
            'descricao_curta': 'Descida aquática radical de 20 metros',
            'categoria': cat_aquatica,
            'area': area_adventure,
            'imagem_principal': 'https://images.unsplash.com/photo-1558618047-3c8c76ca7d13?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1575550959106-5a7defe28b56?w=800',
                'https://images.unsplash.com/photo-1544474333-d2833eb5b8cc?w=800'
            ],
            'coordenadas_mapa': {'x': 350, 'y': 280},
            'altura_minima': 120,
            'duracao': 5,
            'capacidade': 8,
            'nivel_emocao': 4,
            'tempo_espera': 55,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': False,
            'acesso_deficiente_auditivo': True,
            'avaliacao': 4.8,
            'numero_avaliacoes': 3785,
            'horario_abertura': time(10, 0),
            'horario_fechamento': time(21, 0)
        },
        
        # FANTASYLAND
        {
            'nome': 'Space Mountain',
            'descricao': 'Voe através das galáxias em completa escuridão nesta montanha-russa espacial única. Uma experiência inesquecível nas estrelas com efeitos especiais incríveis!',
            'descricao_curta': 'Montanha-russa espacial no escuro total',
            'categoria': cat_montanha,
            'area': area_fantasy,
            'imagem_principal': 'https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800',
                'https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800'
            ],
            'coordenadas_mapa': {'x': 500, 'y': 150},
            'altura_minima': 120,
            'duracao': 3,
            'capacidade': 12,
            'nivel_emocao': 4,
            'tempo_espera': 65,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': False,
            'acesso_deficiente_auditivo': True,
            'avaliacao': 4.9,
            'numero_avaliacoes': 4521,
            'horario_abertura': time(9, 0),
            'horario_fechamento': time(23, 0)
        },
        {
            'nome': 'Castelo da Princesa',
            'descricao': 'Explore o majestoso castelo e conheça suas princesas favoritas em um passeio mágico através dos contos de fadas mais amados de todos os tempos.',
            'descricao_curta': 'Tour mágico pelo castelo encantado',
            'categoria': cat_infantil,
            'area': area_fantasy,
            'imagem_principal': 'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1571003123394-b7dde9b8f395?w=800',
                'https://images.unsplash.com/photo-1518611012118-696072aa579a?w=800'
            ],
            'coordenadas_mapa': {'x': 600, 'y': 200},
            'altura_minima': 0,
            'duracao': 12,
            'capacidade': 20,
            'nivel_emocao': 1,
            'tempo_espera': 40,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': True,
            'acesso_deficiente_auditivo': True,
            'acesso_deficiente_visual': True,
            'avaliacao': 4.7,
            'numero_avaliacoes': 3264,
            'horario_abertura': time(9, 0),
            'horario_fechamento': time(22, 0)
        },
        {
            'nome': 'Carrousel Mágico',
            'descricao': 'Um carrossel clássico com cavalos mágicos que sobem e descem ao som de músicas encantadoras. Perfeito para toda a família criar memórias especiais!',
            'descricao_curta': 'Carrossel clássico familiar encantado',
            'categoria': cat_infantil,
            'area': area_fantasy,
            'imagem_principal': 'https://images.unsplash.com/photo-1453614946848-5aa2c4537d7c?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1460904577954-8fadb262612c?w=800',
                'https://images.unsplash.com/photo-1453614946848-5aa2c4537d7c?w=800'
            ],
            'coordenadas_mapa': {'x': 550, 'y': 180},
            'altura_minima': 0,
            'duracao': 3,
            'capacidade': 40,
            'nivel_emocao': 1,
            'tempo_espera': 15,
            'fast_pass_disponivel': False,
            'acessivel_cadeirante': True,
            'acesso_deficiente_auditivo': True,
            'acesso_deficiente_visual': True,
            'avaliacao': 4.3,
            'numero_avaliacoes': 1856,
            'horario_abertura': time(9, 0),
            'horario_fechamento': time(22, 0)
        },
        
        # TOMORROWLAND
        {
            'nome': 'Hyperspace Mountain',
            'descricao': 'Uma experiência de realidade virtual revolucionária que te transporta para outros planetas em uma jornada intergaláctica emocionante com tecnologia de ponta.',
            'descricao_curta': 'Aventura VR intergaláctica futurística',
            'categoria': cat_simulador,
            'area': area_tomorrow,
            'imagem_principal': 'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800',
                'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800'
            ],
            'coordenadas_mapa': {'x': 300, 'y': 450},
            'altura_minima': 130,
            'duracao': 4,
            'capacidade': 16,
            'nivel_emocao': 5,
            'tempo_espera': 85,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': False,
            'acesso_deficiente_auditivo': False,
            'avaliacao': 4.9,
            'numero_avaliacoes': 5847,
            'horario_abertura': time(10, 0),
            'horario_fechamento': time(23, 0)
        },
        {
            'nome': 'Buzz Lightyear Laser Blast',
            'descricao': 'Junte-se ao Buzz Lightyear nesta missão interativa para derrotar o Imperador Zurg! Use seus lasers para marcar pontos e salvar o universo.',
            'descricao_curta': 'Aventura interativa com lasers espaciais',
            'categoria': cat_simulador,
            'area': area_tomorrow,
            'imagem_principal': 'https://images.unsplash.com/photo-1562113530-57ba23cea03c?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=800'
            ],
            'coordenadas_mapa': {'x': 250, 'y': 500},
            'altura_minima': 90,
            'duracao': 6,
            'capacidade': 24,
            'nivel_emocao': 2,
            'tempo_espera': 30,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': True,
            'acesso_deficiente_auditivo': True,
            'avaliacao': 4.4,
            'numero_avaliacoes': 2156,
            'horario_abertura': time(9, 0),
            'horario_fechamento': time(22, 0)
        },
        
        # FRONTIERLAND
        {
            'nome': 'Thunder Mountain Railroad',
            'descricao': 'Viaje de trem pelas montanhas do velho oeste em uma aventura cheia de surpresas, cavernas misteriosas e paisagens deslumbrantes do far west.',
            'descricao_curta': 'Trem da montanha do velho oeste',
            'categoria': cat_montanha,
            'area': area_frontier,
            'imagem_principal': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1552074284-5e88ef1aef18?w=800',
                'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800'
            ],
            'coordenadas_mapa': {'x': 650, 'y': 480},
            'altura_minima': 110,
            'duracao': 6,
            'capacidade': 32,
            'nivel_emocao': 3,
            'tempo_espera': 45,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': False,
            'acesso_deficiente_auditivo': True,
            'avaliacao': 4.6,
            'numero_avaliacoes': 2946,
            'horario_abertura': time(9, 0),
            'horario_fechamento': time(22, 0)
        },
        {
            'nome': 'Wild West Shootout',
            'descricao': 'Teste sua pontaria no maior duelo do oeste! Uma experiência interativa onde você pode se tornar o xerife mais rápido da cidade.',
            'descricao_curta': 'Duelo interativo do velho oeste',
            'categoria': cat_familia,
            'area': area_frontier,
            'imagem_principal': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1552074284-5e88ef1aef18?w=800'
            ],
            'coordenadas_mapa': {'x': 700, 'y': 520},
            'altura_minima': 100,
            'duracao': 8,
            'capacidade': 16,
            'nivel_emocao': 2,
            'tempo_espera': 20,
            'fast_pass_disponivel': False,
            'acessivel_cadeirante': True,
            'acesso_deficiente_auditivo': True,
            'avaliacao': 4.2,
            'numero_avaliacoes': 1456,
            'horario_abertura': time(10, 0),
            'horario_fechamento': time(21, 0)
        },
        
        # ATRAÇÕES EXTREMAS
        {
            'nome': 'Dragon\'s Fury',
            'descricao': 'A montanha-russa mais radical do parque! Com 5 loops, queda livre de 30 metros e velocidade de 120 km/h. Só para os mais corajosos!',
            'descricao_curta': 'Montanha-russa extrema com 5 loops',
            'categoria': cat_radical,
            'area': area_fantasy,
            'imagem_principal': 'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=800',
                'https://images.unsplash.com/photo-1449824913935-59a10b8d2000?w=800'
            ],
            'coordenadas_mapa': {'x': 480, 'y': 120},
            'altura_minima': 140,
            'altura_maxima': 195,
            'duracao': 3,
            'capacidade': 24,
            'nivel_emocao': 5,
            'tempo_espera': 75,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': False,
            'avaliacao': 4.8,
            'numero_avaliacoes': 3254,
            'horario_abertura': time(10, 0),
            'horario_fechamento': time(22, 0)
        },
        {
            'nome': 'Tower of Terror',
            'descricao': 'Suba 60 metros de altura e experimente a queda livre mais aterrorizante do mundo! Uma experiência que desafia a gravidade.',
            'descricao_curta': 'Queda livre de 60 metros de altura',
            'categoria': cat_radical,
            'area': area_tomorrow,
            'imagem_principal': 'https://images.unsplash.com/photo-1520637836862-4d197d17c27a?w=800',
            'galeria_imagens': [
                'https://images.unsplash.com/photo-1520637836862-4d197d17c27a?w=800'
            ],
            'coordenadas_mapa': {'x': 320, 'y': 480},
            'altura_minima': 130,
            'duracao': 2,
            'capacidade': 16,
            'nivel_emocao': 5,
            'tempo_espera': 90,
            'fast_pass_disponivel': True,
            'acessivel_cadeirante': False,
            'avaliacao': 4.7,
            'numero_avaliacoes': 4123,
            'horario_abertura': time(11, 0),
            'horario_fechamento': time(22, 0)
        }
    ]
    
    for atracao_data in atracoes:
        atracao, created = Atracao.objects.get_or_create(
            nome=atracao_data['nome'],
            defaults=atracao_data
        )
        if created:
            print(f"✓ Atração criada: {atracao.nome}")

def criar_servicos():
    """Criar serviços do parque"""
    
    areas = {
        'adventureland': AreaParque.objects.get(tema='adventureland'),
        'fantasyland': AreaParque.objects.get(tema='fantasyland'),
        'tomorrowland': AreaParque.objects.get(tema='tomorrowland'),
        'frontierland': AreaParque.objects.get(tema='frontierland'),
        'main_street': AreaParque.objects.get(tema='main_street')
    }
    
    servicos = [
        # BANHEIROS
        {
            'nome': 'Banheiros Adventureland',
            'tipo': 'banheiro',
            'area': areas['adventureland'],
            'coordenadas_mapa': {'x': 130, 'y': 280},
            'icone': 'restroom',
            'descricao': 'Banheiros familiares com fraldário'
        },
        {
            'nome': 'Banheiros Fantasyland',
            'tipo': 'banheiro',
            'area': areas['fantasyland'],
            'coordenadas_mapa': {'x': 520, 'y': 280},
            'icone': 'restroom',
            'descricao': 'Banheiros temáticos com decoração de princesas'
        },
        {
            'nome': 'Banheiros Tomorrowland',
            'tipo': 'banheiro',
            'area': areas['tomorrowland'],
            'coordenadas_mapa': {'x': 280, 'y': 520},
            'icone': 'restroom',
            'descricao': 'Banheiros futuristas com tecnologia touchless'
        },
        
        # PRIMEIROS SOCORROS
        {
            'nome': 'Primeiros Socorros Central',
            'tipo': 'primeiros_socorros',
            'area': areas['fantasyland'],
            'coordenadas_mapa': {'x': 500, 'y': 300},
            'icone': 'heart-pulse',
            'descricao': 'Posto médico principal com enfermeiros 24h'
        },
        {
            'nome': 'Posto de Primeiros Socorros',
            'tipo': 'primeiros_socorros',
            'area': areas['adventureland'],
            'coordenadas_mapa': {'x': 180, 'y': 320},
            'icone': 'heart-pulse',
            'descricao': 'Atendimento básico de primeiros socorros'
        },
        
        # CAIXAS ELETRÔNICOS
        {
            'nome': 'Caixa Eletrônico Tomorrowland',
            'tipo': 'caixa_eletronico',
            'area': areas['tomorrowland'],
            'coordenadas_mapa': {'x': 250, 'y': 480},
            'icone': 'credit-card',
            'descricao': 'ATM 24h com múltiplas redes'
        },
        {
            'nome': 'Caixa Eletrônico Main Street',
            'tipo': 'caixa_eletronico',
            'area': areas['main_street'],
            'coordenadas_mapa': {'x': 400, 'y': 80},
            'icone': 'credit-card',
            'descricao': 'Caixa eletrônico na entrada principal'
        },
        
        # LOJAS DE SOUVENIRS
        {
            'nome': 'Loja de Souvenirs Fantasyland',
            'tipo': 'loja_souvenir',
            'area': areas['fantasyland'],
            'coordenadas_mapa': {'x': 620, 'y': 280},
            'icone': 'gift',
            'descricao': 'Souvenirs mágicos e produtos das princesas'
        },
        {
            'nome': 'Pirates Treasure Shop',
            'tipo': 'loja_souvenir',
            'area': areas['adventureland'],
            'coordenadas_mapa': {'x': 160, 'y': 250},
            'icone': 'gift',
            'descricao': 'Tesouros piratas e souvenirs de aventura'
        },
        {
            'nome': 'Future World Store',
            'tipo': 'loja_souvenir',
            'area': areas['tomorrowland'],
            'coordenadas_mapa': {'x': 270, 'y': 470},
            'icone': 'gift',
            'descricao': 'Gadgets futuristas e souvenirs tecnológicos'
        },
        
        # PONTOS FOTOGRÁFICOS
        {
            'nome': 'Ponto Fotográfico Castelo',
            'tipo': 'ponto_fotografico',
            'area': areas['fantasyland'],
            'coordenadas_mapa': {'x': 600, 'y': 200},
            'icone': 'camera',
            'descricao': 'Local perfeito para fotos com o castelo'
        },
        {
            'nome': 'Photo Spot Pirates',
            'tipo': 'ponto_fotografico',
            'area': areas['adventureland'],
            'coordenadas_mapa': {'x': 200, 'y': 200},
            'icone': 'camera',
            'descricao': 'Cenário pirata para fotos incríveis'
        },
        
        # INFORMAÇÕES
        {
            'nome': 'Central de Informações',
            'tipo': 'informacoes',
            'area': areas['main_street'],
            'coordenadas_mapa': {'x': 380, 'y': 100},
            'icone': 'info',
            'descricao': 'Informações gerais e mapas do parque'
        },
        
        # ALUGUEL DE CARRINHO
        {
            'nome': 'Aluguel de Carrinho Infantil',
            'tipo': 'aluguel_carrinho',
            'area': areas['main_street'],
            'coordenadas_mapa': {'x': 350, 'y': 90},
            'icone': 'baby-carriage',
            'descricao': 'Carrinhos e cadeiras de rodas para aluguel'
        }
    ]
    
    for servico_data in servicos:
        servico, created = ServicoParque.objects.get_or_create(
            nome=servico_data['nome'],
            defaults=servico_data
        )
        if created:
            print(f"✓ Serviço criado: {servico.nome}")

def criar_usuario_admin():
    """Criar usuário administrador"""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@infinitypark.com',
            password='admin123',
            first_name='Administrador',
            last_name='Infinity Park'
        )
        print("✓ Usuário admin criado (username: admin, password: admin123)")

def criar_usuarios_teste():
    """Criar alguns usuários de teste"""
    usuarios = [
        {
            'username': 'joao_silva',
            'email': 'joao@email.com',
            'first_name': 'João',
            'last_name': 'Silva',
            'password': 'teste123'
        },
        {
            'username': 'maria_santos',
            'email': 'maria@email.com',
            'first_name': 'Maria',
            'last_name': 'Santos',
            'password': 'teste123'
        },
        {
            'username': 'pedro_oliveira',
            'email': 'pedro@email.com',
            'first_name': 'Pedro',
            'last_name': 'Oliveira',
            'password': 'teste123'
        }
    ]
    
    for user_data in usuarios:
        if not User.objects.filter(username=user_data['username']).exists():
            User.objects.create_user(**user_data)
            print(f"✓ Usuário criado: {user_data['username']}")

def criar_avaliacoes_exemplo():
    # algumas avaliações mais realistas
    usuarios = User.objects.exclude(username='admin')
    atracoes = Atracao.objects.all()
    
    avaliacoes = [
        {'atracao': 'Pirates of the Caribbean', 'nota': 5, 'comentario': 'Cara, que atração incrível! Parece que você tá realmente no filme. Meu filho de 8 anos ficou vidrado.'},
        {'atracao': 'Space Mountain', 'nota': 4, 'comentario': 'Muito boa, mas a fila tava gigante. Vale a pena pegar o fast pass.'},
        {'atracao': 'Splash Mountain', 'nota': 5, 'comentario': 'Melhor atração aquática do parque! Saí encharcado mas feliz haha'},
        {'atracao': 'Dragon\'s Fury', 'nota': 3, 'comentario': 'Muito radical pra mim... quase vomitei nos loops. Mas quem curte adrenalina vai amar.'},
        {'atracao': 'Castelo da Princesa', 'nota': 5, 'comentario': 'As crianças amaram! Tiramos mil fotos. Só achei meio caro as lembrancinhas.'},
        {'atracao': 'Thunder Mountain Railroad', 'nota': 4, 'comentario': 'Legal, mas esperava mais emoção. É mais pra família mesmo.'},
        {'atracao': 'Tower of Terror', 'nota': 5, 'comentario': 'MANO QUE SUSTO! Não consegui nem gritar direito. 10/10'},
        {'atracao': 'Jungle Cruise', 'nota': 2, 'comentario': 'Meio parado... as piadas são bem ruins mesmo. Só fui porque tava com tempo.'},
    ]
    
    for i, aval_data in enumerate(avaliacoes):
        if usuarios.exists():
            try:
                atracao = atracoes.get(nome=aval_data['atracao'])
                usuario = usuarios[i % len(usuarios)]
                
                avaliacao, created = AvaliacaoAtracao.objects.get_or_create(
                    usuario=usuario,
                    atracao=atracao,
                    defaults={
                        'nota': aval_data['nota'],
                        'comentario': aval_data['comentario']
                    }
                )
                if created:
                    print(f"✓ Avaliação criada: {usuario.username} -> {atracao.nome}")
            except Atracao.DoesNotExist:
                continue

def atualizar_avaliacoes_atracoes():
    """Atualizar as médias de avaliação das atrações"""
    from django.db.models import Avg
    
    for atracao in Atracao.objects.all():
        avaliacoes = AvaliacaoAtracao.objects.filter(atracao=atracao)
        if avaliacoes.exists():
            media = avaliacoes.aggregate(media=Avg('nota'))['media']
            atracao.avaliacao = round(media, 1)
            atracao.numero_avaliacoes = avaliacoes.count()
            atracao.save(update_fields=['avaliacao', 'numero_avaliacoes'])

def main():
    # roda tudo pra popular o banco com dados legais
    print("🎢 Criando dados do Infinity Park...")
    print("=" * 50)
    
    try:
        # Limpar dados existentes (opcional)
        print("🗑️ Limpando dados existentes...")
        AvaliacaoAtracao.objects.all().delete()
        FavoritoUsuario.objects.all().delete()
        TempoEspera.objects.all().delete()
        ServicoParque.objects.all().delete()
        Atracao.objects.all().delete()
        AreaParque.objects.all().delete()
        CategoriaAtracao.objects.all().delete()
        User.objects.filter(is_superuser=False).delete()
        
        print("\n📋 Criando categorias...")
        criar_categorias()
        
        print("\n🗺️ Criando áreas do parque...")
        criar_areas()
        
        print("\n🎢 Criando atrações...")
        criar_atracoes()
        
        print("\n🏪 Criando serviços...")
        criar_servicos()
        
        print("\n👤 Criando usuários...")
        criar_usuario_admin()
        criar_usuarios_teste()
        
        print("\n⭐ Criando avaliações...")
        criar_avaliacoes_exemplo()
        
        print("\n📊 Atualizando estatísticas...")
        atualizar_avaliacoes_atracoes()
        
        print("\n" + "=" * 60)
        print("✅ Banco de dados populado com sucesso!")
        print("\n📋 Resumo:")
        print(f"   • {CategoriaAtracao.objects.count()} categorias")
        print(f"   • {AreaParque.objects.count()} áreas")
        print(f"   • {Atracao.objects.count()} atrações")
        print(f"   • {ServicoParque.objects.count()} serviços")
        print(f"   • {User.objects.count()} usuários")
        print(f"   • {AvaliacaoAtracao.objects.count()} avaliações")
        
        print("\n🔑 Credenciais de acesso:")
        print("   Admin: username=admin, password=admin123")
        print("   Usuários teste: username=joao_silva, password=teste123")
        
        print("\n🚀 Pronto! Você pode iniciar o servidor Django agora.")
        
    except Exception as e:
        print(f"❌ Erro durante a população: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    main()