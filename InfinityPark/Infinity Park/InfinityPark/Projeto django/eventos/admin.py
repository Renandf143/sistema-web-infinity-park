from django.contrib import admin
from .models import CategoriaEvento, Evento, AvaliacaoEvento, EventoFavorito, IngressoEvento

@admin.register(CategoriaEvento)
class CategoriaEventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cor', 'icone')
    search_fields = ('nome', 'descricao')

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'local', 'data_inicio', 'tipo', 'gratuito', 'ativo', 'destaque')
    list_filter = ('categoria', 'tipo', 'faixa_etaria', 'gratuito', 'ativo', 'destaque')
    search_fields = ('nome', 'descricao', 'local', 'artistas')
    list_editable = ('ativo', 'destaque')
    date_hierarchy = 'data_inicio'
    
    fieldsets = (
        ('Informações Básicas', {
            'fields': ('nome', 'descricao', 'categoria', 'tipo', 'faixa_etaria')
        }),
        ('Localização e Horários', {
            'fields': ('local', 'capacidade', 'data_inicio', 'data_fim', 'duracao_minutos')
        }),
        ('Mídia', {
            'fields': ('imagem_principal', 'galeria_imagens')
        }),
        ('Detalhes', {
            'fields': ('artistas', 'requisitos', 'observacoes')
        }),
        ('Configurações', {
            'fields': ('ativo', 'destaque', 'gratuito', 'preco')
        }),
    )

@admin.register(AvaliacaoEvento)
class AvaliacaoEventoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'usuario', 'nota', 'criado_em')
    list_filter = ('nota', 'criado_em')
    search_fields = ('evento__nome', 'usuario__username', 'comentario')
    readonly_fields = ('criado_em',)

@admin.register(EventoFavorito)
class EventoFavoritoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'evento', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('usuario__username', 'evento__nome')

@admin.register(IngressoEvento)
class IngressoEventoAdmin(admin.ModelAdmin):
    list_display = ('evento', 'nome', 'tipo', 'preco', 'quantidade_disponivel', 'status')
    list_filter = ('tipo', 'status')
    search_fields = ('evento__nome', 'nome')
    list_editable = ('status',)