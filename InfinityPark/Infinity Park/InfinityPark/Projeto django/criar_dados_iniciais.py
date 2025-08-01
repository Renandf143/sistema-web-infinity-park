#!/usr/bin/env python
"""
Script para criar dados iniciais para o Infinity Park
Execute: python manage.py shell < criar_dados_iniciais.py
"""

import os
import django
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from urllib.request import urlretrieve

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infinity_park.settings')
django.setup()

from atracoes.models import CategoriaAtracao, Atracao
from restaurantes.models import Restaurante

def criar_categorias():
    """Criar categorias de atrações"""
    categorias = [
        {'nome': 'Atrações Radicais', 'tipo': 'radical', 'descricao': 'Para os aventureiros em busca de adrenalina'},
        {'nome': 'Diversão Familiar', 'tipo': 'familiar', 'descricao': 'Atrações para toda a família se divertir'},
        {'nome': 'Para Crianças', 'tipo': 'infantil', 'descricao': 'Especialmente para os pequenos exploradores'},
        {'nome': 'Shows e Espetáculos', 'tipo': 'show', 'descricao': 'Apresentações e espetáculos únicos'},
        {'nome': 'Experiências Aquáticas', 'tipo': 'animal', 'descricao': 'Diversão refrescante com água'},
    ]
    
    for cat_data in categorias:
        categoria, created = CategoriaAtracao.objects.get_or_create(
            tipo=cat_data['tipo'],
            defaults=cat_data
        )
        if created:
            print(f"Categoria criada: {categoria.nome}")

