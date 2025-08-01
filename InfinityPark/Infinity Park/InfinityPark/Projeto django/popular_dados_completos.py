#!/usr/bin/env python
"""
Script para popular o banco de dados com dados completos do Infinity Park
Execute: python manage.py shell < popular_dados_completos.py
"""
import os
import sys
import django
from datetime import datetime, timedelta
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from django.contrib.auth.models import User
from django.utils import timezone
from eventos.models import CategoriaEvento, Evento
from ingressos.models import TipoIngresso, Promocao

def criar_categorias_eventos():
    """Criar categorias de eventos"""
    categorias = [
        {'nome': 'Shows Musicais', 'descricao': 'Apresentações musicais ao vivo', 'cor': '#ff6b6b', 'icone': 'fas fa-music'},
        {'nome': 'Espetáculos', 'descricao': 'Grandes espetáculos teatrais', 'cor': '#4ecdc4', 'icone': 'fas fa-theater-masks'},
        {'nome': 'Encontro com Personagens', 'descricao': 'Conheca seus personagens favoritos', 'cor': '#ffe66d', 'icone': 'fas fa-heart'},
        {'nome': 'Paradas', 'descricao': 'Desfiles e paradas temáticas', 'cor': '#ff8b94', 'icone': 'fas fa-star'},
        {'nome': 'Eventos Especiais', 'descricao': 'Celebrações e eventos sazonais', 'cor': '#95e1d3', 'icone': 'fas fa-calendar-star'},
    ]
    
    for cat_data in categorias:
        categoria, created = CategoriaEvento.objects.get_or_create(
            nome=cat_data['nome'],
            defaults=cat_data
        )
        if created:
            print(f"✓ Categoria criada: {categoria.nome}")

