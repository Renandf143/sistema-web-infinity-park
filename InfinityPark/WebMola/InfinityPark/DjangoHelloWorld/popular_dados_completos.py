"""
Script para popular o banco de dados com dados realistas completos
Execute: python manage.py shell < popular_dados_completos.py
"""

import os
import django
from django.utils import timezone
from datetime import datetime, timedelta
from decimal import Decimal

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infinity_park.settings')
django.setup()

from atracoes.models import CategoriaAtracao, Atracao
from eventos.models import CategoriaEvento, Evento
from restaurantes.models import Restaurante
from hoteis.models import Hotel
from ingressos.models import TipoIngresso

def criar_categorias_atracoes():
    """Criar categorias de atrações"""
    categorias = [
        ('radical', 'Radical', 'Atrações para os mais corajosos'),
        ('familiar', 'Familiar', 'Diversão para toda a família'),
        ('infantil', 'Infantil', 'Especial para crianças'),
        ('show', 'Show', 'Espetáculos e apresentações'),
        ('animal', 'Animal', 'Interação com animais'),
    ]
    
    for tipo, nome, descricao in categorias:
        categoria, created = CategoriaAtracao.objects.get_or_create(
            tipo=tipo,
            defaults={'nome': nome, 'descricao': descricao}
        )
        if created:
            print(f"Categoria criada: {nome}")

def criar_atracoes_realistas():
    """Criar atrações realistas de parque"""
    # Buscar categorias
    radical = CategoriaAtracao.objects.get(tipo='radical')
    familiar = CategoriaAtracao.objects.get(tipo='familiar')
    infantil = CategoriaAtracao.objects.get(tipo='infantil')
    show = CategoriaAtracao.objects.get(tipo='show')
    
    atracoes = [
        # Atrações Radicais
        {
            'nome': 'Thunder Mountain',
            'descricao': 'Montanha-russa radical com loops duplos e velocidade de até 120 km/h. Uma experiência única de adrenalina com 8 inversões em 2 minutos de pura emoção.',
            'categoria': radical,
            'altura_minima': 140,
            'idade_minima': 12,
            'duracao': 2,
            'capacidade': 24,
            'nivel_emocao': 5,
            'tempo_fila_medio': 45,
            'regras': 'Não permitido para gestantes, pessoas com problemas cardíacos ou de coluna. Objetos soltos devem ser guardados nos armários.',
            'status': 'ativa'
        },
        {
            'nome': 'Tornado Spin',
            'descricao': 'Torre de queda livre com 80 metros de altura. Suba devagar e desça em queda livre a 100 km/h. Vista panorâmica incrível do parque.',
            'categoria': radical,
            'altura_minima': 135,
            'idade_minima': 10,
            'duracao': 3,
            'capacidade': 16,
            'nivel_emocao': 5,
            'tempo_fila_medio': 30,
            'regras': 'Não permitido para gestantes. Peso máximo 120kg por pessoa.',
            'status': 'ativa'
        },
        {
            'nome': 'Sky Screamer',
            'descricao': 'Montanha-russa invertida com trilhos suspensos. Pés livres balançando enquanto você voa pelos ares em alta velocidade.',
            'categoria': radical,
            'altura_minima': 140,
            'idade_minima': 12,
            'duracao': 2,
            'capacidade': 20,
            'nivel_emocao': 5,
            'tempo_fila_medio': 40,
            'regras': 'Calçados obrigatórios (sem sandálias). Não permitido para gestantes.',
            'status': 'ativa'
        },
        
        # Atrações Familiares
        {
            'nome': 'Roda Gigante Panorâmica',
            'descricao': 'Roda gigante de 65 metros com cabines climatizadas. Vista de 360° do parque e da cidade. Perfeita para toda a família.',
            'categoria': familiar,
            'altura_minima': None,
            'idade_minima': None,
            'duracao': 8,
            'capacidade': 120,
            'nivel_emocao': 2,
            'tempo_fila_medio': 15,
            'regras': 'Crianças menores de 7 anos devem estar acompanhadas.',
            'status': 'ativa'
        },
        {
            'nome': 'Trem Fantasma',
            'descricao': 'Passeio assombrado com efeitos especiais, animatrônicos e sustos controlados. Diversão garantida para toda a família.',
            'categoria': familiar,
            'altura_minima': 100,
            'idade_minima': 6,
            'duracao': 5,
            'capacidade': 8,
            'nivel_emocao': 3,
            'tempo_fila_medio': 25,
            'regras': 'Não recomendado para crianças menores de 6 anos. Efeitos de luz e som.',
            'status': 'ativa'
        },
        {
            'nome': 'Montanha Russa Familiar',
            'descricao': 'Montanha-russa suave com curvas divertidas, sem inversões. Ideal para primeira experiência em montanha-russa.',
            'categoria': familiar,
            'altura_minima': 110,
            'idade_minima': 5,
            'duracao': 3,
            'capacidade': 16,
            'nivel_emocao': 3,
            'tempo_fila_medio': 20,
            'regras': 'Crianças menores de 10 anos devem estar acompanhadas.',
            'status': 'ativa'
        },
        
        # Atrações Infantis
        {
            'nome': 'Carrossel Mágico',
            'descricao': 'Carrossel clássico com cavalos coloridos e música alegre. Decorado com luzes LED e personagens encantados.',
            'categoria': infantil,
            'altura_minima': None,
            'idade_minima': None,
            'duracao': 4,
            'capacidade': 32,
            'nivel_emocao': 1,
            'tempo_fila_medio': 10,
            'regras': 'Crianças menores de 4 anos devem estar acompanhadas.',
            'status': 'ativa'
        },
        {
            'nome': 'Barcos Pirata',
            'descricao': 'Barquinhos em piscina com jatos d\'água e ilha do tesouro. Aventura pirata para os pequenos exploradores.',
            'categoria': infantil,
            'altura_minima': 90,
            'idade_minima': 3,
            'duracao': 6,
            'capacidade': 12,
            'nivel_emocao': 2,
            'tempo_fila_medio': 15,
            'regras': 'Crianças devem usar colete salva-vidas fornecido.',
            'status': 'ativa'
        },
        {
            'nome': 'Trem do Zoológico',
            'descricao': 'Trem que percorre o mini zoológico do parque. Veja animais de perto em um passeio educativo e divertido.',
            'categoria': infantil,
            'altura_minima': None,
            'idade_minima': None,
            'duracao': 12,
            'capacidade': 40,
            'nivel_emocao': 1,
            'tempo_fila_medio': 8,
            'regras': 'Não é permitido alimentar os animais.',
            'status': 'ativa'
        }
    ]
    
    for atracao_data in atracoes:
        atracao, created = Atracao.objects.get_or_create(
            nome=atracao_data['nome'],
            defaults=atracao_data
        )
        if created:
            print(f"Atração criada: {atracao_data['nome']}")

