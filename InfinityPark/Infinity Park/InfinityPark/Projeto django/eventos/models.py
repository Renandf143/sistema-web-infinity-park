from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
import json

class CategoriaEvento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    cor = models.CharField(max_length=7, default='#007bff')  # cor pro badge
    icone = models.CharField(max_length=50, default='fas fa-calendar')
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Categoria de Evento'
        verbose_name_plural = 'Categorias de Eventos'

class Evento(models.Model):
    # tipos de evento que temos
    TIPOS_EVENTO = [
        ('show', 'Show'),
        ('parada', 'Parada'),
        ('encontro', 'Encontro com Personagens'),
        ('workshop', 'Workshop'),
        ('competicao', 'Competição'),
        ('especial', 'Evento Especial'),
    ]
    
    # pra quem é o evento
    FAIXAS_ETARIAS = [
        ('livre', 'Livre'),
        ('infantil', 'Infantil (0-12 anos)'),
        ('teen', 'Teen (13-17 anos)'),
        ('adulto', 'Adulto (18+ anos)'),
        ('familia', 'Família'),
    ]
    
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.ForeignKey(CategoriaEvento, on_delete=models.CASCADE, related_name='eventos')
    tipo = models.CharField(max_length=20, choices=TIPOS_EVENTO)
    faixa_etaria = models.CharField(max_length=20, choices=FAIXAS_ETARIAS)
    
    # onde acontece
    local = models.CharField(max_length=200)
    capacidade = models.IntegerField(validators=[MinValueValidator(1)])
    
    # quando acontece
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    duracao_minutos = models.IntegerField(validators=[MinValueValidator(1)])
    
    # fotos do evento
    imagem_principal = models.URLField(blank=True)
    galeria_imagens = models.TextField(blank=True, help_text="URLs separadas por vírgula")
    
    # infos extras
    artistas = models.TextField(blank=True, help_text="quem vai se apresentar")
    requisitos = models.TextField(blank=True, help_text="se tem algum requisito especial")
    observacoes = models.TextField(blank=True)
    
    # configurações
    ativo = models.BooleanField(default=True)
    destaque = models.BooleanField(default=False)  # aparece na home
    gratuito = models.BooleanField(default=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    
    # avaliações dos visitantes
    avaliacao_media = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)
    total_avaliacoes = models.IntegerField(default=0)
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('eventos:detalhe', kwargs={'id': self.id})
    
    def get_galeria_lista(self):
        if self.galeria_imagens:
            return [img.strip() for img in self.galeria_imagens.split(',') if img.strip()]
        return []
    
    def get_artistas_lista(self):
        if self.artistas:
            return [artista.strip() for artista in self.artistas.split(',') if artista.strip()]
        return []
    
    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'
        ordering = ['-destaque', 'data_inicio']

class AvaliacaoEvento(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='avaliacoes')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comentario = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.usuario.username} - {self.evento.nome} ({self.nota}★)'
    
    class Meta:
        verbose_name = 'Avaliação de Evento'
        verbose_name_plural = 'Avaliações de Eventos'
        unique_together = ['evento', 'usuario']

class EventoFavorito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.usuario.username} - {self.evento.nome}'
    
    class Meta:
        verbose_name = 'Evento Favorito'
        verbose_name_plural = 'Eventos Favoritos'
        unique_together = ['usuario', 'evento']

class IngressoEvento(models.Model):
    TIPOS_INGRESSO = [
        ('gratuito', 'Gratuito'),
        ('pago', 'Pago'),
        ('vip', 'VIP'),
        ('premium', 'Premium'),
    ]
    
    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('esgotado', 'Esgotado'),
        ('suspenso', 'Suspenso'),
    ]
    
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='ingressos')
    tipo = models.CharField(max_length=20, choices=TIPOS_INGRESSO)
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_total = models.IntegerField(validators=[MinValueValidator(1)])
    quantidade_vendida = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='disponivel')
    
    def __str__(self):
        return f'{self.evento.nome} - {self.nome}'
    
    def quantidade_disponivel(self):
        return self.quantidade_total - self.quantidade_vendida
    
    def esta_esgotado(self):
        return self.quantidade_disponivel() <= 0
    
    class Meta:
        verbose_name = 'Ingresso de Evento'
        verbose_name_plural = 'Ingressos de Eventos'