def criar_eventos_realistas():
    """Criar eventos realistas"""
    eventos_data = [
        {
            'nome': 'Festival de Luzes Mágicas',
            'descricao': 'Um espetáculo deslumbrante com milhares de luzes LED sincronizadas com música épica. Uma experiência única que transforma o parque em um mundo de fantasia.',
            'categoria': 'Espetáculos',
            'tipo': 'show',
            'faixa_etaria': 'familia',
            'local': 'Praça Central',
            'capacidade': 2000,
            'duracao_minutos': 45,
            'imagem_principal': 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800',
            'artistas': 'Orquestra Sinfônica, Grupo de Dança Contemporânea',
            'gratuito': True,
            'destaque': True,
        },
        {
            'nome': 'Rock in Park - Noite dos Heróis',
            'descricao': 'Show de rock com covers dos maiores sucessos dos filmes de super-heróis. Uma noite épica com efeitos especiais e surpresas.',
            'categoria': 'Shows Musicais',
            'tipo': 'show',
            'faixa_etaria': 'teen',
            'local': 'Anfiteatro Principal',
            'capacidade': 1500,
            'duracao_minutos': 90,
            'imagem_principal': 'https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800',
            'artistas': 'Banda Thunder Heroes, DJ Marvel',
            'gratuito': False,
            'preco': Decimal('25.00'),
        },
        {
            'nome': 'Encontro com Princesas Disney',
            'descricao': 'Conheca suas princesas favoritas: Elsa, Anna, Bela, Cinderela e muito mais! Sessão de fotos, autógrafos e histórias mágicas.',
            'categoria': 'Encontro com Personagens',
            'tipo': 'encontro',
            'faixa_etaria': 'infantil',
            'local': 'Castelo Encantado',
            'capacidade': 150,
            'duracao_minutos': 60,
            'imagem_principal': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800',
            'artistas': 'Princesas Disney Oficiais',
            'gratuito': True,
            'destaque': True,
        },
        {
            'nome': 'Parada dos Super-Heróis',
            'descricao': 'Uma parada espetacular com carros alegóricos gigantes dos super-heróis mais amados. Batman, Superman, Mulher Maravilha e muito mais!',
            'categoria': 'Paradas',
            'tipo': 'parada',
            'faixa_etaria': 'familia',
            'local': 'Avenida Principal',
            'capacidade': 5000,
            'duracao_minutos': 30,
            'imagem_principal': 'https://images.unsplash.com/photo-1635805737707-575885ab0820?w=800',
            'artistas': 'Super-Heróis da Marvel e DC',
            'gratuito': True,
        },
        {
            'nome': 'Halloween Horror Nights',
            'descricao': 'A noite mais assombrada do ano! Casas mal-assombradas, zumbis, e sustos em cada esquina. Apenas para os corajosos!',
            'categoria': 'Eventos Especiais',
            'tipo': 'especial',
            'faixa_etaria': 'adulto',
            'local': 'Todo o Parque',
            'capacidade': 3000,
            'duracao_minutos': 480,
            'imagem_principal': 'https://images.unsplash.com/photo-1509909756405-be0199881695?w=800',
            'artistas': 'Atores Profissionais de Terror',
            'gratuito': False,
            'preco': Decimal('80.00'),
            'destaque': True,
        },
        {
            'nome': 'Workshop de Mágica com Harry Potter',
            'descricao': 'Aprenda truques de mágica com os personagens do mundo mágico! Receba sua varinha e participe de aulas interativas.',
            'categoria': 'Eventos Especiais',
            'tipo': 'workshop',
            'faixa_etaria': 'familia',
            'local': 'Escola de Magia',
            'capacidade': 80,
            'duracao_minutos': 120,
            'imagem_principal': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800',
            'artistas': 'Magos Profissionais',
            'gratuito': False,
            'preco': Decimal('45.00'),
        },
        {
            'nome': 'Competição de Cosplay',
            'descricao': 'Mostre sua criatividade! Competição de fantasias com premiação para as melhores caracterizações de personagens.',
            'categoria': 'Eventos Especiais',
            'tipo': 'competicao',
            'faixa_etaria': 'teen',
            'local': 'Arena de Eventos',
            'capacidade': 500,
            'duracao_minutos': 180,
            'imagem_principal': 'https://images.unsplash.com/photo-1566041510394-cf7c8fe21800?w=800',
            'artistas': 'Jurados Especialistas em Cosplay',
            'gratuito': True,
        },
        {
            'nome': 'Festa de Ano Novo',
            'descricao': 'Celebre a virada do ano com fogos de artifício espetaculares, shows ao vivo e uma contagem regressiva inesquecível!',
            'categoria': 'Eventos Especiais',
            'tipo': 'especial',
            'faixa_etaria': 'familia',
            'local': 'Praça Central',
            'capacidade': 8000,
            'duracao_minutos': 360,
            'imagem_principal': 'https://images.unsplash.com/photo-1467810563316-b5476525c0f9?w=800',
            'artistas': 'Artistas Nacionais e Internacionais',
            'gratuito': False,
            'preco': Decimal('120.00'),
            'destaque': True,
        }
    ]
    
    now = timezone.now()
    
    for i, evento_data in enumerate(eventos_data):
        categoria = CategoriaEvento.objects.get(nome=evento_data['categoria'])
        
        # Criar datas futuras realistas
        dias_futuro = 7 + (i * 14)  # Eventos espaçados a cada 2 semanas
        data_inicio = now + timedelta(days=dias_futuro, hours=19)  # 19h
        data_fim = data_inicio + timedelta(minutes=evento_data['duracao_minutos'])
        
        evento, created = Evento.objects.get_or_create(
            nome=evento_data['nome'],
            defaults={
                **evento_data,
                'categoria': categoria,
                'data_inicio': data_inicio,
                'data_fim': data_fim,
                'galeria_imagens': f"{evento_data['imagem_principal']}, https://images.unsplash.com/photo-1540039155733-5bb30b53aa14?w=800, https://images.unsplash.com/photo-1493225457124-a3eb161ffa5f?w=800",
                'observacoes': 'Sujeito a alterações devido às condições climáticas.',
                'avaliacao_media': 4.2 + (i * 0.1),
                'total_avaliacoes': 50 + (i * 20)
            }
        )
        if created:
            print(f"✓ Evento criado: {evento.nome}")