def criar_categorias_eventos():
    """Criar categorias de eventos"""
    categorias = [
        ('show', 'Show', 'Apresentações musicais e artísticas'),
        ('espetaculo', 'Espetáculo', 'Grandes espetáculos temáticos'),
        ('parada', 'Parada', 'Desfiles e paradas'),
        ('encontro_personagem', 'Encontro com Personagem', 'Encontros com personagens'),
        ('evento_especial', 'Evento Especial', 'Eventos sazonais especiais'),
    ]
    
    for tipo, nome, descricao in categorias:
        categoria, created = CategoriaEvento.objects.get_or_create(
            tipo=tipo,
            defaults={'nome': nome, 'descricao': descricao}
        )
        if created:
            print(f"Categoria de evento criada: {nome}")

def criar_eventos_realistas():
    """Criar eventos realistas"""
    # Buscar categorias
    show = CategoriaEvento.objects.get(tipo='show')
    espetaculo = CategoriaEvento.objects.get(tipo='espetaculo')
    parada = CategoriaEvento.objects.get(tipo='parada')
    encontro = CategoriaEvento.objects.get(tipo='encontro_personagem')
    
    # Datas dos próximos dias
    hoje = timezone.now().date()
    
    eventos = [
        # Shows
        {
            'nome': 'Show Musical: Clássicos do Rock',
            'descricao': 'Apresentação ao vivo com as maiores hits do rock internacional. Banda completa com efeitos visuais e pirotecnia.',
            'categoria': show,
            'data_evento': hoje + timedelta(days=1),
            'hora_inicio': datetime.strptime('19:00', '%H:%M').time(),
            'hora_fim': datetime.strptime('20:30', '%H:%M').time(),
            'duracao': 90,
            'local': 'Teatro Principal',
            'capacidade': 500,
            'preco': Decimal('25.00'),
            'artistas_performers': 'Banda Thunder Rock, Vocalista Maria Silva',
            'detalhes_extras': 'Show com efeitos especiais de luz e som. Recomendado para maiores de 8 anos.',
            'requer_ingresso_adicional': True
        },
        {
            'nome': 'Show Infantil: Aventuras na Floresta',
            'descricao': 'Show interativo para crianças com personagens animados, músicas e danças. Participação do público.',
            'categoria': show,
            'data_evento': hoje + timedelta(days=2),
            'hora_inicio': datetime.strptime('15:00', '%H:%M').time(),
            'hora_fim': datetime.strptime('16:00', '%H:%M').time(),
            'duracao': 60,
            'local': 'Teatro Infantil',
            'capacidade': 200,
            'preco': None,
            'artistas_performers': 'Grupo Teatro Mágico',
            'detalhes_extras': 'Show gratuito incluído no ingresso do parque.',
            'requer_ingresso_adicional': False
        },
        
        # Espetáculos
        {
            'nome': 'Espetáculo: Circo dos Sonhos',
            'descricao': 'Grande espetáculo circense com acrobatas, malabaristas e palhaços. Uma experiência única para toda a família.',
            'categoria': espetaculo,
            'data_evento': hoje + timedelta(days=3),
            'hora_inicio': datetime.strptime('18:00', '%H:%M').time(),
            'hora_fim': datetime.strptime('19:30', '%H:%M').time(),
            'duracao': 90,
            'local': 'Arena Central',
            'capacidade': 800,
            'preco': Decimal('35.00'),
            'artistas_performers': 'Circo Internacional dos Sonhos',
            'detalhes_extras': 'Espetáculo com animais treinados e acrobacias aéreas.',
            'requer_ingresso_adicional': True
        },
        
        # Paradas
        {
            'nome': 'Grande Parada dos Personagens',
            'descricao': 'Desfile com todos os personagens do parque, carros alegóricos e muita música. Não perca!',
            'categoria': parada,
            'data_evento': hoje + timedelta(days=4),
            'hora_inicio': datetime.strptime('16:00', '%H:%M').time(),
            'hora_fim': datetime.strptime('17:00', '%H:%M').time(),
            'duracao': 60,
            'local': 'Avenida Principal',
            'capacidade': 2000,
            'preco': None,
            'artistas_performers': 'Personagens do Infinity Park',
            'detalhes_extras': 'Parada gratuita. Chegue cedo para garantir o melhor lugar.',
            'requer_ingresso_adicional': False
        },
        
        # Encontros
        {
            'nome': 'Encontro com Mascote Infinity',
            'descricao': 'Encontro e sessão de fotos com o mascote oficial do parque. Autógrafos e abraços garantidos!',
            'categoria': encontro,
            'data_evento': hoje + timedelta(days=1),
            'hora_inicio': datetime.strptime('14:00', '%H:%M').time(),
            'hora_fim': datetime.strptime('15:00', '%H:%M').time(),
            'duracao': 60,
            'local': 'Praça Central',
            'capacidade': 50,
            'preco': None,
            'artistas_performers': 'Mascote Infinity',
            'detalhes_extras': 'Atividade gratuita. Limite de 1 foto por família.',
            'requer_ingresso_adicional': False
        }
    ]
    
    for evento_data in eventos:
        evento, created = Evento.objects.get_or_create(
            nome=evento_data['nome'],
            defaults=evento_data
        )
        if created:
            print(f"Evento criado: {evento_data['nome']}")

