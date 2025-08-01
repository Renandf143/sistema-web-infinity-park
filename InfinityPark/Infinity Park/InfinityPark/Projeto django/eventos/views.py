from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Q, Avg
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Evento, CategoriaEvento, AvaliacaoEvento, EventoFavorito, IngressoEvento
from datetime import datetime, timedelta
import json

def lista_eventos(request):
    eventos = Evento.objects.filter(ativo=True)
    categorias = CategoriaEvento.objects.all()
    
    # Filtros
    categoria_id = request.GET.get('categoria')
    tipo = request.GET.get('tipo')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')
    gratuito = request.GET.get('gratuito')
    busca = request.GET.get('q')
    
    if categoria_id:
        eventos = eventos.filter(categoria_id=categoria_id)
    
    if tipo:
        eventos = eventos.filter(tipo=tipo)
    
    if data_inicio:
        eventos = eventos.filter(data_inicio__gte=data_inicio)
    
    if data_fim:
        eventos = eventos.filter(data_fim__lte=data_fim)
    
    if gratuito == 'true':
        eventos = eventos.filter(gratuito=True)
    
    if busca:
        eventos = eventos.filter(
            Q(nome__icontains=busca) |
            Q(descricao__icontains=busca) |
            Q(local__icontains=busca) |
            Q(artistas__icontains=busca)
        )
    
    # Paginação
    paginator = Paginator(eventos, 12)
    page = request.GET.get('page')
    eventos = paginator.get_page(page)
    
    # Eventos em destaque
    eventos_destaque = Evento.objects.filter(ativo=True, destaque=True)[:6]
    
    # Próximos eventos
    proximos_eventos = Evento.objects.filter(
        ativo=True,
        data_inicio__gte=timezone.now()
    ).order_by('data_inicio')[:5]
    
    context = {
        'eventos': eventos,
        'categorias': categorias,
        'eventos_destaque': eventos_destaque,
        'proximos_eventos': proximos_eventos,
        'tipos_evento': Evento.TIPOS_EVENTO,
        'filtros': {
            'categoria': categoria_id,
            'tipo': tipo,
            'data_inicio': data_inicio,
            'data_fim': data_fim,
            'gratuito': gratuito,
            'busca': busca,
        }
    }
    
    return render(request, 'eventos/lista.html', context)

def detalhe_evento(request, id):
    evento = get_object_or_404(Evento, id=id, ativo=True)
    
    # Avaliações
    avaliacoes = AvaliacaoEvento.objects.filter(evento=evento).order_by('-criado_em')
    
    # Verificar se o usuário já avaliou
    avaliacao_usuario = None
    if request.user.is_authenticated:
        try:
            avaliacao_usuario = AvaliacaoEvento.objects.get(evento=evento, usuario=request.user)
        except AvaliacaoEvento.DoesNotExist:
            pass
    
    # Verificar se está nos favoritos
    eh_favorito = False
    if request.user.is_authenticated:
        eh_favorito = EventoFavorito.objects.filter(usuario=request.user, evento=evento).exists()
    
    # Ingressos disponíveis
    ingressos = IngressoEvento.objects.filter(evento=evento, status='disponivel')
    
    # Eventos relacionados
    eventos_relacionados = Evento.objects.filter(
        categoria=evento.categoria,
        ativo=True
    ).exclude(id=evento.id)[:4]
    
    context = {
        'evento': evento,
        'avaliacoes': avaliacoes,
        'avaliacao_usuario': avaliacao_usuario,
        'eh_favorito': eh_favorito,
        'ingressos': ingressos,
        'eventos_relacionados': eventos_relacionados,
        'galeria_imagens': evento.get_galeria_lista(),
        'artistas': evento.get_artistas_lista(),
    }
    
    return render(request, 'eventos/detalhe.html', context)

@login_required
def avaliar_evento(request, id):
    if request.method == 'POST':
        evento = get_object_or_404(Evento, id=id)
        nota = int(request.POST.get('nota', 0))
        comentario = request.POST.get('comentario', '')
        
        if 1 <= nota <= 5:
            avaliacao, created = AvaliacaoEvento.objects.get_or_create(
                evento=evento,
                usuario=request.user,
                defaults={'nota': nota, 'comentario': comentario}
            )
            
            if not created:
                avaliacao.nota = nota
                avaliacao.comentario = comentario
                avaliacao.save()
            
            # Atualizar média do evento
            media = AvaliacaoEvento.objects.filter(evento=evento).aggregate(Avg('nota'))['nota__avg']
            total = AvaliacaoEvento.objects.filter(evento=evento).count()
            
            evento.avaliacao_media = round(media, 1) if media else 0
            evento.total_avaliacoes = total
            evento.save()
            
            messages.success(request, 'Avaliação salva com sucesso!')
        else:
            messages.error(request, 'Nota inválida!')
    
    return redirect('eventos:detalhe', id=id)

@login_required
def toggle_favorito(request, id):
    if request.method == 'POST':
        evento = get_object_or_404(Evento, id=id)
        favorito, created = EventoFavorito.objects.get_or_create(
            usuario=request.user,
            evento=evento
        )
        
        if not created:
            favorito.delete()
            adicionado = False
        else:
            adicionado = True
        
        return JsonResponse({
            'success': True,
            'adicionado': adicionado,
            'message': 'Adicionado aos favoritos!' if adicionado else 'Removido dos favoritos!'
        })
    
    return JsonResponse({'success': False})

@login_required
def eventos_favoritos(request):
    favoritos = EventoFavorito.objects.filter(usuario=request.user).select_related('evento')
    
    # Estatísticas
    total_favoritos = favoritos.count()
    categorias_favoritas = {}
    
    for favorito in favoritos:
        cat = favorito.evento.categoria.nome
        categorias_favoritas[cat] = categorias_favoritas.get(cat, 0) + 1
    
    context = {
        'favoritos': favoritos,
        'total_favoritos': total_favoritos,
        'categorias_favoritas': categorias_favoritas,
    }
    
    return render(request, 'eventos/favoritos.html', context)

def buscar_eventos(request):
    query = request.GET.get('q', '')
    eventos = []
    
    if query and len(query) >= 2:
        eventos_queryset = Evento.objects.filter(
            Q(nome__icontains=query) |
            Q(descricao__icontains=query) |
            Q(local__icontains=query),
            ativo=True
        )[:10]
        
        eventos = [{
            'id': evento.id,
            'nome': evento.nome,
            'local': evento.local,
            'data_inicio': evento.data_inicio.strftime('%d/%m/%Y %H:%M'),
            'imagem_principal': evento.imagem_principal,
            'url': evento.get_absolute_url(),
        } for evento in eventos_queryset]
    
    return JsonResponse({'resultados': eventos})

def calendario_eventos(request):
    hoje = timezone.now().date()
    
    # Eventos do mês atual
    eventos_mes = Evento.objects.filter(
        ativo=True,
        data_inicio__month=hoje.month,
        data_inicio__year=hoje.year
    )
    
    # Eventos por data
    eventos_por_data = {}
    for evento in eventos_mes:
        data_str = evento.data_inicio.strftime('%Y-%m-%d')
        if data_str not in eventos_por_data:
            eventos_por_data[data_str] = []
        eventos_por_data[data_str].append(evento)
    
    context = {
        'eventos_por_data': eventos_por_data,
        'mes_atual': hoje.strftime('%B %Y'),
        'hoje': hoje,
    }
    
    return render(request, 'eventos/calendario.html', context)