def criar_tipos_ingressos():
    """Criar tipos de ingressos realistas"""
    tipos_data = [
        {
            'nome': 'Ingresso Básico',
            'descricao': 'Acesso a todas as atrações do parque durante um dia inteiro. Diversão garantida!',
            'preco': Decimal('89.90'),
            'cor': '#007bff',
            'icone': 'fas fa-ticket-alt',
            'validade_dias': 1,
            'idade_minima': 0,
        },
        {
            'nome': 'Ingresso Família (4 pessoas)',
            'descricao': 'Pacote especial para família com até 4 pessoas. Melhor custo-benefício!',
            'preco': Decimal('299.90'),
            'cor': '#28a745',
            'icone': 'fas fa-users',
            'validade_dias': 1,
            'idade_minima': 0,
            'desconto_restaurantes': 10,
        },
        {
            'nome': 'Fast Pass VIP',
            'descricao': 'Passe pela fila preferencial em todas as atrações + acesso VIP a eventos especiais.',
            'preco': Decimal('149.90'),
            'cor': '#ffc107',
            'icone': 'fas fa-crown',
            'acesso_fast_pass': True,
            'acesso_vip': True,
            'validade_dias': 1,
            'desconto_restaurantes': 20,
            'desconto_loja': 15,
        },
        {
            'nome': 'Passe Anual Premium',
            'descricao': 'Acesso ilimitado por 1 ano + estacionamento gratuito + descontos exclusivos.',
            'preco': Decimal('899.90'),
            'cor': '#dc3545',
            'icone': 'fas fa-infinity',
            'acesso_fast_pass': True,
            'acesso_vip': True,
            'estacionamento_gratuito': True,
            'validade_dias': 365,
            'desconto_restaurantes': 30,
            'desconto_loja': 25,
        },
        {
            'nome': 'Ingresso Infantil',
            'descricao': 'Especial para crianças de 3 a 12 anos. Inclui brinde exclusivo!',
            'preco': Decimal('59.90'),
            'cor': '#fd7e14',
            'icone': 'fas fa-child',
            'validade_dias': 1,
            'idade_minima': 3,
            'idade_maxima': 12,
        },
        {
            'nome': 'Ingresso Estudante',
            'descricao': 'Desconto especial para estudantes. Apresente sua carteirinha na entrada.',
            'preco': Decimal('69.90'),
            'cor': '#6610f2',
            'icone': 'fas fa-graduation-cap',
            'validade_dias': 1,
            'idade_minima': 12,
        },
        {
            'nome': '2 Dias Consecutivos',
            'descricao': 'Aproveite o parque por dois dias seguidos. Mais tempo para curtir tudo!',
            'preco': Decimal('159.90'),
            'cor': '#20c997',
            'icone': 'fas fa-calendar-day',
            'validade_dias': 2,
            'desconto_restaurantes': 5,
        }
    ]
    
    for tipo_data in tipos_data:
        tipo, created = TipoIngresso.objects.get_or_create(
            nome=tipo_data['nome'],
            defaults=tipo_data
        )
        if created:
            print(f"✓ Tipo de ingresso criado: {tipo.nome}")

def criar_promocoes():
    """Criar promoções realistas"""
    now = timezone.now()
    
    promocoes_data = [
        {
            'nome': 'Black Friday 2024',
            'descricao': 'Desconto imperdível de Black Friday! Válido apenas hoje!',
            'codigo': 'BLACKFRIDAY50',
            'tipo_desconto': 'percentual',
            'valor_desconto': Decimal('50.00'),
            'data_inicio': now - timedelta(days=1),
            'data_fim': now + timedelta(days=30),
            'uso_maximo': 1,
            'quantidade_maxima': 1000,
            'valor_minimo': Decimal('100.00'),
        },
        {
            'nome': 'Desconto Família',
            'descricao': 'R$ 30 OFF para compras em família!',
            'codigo': 'FAMILIA30',
            'tipo_desconto': 'valor_fixo',
            'valor_desconto': Decimal('30.00'),
            'data_inicio': now,
            'data_fim': now + timedelta(days=60),
            'uso_maximo': 2,
            'valor_minimo': Decimal('200.00'),
        },
        {
            'nome': 'Primeira Visita',
            'descricao': '20% OFF para quem visita pela primeira vez!',
            'codigo': 'PRIMEIRAVISITA',
            'tipo_desconto': 'percentual',
            'valor_desconto': Decimal('20.00'),
            'data_inicio': now,
            'data_fim': now + timedelta(days=90),
            'uso_maximo': 1,
            'valor_minimo': Decimal('50.00'),
        },
        {
            'nome': 'Aniversário do Parque',
            'descricao': 'Celebre conosco! 25% OFF em todos os ingressos!',
            'codigo': 'ANIVERSARIO25',
            'tipo_desconto': 'percentual',
            'valor_desconto': Decimal('25.00'),
            'data_inicio': now + timedelta(days=30),
            'data_fim': now + timedelta(days=37),
            'uso_maximo': 1,
            'quantidade_maxima': 500,
        }
    ]
    
    for promo_data in promocoes_data:
        promocao, created = Promocao.objects.get_or_create(
            codigo=promo_data['codigo'],
            defaults=promo_data
        )
        if created:
            print(f"✓ Promoção criada: {promocao.nome}")

def main():
    """Executar população completa do banco"""
    print("🎢 Populando banco de dados do Infinity Park...")
    print("=" * 50)
    
    try:
        # Eventos
        print("\n📅 Criando categorias de eventos...")
        criar_categorias_eventos()
        
        print("\n🎭 Criando eventos...")
        criar_eventos_realistas()
        
        # Ingressos
        print("\n🎫 Criando tipos de ingressos...")
        criar_tipos_ingressos()
        
        print("\n🏷️ Criando promoções...")
        criar_promocoes()
        
        print("\n" + "=" * 50)
        print("✅ Banco de dados populado com sucesso!")
        print("\n📊 Resumo:")
        print(f"   • {CategoriaEvento.objects.count()} categorias de eventos")
        print(f"   • {Evento.objects.count()} eventos")
        print(f"   • {TipoIngresso.objects.count()} tipos de ingressos")
        print(f"   • {Promocao.objects.count()} promoções")
        
    except Exception as e:
        print(f"❌ Erro ao popular banco: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()