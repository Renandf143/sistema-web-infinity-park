# funções úteis que criei durante o desenvolvimento
import random
from datetime import datetime, timedelta

def gerar_tempo_espera_aleatorio():
    """
    Gera um tempo de espera aleatório pras atrações
    Uso isso pra simular filas reais
    """
    # pesos baseados na minha experiência em parques reais
    tempos = [0, 5, 10, 15, 20, 25, 30, 45, 60, 75, 90]
    pesos = [5, 10, 15, 20, 15, 10, 10, 8, 5, 1, 1]  # mais provável ter fila pequena
    
    return random.choices(tempos, weights=pesos)[0]

def calcular_nivel_lotacao(tempo_espera):
    """
    Converte tempo de espera em nível de lotação
    """
    if tempo_espera == 0:
        return "vazio"
    elif tempo_espera <= 15:
        return "tranquilo"
    elif tempo_espera <= 30:
        return "moderado"
    elif tempo_espera <= 60:
        return "cheio"
    else:
        return "lotado"

def formatar_duracao(minutos):
    """
    Formata duração em texto mais amigável
    """
    if minutos < 60:
        return f"{minutos} min"
    else:
        horas = minutos // 60
        mins = minutos % 60
        if mins == 0:
            return f"{horas}h"
        else:
            return f"{horas}h{mins}min"

def gerar_horarios_evento():
    """
    Gera horários aleatórios pra eventos
    Baseado nos horários reais de parques
    """
    horarios_comuns = [
        "10:00", "11:30", "13:00", "14:30", 
        "16:00", "17:30", "19:00", "20:30"
    ]
    return random.choice(horarios_comuns)

def calcular_desconto_familia(num_pessoas):
    """
    Calcula desconto pra famílias grandes
    Ideia que tive mas ainda não implementei
    """
    if num_pessoas >= 5:
        return 0.15  # 15% desconto
    elif num_pessoas >= 4:
        return 0.10  # 10% desconto
    else:
        return 0.0

def sugerir_atracoes_similares(atracao_atual, todas_atracoes):
    """
    Algoritmo simples pra sugerir atrações similares
    Não é nada sofisticado, mas funciona
    """
    similares = []
    
    for atracao in todas_atracoes:
        if atracao.id == atracao_atual.id:
            continue
            
        pontos = 0
        
        # mesma categoria = +3 pontos
        if atracao.categoria == atracao_atual.categoria:
            pontos += 3
            
        # mesma área = +2 pontos  
        if atracao.area == atracao_atual.area:
            pontos += 2
            
        # nível de emoção similar = +1 ponto
        if abs(atracao.nivel_emocao - atracao_atual.nivel_emocao) <= 1:
            pontos += 1
            
        if pontos > 0:
            similares.append((atracao, pontos))
    
    # ordena por pontuação e pega as 4 melhores
    similares.sort(key=lambda x: x[1], reverse=True)
    return [atracao for atracao, pontos in similares[:4]]

# constantes que uso em vários lugares
EMOJI_NIVEIS = {
    1: "😊",  # suave
    2: "😄",  # legal  
    3: "😆",  # emocionante
    4: "😱",  # intenso
    5: "🤯"   # extremo
}

CORES_TEMPO_ESPERA = {
    "vazio": "#28a745",
    "tranquilo": "#17a2b8", 
    "moderado": "#ffc107",
    "cheio": "#fd7e14",
    "lotado": "#dc3545"
}