def criar_atracoes():
    """Criar atrações reais do parque"""
    
    # Pegar as categorias
    radical = CategoriaAtracao.objects.get(tipo='radical')
    familiar = CategoriaAtracao.objects.get(tipo='familiar')
    infantil = CategoriaAtracao.objects.get(tipo='infantil')
    show = CategoriaAtracao.objects.get(tipo='show')
    aquatico = CategoriaAtracao.objects.get(tipo='animal')
    
    atracoes_data = [
        # Atrações Radicais
        {
            'nome': 'Infinity Coaster',
            'descricao': 'A montanha-russa mais radical do parque! Com loops invertidos, quedas de 60 metros e velocidade de até 120 km/h. Uma experiência que vai acelerar seu coração e te dar a sensação de voar.',
            'categoria': radical,
            'altura_minima': 140,
            'idade_minima': 12,
            'duracao': 3,
            'capacidade': 24,
            'nivel_emocao': 5,
            'tempo_fila_medio': 45,
            'regras': 'Não é recomendado para pessoas com problemas cardíacos, de coluna ou mulheres grávidas. Altura mínima: 1,40m.'
        },
        {
            'nome': 'Torre do Terror',
            'descricao': 'Uma queda livre de 80 metros de altura! Suba até o topo e sinta a adrenalina da queda livre em velocidade máxima. Uma das atrações mais assustadoras do parque.',
            'categoria': radical,
            'altura_minima': 130,
            'idade_minima': 10,
            'duracao': 2,
            'capacidade': 16,
            'nivel_emocao': 5,
            'tempo_fila_medio': 35,
            'regras': 'Altura mínima: 1,30m. Não recomendado para pessoas com medo de altura.'
        },
        {
            'nome': 'Twister',
            'descricao': 'Montanha-russa com giros e loops emocionantes. Prepare-se para ser virado de cabeça para baixo várias vezes nesta aventura cheia de adrenalina.',
            'categoria': radical,
            'altura_minima': 135,
            'idade_minima': 11,
            'duracao': 4,
            'capacidade': 20,
            'nivel_emocao': 4,
            'tempo_fila_medio': 40,
            'regras': 'Altura mínima: 1,35m. Retire objetos soltos antes do passeio.'
        },
        
        # Atrações Familiares
        {
            'nome': 'Roda Gigante Infinity',
            'descricao': 'Uma roda gigante de 50 metros de altura com vista panorâmica de todo o parque e da região. Perfeita para contemplar a paisagem e relaxar com a família.',
            'categoria': familiar,
            'altura_minima': None,
            'idade_minima': None,
            'duracao': 12,
            'capacidade': 48,
            'nivel_emocao': 1,
            'tempo_fila_medio': 20,
            'regras': 'Crianças menores de 8 anos devem estar acompanhadas de um adulto.'
        },
        {
            'nome': 'Carrossel Mágico',
            'descricao': 'Um carrossel clássico com cavalos pintados à mão e música encantadora. Uma atração tradicional que encanta crianças e desperta nostalgia nos adultos.',
            'categoria': familiar,
            'altura_minima': None,
            'idade_minima': None,
            'duracao': 5,
            'capacidade': 32,
            'nivel_emocao': 1,
            'tempo_fila_medio': 15,
            'regras': 'Crianças até 5 anos devem estar acompanhadas.'
        },
        {
            'nome': 'Trem Fantasma',
            'descricao': 'Uma jornada assombrada através de cenários misteriosos e sustos divertidos. Uma aventura emocionante, mas adequada para toda a família.',
            'categoria': familiar,
            'altura_minima': 100,
            'idade_minima': 6,
            'duracao': 8,
            'capacidade': 16,
            'nivel_emocao': 2,
            'tempo_fila_medio': 25,
            'regras': 'Altura mínima: 1,00m. Crianças até 8 anos devem estar acompanhadas.'
        },
        {
            'nome': 'Barcos do Piratas',
            'descricao': 'Navegue em uma aventura pirata cheia de surpresas, tesouros escondidos e batalhas navais. Uma atração aquática divertida para toda a família.',
            'categoria': familiar,
            'altura_minima': 110,
            'idade_minima': 5,
            'duracao': 10,
            'capacidade': 20,
            'nivel_emocao': 2,
            'tempo_fila_medio': 30,
            'regras': 'Altura mínima: 1,10m. Prepare-se para se molhar um pouco!'
        },
        
        # Atrações Infantis
        {
            'nome': 'Aviõezinhos',
            'descricao': 'Voe pelos céus em aviões coloridos que sobem e descem suavemente. Uma aventura aérea segura e divertida para os pequenos pilotos.',
            'categoria': infantil,
            'altura_minima': 90,
            'idade_minima': 3,
            'duracao': 4,
            'capacidade': 16,
            'nivel_emocao': 1,
            'tempo_fila_medio': 15,
            'regras': 'Altura mínima: 90cm. Crianças até 6 anos devem estar acompanhadas.'
        },
        {
            'nome': 'Carrinhos Bate-Bate',
            'descricao': 'Dirija seu próprio carrinho e divirta-se batendo nos amigos e família. Uma atração clássica que nunca sai de moda e diverte todas as idades.',
            'categoria': infantil,
            'altura_minima': 110,
            'idade_minima': 4,
            'duracao': 5,
            'capacidade': 20,
            'nivel_emocao': 1,
            'tempo_fila_medio': 20,
            'regras': 'Altura mínima: 1,10m para dirigir sozinho. Menores podem ir acompanhados.'
        },
        {
            'nome': 'Mini Montanha-Russa',
            'descricao': 'Uma montanha-russa especialmente projetada para crianças, com curvas suaves e velocidade moderada. A introdução perfeita ao mundo das montanhas-russas.',
            'categoria': infantil,
            'altura_minima': 100,
            'idade_minima': 5,
            'duracao': 3,
            'capacidade': 12,
            'nivel_emocao': 2,
            'tempo_fila_medio': 25,
            'regras': 'Altura mínima: 1,00m. Primeira montanha-russa dos pequenos!'
        },
        
        # Shows
        {
            'nome': 'O Sonho do Cowboy',
            'descricao': 'Um espetáculo emocionante que celebra a vida no campo, com música country, dança e acrobacias que transportam você para o coração do oeste americano.',
            'categoria': show,
            'altura_minima': None,
            'idade_minima': None,
            'duracao': 45,
            'capacidade': 300,
            'nivel_emocao': 1,
            'tempo_fila_medio': 10,
            'regras': 'Show ao vivo com horários específicos. Consulte a programação.'
        },
        {
            'nome': 'Madagascar Circus Show',
            'descricao': 'Os personagens queridos de Madagascar em um circo repleto de alegria, mágica e diversão para toda a família, com Alex, Marty, Gloria e Melman.',
            'categoria': show,
            'altura_minima': None,
            'idade_minima': None,
            'duracao': 35,
            'capacidade': 250,
            'nivel_emocao': 1,
            'tempo_fila_medio': 15,
            'regras': 'Espetáculo familiar. Chegue com 15 minutos de antecedência.'
        },
    ]
    
    for atracao_data in atracoes_data:
        atracao, created = Atracao.objects.get_or_create(
            nome=atracao_data['nome'],
            defaults=atracao_data
        )
        if created:
            print(f"Atração criada: {atracao.nome}")