def criar_restaurantes_realistas():
    """Criar restaurantes realistas"""
    restaurantes = [
        {
            'nome': 'Pizzaria Infinity',
            'categoria': 'pizzaria',
            'descricao': 'Pizzas artesanais com ingredientes frescos. Ambiente familiar com vista para as atrações principais. Menu kids disponível. Opções vegetarianas e veganas.',
            'horario_funcionamento': '11:00 - 22:00',
            'telefone': '(11) 3456-7890',
            'capacidade': 80,
            'preco_medio': Decimal('45.00'),
            'aceita_reserva': True,
            'status': 'aberto'
        },
        {
            'nome': 'Hamburgueria Thunder',
            'categoria': 'lanchonete',
            'descricao': 'Hambúrgueres gourmet e batatas especiais. Ambiente descontraído com música ao vivo nos fins de semana. Hambúrgueres de 200g, batatas rústicas e milk-shakes.',
            'horario_funcionamento': '12:00 - 23:00',
            'telefone': '(11) 3456-7891',
            'capacidade': 60,
            'preco_medio': Decimal('35.00'),
            'aceita_reserva': True,
            'status': 'aberto'
        },
        {
            'nome': 'Café Panorâmico',
            'categoria': 'cafeteria',
            'descricao': 'Cafeteria com vista panorâmica do parque. Cafés especiais, doces e salgados. Wi-Fi gratuito. Ideal para relaxar e apreciar a vista.',
            'horario_funcionamento': '08:00 - 20:00',
            'telefone': '(11) 3456-7892',
            'capacidade': 40,
            'preco_medio': Decimal('25.00'),
            'aceita_reserva': False,
            'status': 'aberto'
        },
        {
            'nome': 'Restaurante Família',
            'categoria': 'restaurante',
            'descricao': 'Culinária brasileira tradicional com pratos para toda a família. Ambiente acolhedor e preços justos. Buffet aos domingos. Cadeirões para bebês disponíveis.',
            'horario_funcionamento': '11:30 - 21:30',
            'telefone': '(11) 3456-7893',
            'capacidade': 120,
            'preco_medio': Decimal('40.00'),
            'aceita_reserva': True,
            'status': 'aberto'
        },
        {
            'nome': 'Sorveteria Gelato',
            'categoria': 'sorveteria',
            'descricao': 'Sorvetes artesanais, açaí e milk-shakes. Sabores únicos e ingredientes naturais. Sorvetes sem açúcar e opções veganas disponíveis.',
            'horario_funcionamento': '10:00 - 22:00',
            'telefone': '(11) 3456-7894',
            'capacidade': 30,
            'preco_medio': Decimal('18.00'),
            'aceita_reserva': False,
            'status': 'aberto'
        }
    ]
    
    for restaurante_data in restaurantes:
        restaurante, created = Restaurante.objects.get_or_create(
            nome=restaurante_data['nome'],
            defaults=restaurante_data
        )
        if created:
            print(f"Restaurante criado: {restaurante_data['nome']}")

