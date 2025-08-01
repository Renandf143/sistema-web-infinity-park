from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from decimal import Decimal
import uuid

class TipoIngresso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])
    cor = models.CharField(max_length=7, default='#007bff')
    icone = models.CharField(max_length=50, default='fas fa-ticket-alt')
    ativo = models.BooleanField(default=True)
    
    # Benefícios inclusos
    acesso_fast_pass = models.BooleanField(default=False)
    acesso_vip = models.BooleanField(default=False)
    estacionamento_gratuito = models.BooleanField(default=False)
    desconto_restaurantes = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    desconto_loja = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    # Restrições
    idade_minima = models.IntegerField(default=0)
    idade_maxima = models.IntegerField(null=True, blank=True)
    validade_dias = models.IntegerField(default=1, help_text="Número de dias que o ingresso é válido")
    
    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Tipo de Ingresso'
        verbose_name_plural = 'Tipos de Ingressos'

class Promocao(models.Model):
    TIPOS_DESCONTO = [
        ('percentual', 'Percentual'),
        ('valor_fixo', 'Valor Fixo'),
    ]
    
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    codigo = models.CharField(max_length=50, unique=True, help_text="Código promocional")
    tipo_desconto = models.CharField(max_length=20, choices=TIPOS_DESCONTO)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Validade
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    
    # Restrições
    uso_maximo = models.IntegerField(default=1, help_text="Máximo de usos por usuário")
    quantidade_maxima = models.IntegerField(null=True, blank=True, help_text="Quantidade máxima de usos total")
    quantidade_usada = models.IntegerField(default=0)
    valor_minimo = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="Valor mínimo da compra")
    
    # Tipos aplicáveis
    tipos_aplicaveis = models.ManyToManyField(TipoIngresso, blank=True)
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.nome} ({self.codigo})'
    
    def esta_valida(self):
        from django.utils import timezone
        now = timezone.now()
        return (self.ativo and 
                self.data_inicio <= now <= self.data_fim and
                (self.quantidade_maxima is None or self.quantidade_usada < self.quantidade_maxima))
    
    def pode_usar(self, usuario):
        if not self.esta_valida():
            return False
        
        usos_usuario = Compra.objects.filter(
            usuario=usuario,
            promocao=self,
            status='confirmado'
        ).count()
        
        return usos_usuario < self.uso_maximo
    
    class Meta:
        verbose_name = 'Promoção'
        verbose_name_plural = 'Promoções'

class Compra(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('confirmado', 'Confirmado'),
        ('cancelado', 'Cancelado'),
        ('usado', 'Usado'),
    ]
    
    # Identificação
    codigo = models.CharField(max_length=20, unique=True, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='compras')
    
    # Dados da compra
    data_compra = models.DateTimeField(auto_now_add=True)
    data_uso = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    # Valores
    valor_subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    valor_desconto = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Promoção aplicada
    promocao = models.ForeignKey(Promocao, on_delete=models.SET_NULL, null=True, blank=True)
    codigo_promocional = models.CharField(max_length=50, blank=True)
    
    # Dados do comprador
    nome_completo = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    
    # Observações
    observacoes = models.TextField(blank=True)
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            import random
            import string
            self.codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Compra {self.codigo} - {self.usuario.username}'
    
    def get_absolute_url(self):
        return reverse('ingressos:compra_detalhe', kwargs={'codigo': self.codigo})
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['-data_compra']

class ItemCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='itens')
    tipo_ingresso = models.ForeignKey(TipoIngresso, on_delete=models.CASCADE)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)])
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    preco_total = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.preco_total = self.quantidade * self.preco_unitario
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'{self.quantidade}x {self.tipo_ingresso.nome}'
    
    class Meta:
        verbose_name = 'Item da Compra'
        verbose_name_plural = 'Itens da Compra'

class Ingresso(models.Model):
    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('usado', 'Usado'),
        ('cancelado', 'Cancelado'),
        ('expirado', 'Expirado'),
    ]
    
    # Identificação
    codigo = models.CharField(max_length=20, unique=True, editable=False)
    qr_code = models.CharField(max_length=100, unique=True, editable=False)
    
    # Relacionamentos
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='ingressos')
    tipo_ingresso = models.ForeignKey(TipoIngresso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ingressos')
    
    # Dados do ingresso
    data_validade = models.DateTimeField()
    data_uso = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ativo')
    
    # Dados do visitante
    nome_visitante = models.CharField(max_length=200)
    cpf_visitante = models.CharField(max_length=14, blank=True)
    idade = models.IntegerField(null=True, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.codigo:
            import random
            import string
            self.codigo = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        
        if not self.qr_code:
            self.qr_code = str(uuid.uuid4())
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f'Ingresso {self.codigo} - {self.nome_visitante}'
    
    def esta_valido(self):
        from django.utils import timezone
        return (self.status == 'ativo' and 
                self.data_validade >= timezone.now())
    
    def pode_usar(self):
        return self.esta_valido() and self.status == 'ativo'
    
    class Meta:
        verbose_name = 'Ingresso'
        verbose_name_plural = 'Ingressos'
        ordering = ['-data_validade']

class UsoIngresso(models.Model):
    TIPOS_USO = [
        ('entrada', 'Entrada no Parque'),
        ('atracao', 'Uso em Atração'),
        ('fast_pass', 'Fast Pass'),
        ('restaurante', 'Restaurante'),
        ('loja', 'Loja'),
    ]
    
    ingresso = models.ForeignKey(Ingresso, on_delete=models.CASCADE, related_name='usos')
    tipo_uso = models.CharField(max_length=20, choices=TIPOS_USO)
    data_uso = models.DateTimeField(auto_now_add=True)
    local = models.CharField(max_length=200, blank=True)
    observacoes = models.TextField(blank=True)
    
    def __str__(self):
        return f'{self.get_tipo_uso_display()} - {self.ingresso.codigo}'
    
    class Meta:
        verbose_name = 'Uso de Ingresso'
        verbose_name_plural = 'Usos de Ingressos'
        ordering = ['-data_uso']