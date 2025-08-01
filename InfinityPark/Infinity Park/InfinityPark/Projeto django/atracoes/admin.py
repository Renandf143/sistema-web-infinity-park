from django.contrib import admin
from django.utils.html import format_html
from .models import (
    CategoriaAtracao, AreaParque, Atracao, AvaliacaoAtracao,
    FavoritoUsuario, TempoEspera, ServicoParque
)

@admin.register(CategoriaAtracao)
class CategoriaAtracaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'cor_preview']
    list_filter = ['tipo']
    search_fields = ['nome', 'descricao']
    
    def cor_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}; border: 1px solid #ddd;"></div>',
            obj.cor
        )
    cor_preview.short_description = 'Cor'

@admin.register(AreaParque)
class AreaParqueAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tema', 'cor_preview']
    list_filter = ['tema']
    search_fields = ['nome', 'descricao']
    
    def cor_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}; border: 1px solid #ddd;"></div>',
            obj.cor
        )
    cor_preview.short_description = 'Cor'

@admin.register(Atracao)
class AtracaoAdmin(admin.ModelAdmin):
    list_display = [
        'nome', 'categoria', 'area', 'nivel_emocao', 'tempo_espera',
        'avaliacao', 'ativa', 'imagem_preview'
    ]
    list_filter = [
        'categoria', 'area', 'nivel_emocao', 'ativa', 
        'fast_pass_disponivel', 'acessivel_cadeirante'
    ]
    search_fields = ['nome', 'descricao', 'descricao_curta']
    list_editable = ['tempo_espera', 'ativa']
    readonly_fields = ['avaliacao', 'numero_avaliacoes', 'criado_em', 'atualizado_em']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'descricao_curta', 'categoria', 'area')
        }),
        ('Imagens', {
            'fields': ('imagem_principal', 'galeria_imagens')
        }),
        ('Localização', {
            'fields': ('coordenadas_mapa',)
        }),
        ('Especificações', {
            'fields': (
                'altura_minima', 'altura_maxima', 'duracao', 'capacidade', 
                'nivel_emocao', 'horario_abertura', 'horario_fechamento'
            )
        }),
        ('Status Operacional', {
            'fields': ('ativa', 'tempo_espera', 'fast_pass_disponivel')
        }),
        ('Acessibilidade', {
            'fields': (
                'acessivel_cadeirante', 'acesso_deficiente_auditivo', 
                'acesso_deficiente_visual'
            )
        }),
        ('Avaliações (Somente Leitura)', {
            'fields': ('avaliacao', 'numero_avaliacoes'),
            'classes': ('collapse',)
        }),
        ('Timestamps (Somente Leitura)', {
            'fields': ('criado_em', 'atualizado_em'),
            'classes': ('collapse',)
        }),
    )
    
    def imagem_preview(self, obj):
        if obj.imagem_principal:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px;" />',
                obj.imagem_principal
            )
        return "Sem imagem"
    imagem_preview.short_description = 'Prévia'
    
    actions = ['ativar_atracoes', 'desativar_atracoes', 'zerar_tempo_espera']
    
    def ativar_atracoes(self, request, queryset):
        count = queryset.update(ativa=True)
        self.message_user(request, f'{count} atrações foram ativadas.')
    ativar_atracoes.short_description = "Ativar atrações selecionadas"
    
    def desativar_atracoes(self, request, queryset):
        count = queryset.update(ativa=False)
        self.message_user(request, f'{count} atrações foram desativadas.')
    desativar_atracoes.short_description = "Desativar atrações selecionadas"
    
    def zerar_tempo_espera(self, request, queryset):
        count = queryset.update(tempo_espera=0)
        self.message_user(request, f'Tempo de espera zerado para {count} atrações.')
    zerar_tempo_espera.short_description = "Zerar tempo de espera"

@admin.register(AvaliacaoAtracao)
class AvaliacaoAtracaoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'atracao', 'nota', 'criado_em']
    list_filter = ['nota', 'criado_em', 'atracao__categoria']
    search_fields = ['usuario__username', 'atracao__nome', 'comentario']
    readonly_fields = ['criado_em']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('usuario', 'atracao')

@admin.register(FavoritoUsuario)
class FavoritoUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'atracao', 'criado_em']
    list_filter = ['criado_em', 'atracao__categoria']
    search_fields = ['usuario__username', 'atracao__nome']
    readonly_fields = ['criado_em']
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('usuario', 'atracao')

@admin.register(TempoEspera)
class TempoEsperaAdmin(admin.ModelAdmin):
    list_display = ['atracao', 'tempo_espera', 'timestamp']
    list_filter = ['timestamp', 'atracao__categoria', 'atracao__area']
    search_fields = ['atracao__nome']
    readonly_fields = ['timestamp']
    date_hierarchy = 'timestamp'
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('atracao')

@admin.register(ServicoParque)
class ServicoParqueAdmin(admin.ModelAdmin):
    list_display = ['nome', 'tipo', 'area', 'ativo']
    list_filter = ['tipo', 'area', 'ativo']
    search_fields = ['nome', 'descricao']
    list_editable = ['ativo']
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'tipo', 'area', 'descricao')
        }),
        ('Localização', {
            'fields': ('coordenadas_mapa', 'icone')
        }),
        ('Status', {
            'fields': ('ativo',)
        }),
    )