def criar_hoteis_realistas():
    """Criar hotéis realistas"""
    # Primeiro criar categoria para hotéis
    from hoteis.models import CategoriaHotel
    
    categoria_luxo, _ = CategoriaHotel.objects.get_or_create(
        tipo='luxo',
        defaults={'nome': 'Luxo', 'descricao': 'Hotéis de alto padrão'}
    )
    
    categoria_familiar, _ = CategoriaHotel.objects.get_or_create(
        tipo='familiar',
        defaults={'nome': 'Familiar', 'descricao': 'Hotéis para famílias'}
    )
    
    categoria_economico, _ = CategoriaHotel.objects.get_or_create(
        tipo='economico',
        defaults={'nome': 'Econômico', 'descricao': 'Hotéis econômicos'}
    )
    
    hoteis = [
        {
            'nome': 'Hotel Infinity Resort',
            'descricao': 'Hotel 5 estrelas com vista para o parque. Quartos luxuosos, spa, piscina e acesso direto ao parque. Ingresso VIP para o parque incluído. Serviço de quarto 24h.',
            'categoria': categoria_luxo,
            'endereco': 'Entrada Principal do Parque',
            'distancia_parque': Decimal('0.1'),
            'estrelas': 5,
            'quartos_disponiveis': 15,
            'total_quartos': 200,
            'wifi_gratuito': True,
            'estacionamento': True,
            'piscina': True,
            'academia': True,
            'restaurante': True,
            'spa': True,
            'transporte_parque': False,
            'preco_diaria_base': Decimal('450.00'),
            'telefone': '(11) 4567-8901',
            'email': 'reservas@infinityresort.com',
            'status': 'disponivel',
            'avaliacao_media': Decimal('4.8')
        },
        {
            'nome': 'Pousada Aventura',
            'descricao': 'Pousada temática com decoração de aventura. Ideal para famílias que buscam conforto e diversão. Café da manhã incluso. Transporte gratuito para o parque.',
            'categoria': categoria_familiar,
            'endereco': 'A 500m da entrada do parque',
            'distancia_parque': Decimal('0.5'),
            'estrelas': 3,
            'quartos_disponiveis': 8,
            'total_quartos': 80,
            'wifi_gratuito': True,
            'estacionamento': True,
            'piscina': True,
            'academia': False,
            'restaurante': True,
            'spa': False,
            'transporte_parque': True,
            'preco_diaria_base': Decimal('180.00'),
            'telefone': '(11) 4567-8902',
            'email': 'contato@pousadaaventura.com',
            'status': 'disponivel',
            'avaliacao_media': Decimal('4.2')
        },
        {
            'nome': 'Hotel Econômico Parque',
            'descricao': 'Hotel econômico com boa localização. Quartos limpos e confortáveis para quem busca economia. Café da manhã simples incluso. Ônibus para o parque a cada 30 min.',
            'categoria': categoria_economico,
            'endereco': 'A 1km da entrada do parque',
            'distancia_parque': Decimal('1.0'),
            'estrelas': 2,
            'quartos_disponiveis': 12,
            'total_quartos': 50,
            'wifi_gratuito': True,
            'estacionamento': True,
            'piscina': False,
            'academia': False,
            'restaurante': False,
            'spa': False,
            'transporte_parque': True,
            'preco_diaria_base': Decimal('95.00'),
            'telefone': '(11) 4567-8903',
            'email': 'reservas@hoteleconomicoparque.com',
            'status': 'disponivel',
            'avaliacao_media': Decimal('3.8')
        }
    ]
    
    for hotel_data in hoteis:
        hotel, created = Hotel.objects.get_or_create(
            nome=hotel_data['nome'],
            defaults=hotel_data
        )
        if created:
            print(f"Hotel criado: {hotel_data['nome']}")

