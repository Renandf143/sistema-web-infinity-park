from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q, Avg
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
import json
from .models import (
    Atracao, CategoriaAtracao, AreaParque, AvaliacaoAtracao, 
    FavoritoUsuario, TempoEspera, ServicoParque
)

def home(request):
    """Página inicial do parque"""
    # Atrações em destaque (mais bem avaliadas)
    atracoes_destaque = Atracao.objects.filter(ativa=True).order_by('-avaliacao')[:6]
    
    # Áreas do parque
    areas = AreaParque.objects.all()
    
    # Estatísticas do parque
    total_atracoes = Atracao.objects.filter(ativa=True).count()
    total_areas = areas.count()
    
    context = {
        'atracoes_destaque': atracoes_destaque,
        'areas': areas,
        'total_atracoes': total_atracoes,
        'total_areas': total_areas,
    }
    return render(request, 'atracoes/home.html', context)

def lista_atracoes(request):
    """Lista todas as atrações com filtros"""
    atracoes = Atracao.objects.filter(ativa=True)
    
    # Filtros
    categoria_id = request.GET.get('categoria')
    area_id = request.GET.get('area')
    nivel_emocao = request.GET.get('nivel_emocao')
    busca = request.GET.get('busca')
    
    if categoria_id:
        atracoes = atracoes.filter(categoria_id=categoria_id)
    
    if area_id:
        atracoes = atracoes.filter(area_id=area_id)
        
    if nivel_emocao:
        atracoes = atracoes.filter(nivel_emocao=nivel_emocao)
    
    if busca:
        atracoes = atracoes.filter(
            Q(nome__icontains=busca) | 
            Q(descricao__icontains=busca) |
            Q(descricao_curta__icontains=busca)
        )
    
    # Ordenação
    ordenacao = request.GET.get('ordem', 'nome')
    if ordenacao == 'avaliacao':
        atracoes = atracoes.order_by('-avaliacao')
    elif ordenacao == 'tempo_espera':
        atracoes = atracoes.order_by('tempo_espera')
    elif ordenacao == 'emocao':
        atracoes = atracoes.order_by('-nivel_emocao')
    else:
        atracoes = atracoes.order_by('nome')
    
    # Paginação
    paginator = Paginator(atracoes, 12)
    page = request.GET.get('page')
    atracoes_paginadas = paginator.get_page(page)
    
    # Dados para filtros
    categorias = CategoriaAtracao.objects.all()
    areas = AreaParque.objects.all()
    
    context = {
        'atracoes': atracoes_paginadas,
        'categorias': categorias,
        'areas': areas,
        'filtros_aplicados': {
            'categoria': categoria_id,
            'area': area_id,
            'nivel_emocao': nivel_emocao,
            'busca': busca,
            'ordem': ordenacao,
        }
    }
    return render(request, 'atracoes/lista.html', context)

def detalhe_atracao(request, atracao_id):
    """Página de detalhes de uma atração"""
    atracao = get_object_or_404(Atracao, id=atracao_id, ativa=True)
    
    # Verificar se é favorito do usuário (se logado)
    eh_favorito = False
    if request.user.is_authenticated:
        eh_favorito = FavoritoUsuario.objects.filter(
            usuario=request.user, 
            atracao=atracao
        ).exists()
    
    # Avaliações recentes
    avaliacoes = AvaliacaoAtracao.objects.filter(atracao=atracao).order_by('-criado_em')[:5]
    
    # Atrações similares (mesma categoria ou área)
    atracoes_similares = Atracao.objects.filter(
        Q(categoria=atracao.categoria) | Q(area=atracao.area),
        ativa=True
    ).exclude(id=atracao.id).order_by('-avaliacao')[:4]
    
    # Histórico de tempo de espera (últimas 24h)
    historico_espera = TempoEspera.objects.filter(
        atracao=atracao
    ).order_by('-timestamp')[:24]
    
    context = {
        'atracao': atracao,
        'eh_favorito': eh_favorito,
        'avaliacoes': avaliacoes,
        'atracoes_similares': atracoes_similares,
        'historico_espera': historico_espera,
        'pode_avaliar': request.user.is_authenticated,
    }
    return render(request, 'atracoes/detalhe.html', context)