def criar_restaurantes():
    """Criar restaurantes do parque"""
    
    restaurantes_data = [
        {
            'nome': 'Restaurante Infinity Grill',
            'descricao': 'Nosso restaurante principal oferece uma variedade de pratos deliciosos, desde carnes grelhadas até opções vegetarianas. Ambiente familiar com vista para o parque.',
            'categoria': 'restaurante',
            'horario_funcionamento': 'Seg-Dom: 11:00 às 22:00',
            'telefone': '(11) 1234-5678',
            'capacidade': 120,
            'preco_medio': 45.00,
            'aceita_reserva': True,
        },
        {
            'nome': 'Lanchonete do Cowboy',
            'descricao': 'Lanches rápidos e saborosos no tema do oeste americano. Hambúrguers artesanais, batatas fritas crocantes e milk-shakes cremosos.',
            'categoria': 'lanchonete',
            'horario_funcionamento': 'Seg-Dom: 10:00 às 20:00',
            'telefone': '(11) 1234-5679',
            'capacidade': 60,
            'preco_medio': 25.00,
            'aceita_reserva': False,
        },
        {
            'nome': 'Pizzaria Mama Mia',
            'descricao': 'Pizzas tradicionais italianas feitas no forno à lenha, com ingredientes frescos e selecionados. Ambiente aconchegante para toda a família.',
            'categoria': 'pizzaria',
            'horario_funcionamento': 'Ter-Dom: 18:00 às 23:00',
            'telefone': '(11) 1234-5680',
            'capacidade': 80,
            'preco_medio': 35.00,
            'aceita_reserva': True,
        },
        {
            'nome': 'Sorveteria Gelato Paradise',
            'descricao': 'Sorvetes artesanais, gelatos italianos e sobremesas geladas. Perfeito para refrescar nos dias quentes e adoçar sua visita ao parque.',
            'categoria': 'sorveteria',
            'horario_funcionamento': 'Seg-Dom: 9:00 às 21:00',
            'telefone': '(11) 1234-5681',
            'capacidade': 40,
            'preco_medio': 15.00,
            'aceita_reserva': False,
        },
        {
            'nome': 'Cafeteria Central',
            'descricao': 'Cafés especiais, chás, bolos caseiros e salgados. O local perfeito para uma pausa relaxante durante sua aventura no parque.',
            'categoria': 'cafeteria',
            'horario_funcionamento': 'Seg-Dom: 7:00 às 19:00',
            'telefone': '(11) 1234-5682',
            'capacidade': 50,
            'preco_medio': 20.00,
            'aceita_reserva': False,
        },
    ]
    
    for rest_data in restaurantes_data:
        restaurante, created = Restaurante.objects.get_or_create(
            nome=rest_data['nome'],
            defaults=rest_data
        )
        if created:
            print(f"Restaurante criado: {restaurante.nome}")

def main():
    print("Criando dados iniciais para o Infinity Park...")
    
    print("\n1. Criando categorias...")
    criar_categorias()
    
    print("\n2. Criando atrações...")
    criar_atracoes()
    
    print("\n3. Criando restaurantes...")
    criar_restaurantes()
    
    print("\nDados iniciais criados com sucesso!")
    print("Agora você pode acessar o painel administrativo e ver todas as atrações e restaurantes.")

if __name__ == "__main__":
    main()