def criar_tipos_ingressos():
    """Criar tipos de ingressos realistas"""
    ingressos = [
        {
            'nome': 'Ingresso Básico',
            'tipo': 'diario',
            'descricao': 'Acesso a todas as atrações do parque por 1 dia. Ideal para quem quer aproveitar o máximo do parque. Inclui acesso a todas as atrações, shows gratuitos, paradas e encontros com personagens.',
            'preco': Decimal('85.00'),
            'validade_dias': 1,
            'ativo': True,
            'destaque': False,
            'acesso_vip': False,
            'acesso_fast_pass': False,
            'inclui_estacionamento': False,
            'inclui_refeicao': False
        },
        {
            'nome': 'Ingresso VIP',
            'tipo': 'vip',
            'descricao': 'Experiência premium com Fast Pass e benefícios exclusivos. Pule filas e aproveite mais! Inclui Fast Pass para todas as atrações, estacionamento gratuito, desconto de 20% em restaurantes.',
            'preco': Decimal('150.00'),
            'validade_dias': 1,
            'ativo': True,
            'destaque': True,
            'acesso_vip': True,
            'acesso_fast_pass': True,
            'inclui_estacionamento': True,
            'inclui_refeicao': False
        },
        {
            'nome': 'Ingresso Estudante',
            'tipo': 'estudante',
            'descricao': 'Desconto especial para estudantes com documento. Acesso a todas as atrações com preço especial.',
            'preco': Decimal('65.00'),
            'validade_dias': 1,
            'ativo': True,
            'destaque': False,
            'acesso_vip': False,
            'acesso_fast_pass': False,
            'inclui_estacionamento': False,
            'inclui_refeicao': False
        },
        {
            'nome': 'Pacote Familiar',
            'tipo': 'familiar',
            'descricao': 'Pacote especial para famílias de até 4 pessoas. Inclui estacionamento gratuito e voucher de R$ 50 para restaurantes.',
            'preco': Decimal('280.00'),
            'validade_dias': 1,
            'ativo': True,
            'destaque': True,
            'acesso_vip': False,
            'acesso_fast_pass': False,
            'inclui_estacionamento': True,
            'inclui_refeicao': True
        },
        {
            'nome': 'Passaporte Anual',
            'tipo': 'anual',
            'descricao': 'Acesso ilimitado ao parque por 1 ano inteiro. Inclui todos os benefícios VIP, estacionamento gratuito e descontos em restaurantes.',
            'preco': Decimal('850.00'),
            'validade_dias': 365,
            'ativo': True,
            'destaque': True,
            'acesso_vip': True,
            'acesso_fast_pass': True,
            'inclui_estacionamento': True,
            'inclui_refeicao': False
        }
    ]
    
    for ingresso_data in ingressos:
        ingresso, created = TipoIngresso.objects.get_or_create(
            nome=ingresso_data['nome'],
            defaults=ingresso_data
        )
        if created:
            print(f"Tipo de ingresso criado: {ingresso_data['nome']}")

def main():
    """Função principal para executar todos os dados"""
    print("Iniciando criação de dados realistas...")
    
    # Criar dados na ordem correta
    criar_categorias_atracoes()
    criar_atracoes_realistas()
    
    criar_categorias_eventos()
    criar_eventos_realistas()
    
    criar_restaurantes_realistas()
    criar_hoteis_realistas()
    criar_tipos_ingressos()
    
    print("\nDados criados com sucesso!")
    print("O banco de dados agora contém:")
    print(f"- {Atracao.objects.count()} atrações")
    print(f"- {Evento.objects.count()} eventos")
    print(f"- {Restaurante.objects.count()} restaurantes")
    print(f"- {Hotel.objects.count()} hotéis")
    print(f"- {TipoIngresso.objects.count()} tipos de ingressos")

if __name__ == "__main__":
    main()