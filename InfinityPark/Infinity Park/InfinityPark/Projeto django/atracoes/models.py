from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import json

class CategoriaAtracao(models.Model):
    # tipos de atração que temos no parque
    TIPO_CHOICES = [
        ('montanha_russa', 'Montanha-Russa'),
        ('aquatica', 'Aventura Aquática'),
        ('familia', 'Família'),
        ('radical', 'Radical'),
        ('infantil', 'Infantil'),
        ('simulador', 'Simulador'),
        ('show', 'Show'),
    ]
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    icone = models.CharField(max_length=50, default='star')  # Nome do ícone
    cor = models.CharField(max_length=7, default='#3B82F6')  # Cor hex
    
    class Meta:
        verbose_name = "Categoria de Atração"
        verbose_name_plural = "Categorias de Atrações"
        
    def __str__(self):
        return self.nome

class AreaParque(models.Model):
    # peguei inspiração na Disney pra essas áreas
    TEMA_CHOICES = [
        ('adventureland', 'Adventureland'),
        ('fantasyland', 'Fantasyland'),
        ('tomorrowland', 'Tomorrowland'),
        ('frontierland', 'Frontierland'),
        ('main_street', 'Main Street'),
    ]
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    tema = models.CharField(max_length=20, choices=TEMA_CHOICES)
    imagem = models.URLField(max_length=500)
    coordenadas_mapa = models.JSONField(default=dict)  # posição no mapa
    cor = models.CharField(max_length=7, default='#3B82F6')
    
    class Meta:
        verbose_name = "Área do Parque"
        verbose_name_plural = "Áreas do Parque"
        
    def __str__(self):
        return self.nome

class Atracao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    descricao_curta = models.CharField(max_length=300)
    categoria = models.ForeignKey(CategoriaAtracao, on_delete=models.CASCADE)
    area = models.ForeignKey(AreaParque, on_delete=models.CASCADE)
    
    # fotos da atração
    imagem_principal = models.URLField(max_length=500)
    galeria_imagens = models.JSONField(default=list)  # mais fotos
    
    # onde fica no mapa
    coordenadas_mapa = models.JSONField(default=dict)
    
    # infos importantes
    altura_minima = models.IntegerField(null=True, blank=True, help_text="altura mínima em cm")
    altura_maxima = models.IntegerField(null=True, blank=True, help_text="altura máxima em cm")
    duracao = models.IntegerField(help_text="quantos minutos dura")
    capacidade = models.IntegerField(help_text="quantas pessoas por vez")
    nivel_emocao = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="de 1 (suave) a 5 (radical)"
    )
    
    # se tá funcionando
    ativa = models.BooleanField(default=True)
    tempo_espera = models.IntegerField(default=0, help_text="fila atual em minutos")
    fast_pass_disponivel = models.BooleanField(default=False)
    
    # acessibilidade (importante!)
    acessivel_cadeirante = models.BooleanField(default=False)
    acesso_deficiente_auditivo = models.BooleanField(default=False)
    acesso_deficiente_visual = models.BooleanField(default=False)
    
    # notas dos visitantes
    avaliacao = models.FloatField(default=0.0)
    numero_avaliacoes = models.IntegerField(default=0)
    
    # horário de funcionamento
    horario_abertura = models.TimeField()
    horario_fechamento = models.TimeField()
    
    # controle interno
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Atração"
        verbose_name_plural = "Atrações"
        
    def __str__(self):
        return self.nome
    
    def get_tempo_espera_texto(self):
        if self.tempo_espera == 0:
            return "Sem fila"
        elif self.tempo_espera <= 15:
            return f"{self.tempo_espera} min - Rápido"
        elif self.tempo_espera <= 30:
            return f"{self.tempo_espera} min - Moderado"
        else:
            return f"{self.tempo_espera} min - Longo"
    
    def get_nivel_emocao_texto(self):
        niveis = {
            1: "Muito Suave",
            2: "Suave", 
            3: "Moderado",
            4: "Intenso",
            5: "Extremo"
        }
        return niveis.get(self.nivel_emocao, "N/A")

class AvaliacaoAtracao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    atracao = models.ForeignKey(Atracao, on_delete=models.CASCADE)
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Avaliação de Atração"
        verbose_name_plural = "Avaliações de Atrações"
        unique_together = ['usuario', 'atracao']
        
    def __str__(self):
        return f"{self.usuario.username} - {self.atracao.nome} ({self.nota}★)"

class FavoritoUsuario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    atracao = models.ForeignKey(Atracao, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Favorito do Usuário"
        verbose_name_plural = "Favoritos dos Usuários"
        unique_together = ['usuario', 'atracao']
        
    def __str__(self):
        return f"{self.usuario.username} ♥ {self.atracao.nome}"

class TempoEspera(models.Model):
    atracao = models.ForeignKey(Atracao, on_delete=models.CASCADE)
    tempo_espera = models.IntegerField(help_text="Tempo em minutos")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Histórico de Tempo de Espera"
        verbose_name_plural = "Histórico de Tempos de Espera"
        
    def __str__(self):
        return f"{self.atracao.nome} - {self.tempo_espera}min ({self.timestamp})"

class ServicoParque(models.Model):
    TIPO_CHOICES = [
        ('banheiro', 'Banheiro'),
        ('primeiros_socorros', 'Primeiros Socorros'),
        ('caixa_eletronico', 'Caixa Eletrônico'),
        ('loja_souvenir', 'Loja de Souvenirs'),
        ('ponto_fotografico', 'Ponto Fotográfico'),
        ('informacoes', 'Informações'),
        ('estacionamento', 'Estacionamento'),
        ('aluguel_carrinho', 'Aluguel de Carrinho'),
    ]
    
    nome = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    area = models.ForeignKey(AreaParque, on_delete=models.CASCADE)
    coordenadas_mapa = models.JSONField(default=dict)  # {x, y}
    icone = models.CharField(max_length=50, default='map-pin')
    ativo = models.BooleanField(default=True)
    descricao = models.TextField(blank=True)
    
    class Meta:
        verbose_name = "Serviço do Parque"
        verbose_name_plural = "Serviços do Parque"
        
    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"