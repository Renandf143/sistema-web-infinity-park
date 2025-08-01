# configurações específicas do parque
# criei esse arquivo pra não bagunçar o settings.py

# horários de funcionamento
HORARIO_ABERTURA = "09:00"
HORARIO_FECHAMENTO = "22:00"

# preços base (em reais)
PRECO_INGRESSO_ADULTO = 89.90
PRECO_INGRESSO_CRIANCA = 59.90
PRECO_FAST_PASS = 29.90

# limites do sistema
MAX_AVALIACOES_POR_USUARIO = 50  # pra evitar spam
TEMPO_CACHE_FILA = 300  # 5 minutos
MAX_FAVORITOS = 20

# configurações do mapa
MAPA_LARGURA = 800
MAPA_ALTURA = 600

# cores das áreas (peguei do site da Disney)
CORES_AREAS = {
    'adventureland': '#8B4513',
    'fantasyland': '#9370DB', 
    'tomorrowland': '#4169E1',
    'frontierland': '#D2691E',
    'main_street': '#CD853F'
}

# mensagens personalizadas
MENSAGENS = {
    'boas_vindas': 'Bem-vindo ao Infinity Park! 🎢',
    'erro_fila': 'Ops! Não conseguimos atualizar o tempo de fila.',
    'sucesso_avaliacao': 'Obrigado pela sua avaliação! ⭐',
    'erro_login': 'Email ou senha incorretos. Tenta de novo!',
}

# integrações externas (quando implementar)
APIS_EXTERNAS = {
    'clima': 'https://api.openweathermap.org/data/2.5/weather',
    'pagamento': 'https://api.mercadopago.com/v1/payments',
    'email': 'smtp.gmail.com'  # pra enviar confirmações
}

# features que ainda vou implementar
FEATURES_FUTURAS = [
    'sistema_reserva_restaurante',
    'notificacoes_push', 
    'realidade_aumentada_mapa',
    'chatbot_atendimento'
]