def mapa_parque(request):
    """Mapa interativo do parque"""
    areas = AreaParque.objects.all()
    atracoes = Atracao.objects.filter(ativa=True)
    servicos = ServicoParque.objects.filter(ativo=True)
    
    # Converter para JSON para uso no JavaScript
    areas_json = []
    for area in areas:
        areas_json.append({
            'id': area.id,
            'nome': area.nome,
            'tema': area.tema,
            'cor': area.cor,
            'coordenadas': area.coordenadas_mapa,
        })
    
    atracoes_json = []
    for atracao in atracoes:
        atracoes_json.append({
            'id': atracao.id,
            'nome': atracao.nome,
            'categoria': atracao.categoria.nome,
            'tempo_espera': atracao.tempo_espera,
            'coordenadas': atracao.coordenadas_mapa,
            'avaliacao': atracao.avaliacao,
            'nivel_emocao': atracao.nivel_emocao,
        })
    
    servicos_json = []
    for servico in servicos:
        servicos_json.append({
            'id': servico.id,
            'nome': servico.nome,
            'tipo': servico.tipo,
            'icone': servico.icone,
            'coordenadas': servico.coordenadas_mapa,
        })
    
    context = {
        'areas': areas,
        'areas_json': json.dumps(areas_json),
        'atracoes_json': json.dumps(atracoes_json),
        'servicos_json': json.dumps(servicos_json),
    }
    return render(request, 'atracoes/mapa.html', context)

@login_required
def toggle_favorito(request, atracao_id):
    """Toggle favorito de uma atração"""
    if request.method == 'POST':
        atracao = get_object_or_404(Atracao, id=atracao_id)
        favorito, criado = FavoritoUsuario.objects.get_or_create(
            usuario=request.user,
            atracao=atracao
        )
        
        if not criado:
            favorito.delete()
            favoritado = False
            mensagem = f"{atracao.nome} removida dos favoritos"
        else:
            favoritado = True
            mensagem = f"{atracao.nome} adicionada aos favoritos"
        
        if request.headers.get('Content-Type') == 'application/json':
            return JsonResponse({
                'favoritado': favoritado,
                'mensagem': mensagem
            })
        else:
            messages.success(request, mensagem)
            return redirect('detalhe_atracao', atracao_id=atracao_id)
    
    return redirect('lista_atracoes')

@login_required 
def avaliar_atracao(request, atracao_id):
    """Avaliar uma atração"""
    if request.method == 'POST':
        atracao = get_object_or_404(Atracao, id=atracao_id)
        nota = int(request.POST.get('nota', 0))
        comentario = request.POST.get('comentario', '')
        
        if 1 <= nota <= 5:
            avaliacao, criado = AvaliacaoAtracao.objects.update_or_create(
                usuario=request.user,
                atracao=atracao,
                defaults={
                    'nota': nota,
                    'comentario': comentario
                }
            )
            
            # Atualizar média da atração
            media = AvaliacaoAtracao.objects.filter(atracao=atracao).aggregate(
                media=Avg('nota')
            )['media']
            atracao.avaliacao = round(media, 1) if media else 0
            atracao.numero_avaliacoes = AvaliacaoAtracao.objects.filter(atracao=atracao).count()
            atracao.save()
            
            if criado:
                messages.success(request, 'Avaliação adicionada com sucesso!')
            else:
                messages.success(request, 'Avaliação atualizada com sucesso!')
        else:
            messages.error(request, 'Nota deve ser entre 1 e 5 estrelas')
    
    return redirect('detalhe_atracao', atracao_id=atracao_id)

@login_required
def meus_favoritos(request):
    """Lista de atrações favoritas do usuário"""
    favoritos = FavoritoUsuario.objects.filter(usuario=request.user).select_related('atracao')
    
    context = {
        'favoritos': favoritos,
    }
    return render(request, 'atracoes/favoritos.html', context)

def api_tempos_espera(request):
    """API para tempos de espera em tempo real"""
    atracoes = Atracao.objects.filter(ativa=True).values(
        'id', 'nome', 'tempo_espera', 'fast_pass_disponivel'
    )
    
    data = []
    for atracao in atracoes:
        data.append({
            'id': atracao['id'],
            'nome': atracao['nome'],
            'tempo_espera': atracao['tempo_espera'],
            'fast_pass': atracao['fast_pass_disponivel'],
            'status': 'aberta' if atracao['tempo_espera'] >= 0 else 'fechada'
        })
    
    return JsonResponse({'atracoes': data})

def buscar_atracoes(request):
    """API de busca de atrações para autocomplete"""
    termo = request.GET.get('q', '')
    
    if len(termo) >= 2:
        atracoes = Atracao.objects.filter(
            Q(nome__icontains=termo) | Q(descricao_curta__icontains=termo),
            ativa=True
        ).values('id', 'nome', 'imagem_principal')[:10]
        
        resultados = list(atracoes)
    else:
        resultados = []
    
    return JsonResponse({'resultados': resultados})