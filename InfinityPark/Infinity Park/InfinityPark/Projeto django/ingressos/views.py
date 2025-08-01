from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from django.db import transaction
from .models import TipoIngresso, Promocao, Compra, ItemCompra, Ingresso
from decimal import Decimal
import json

def lista_ingressos(request):
    """Lista todos os tipos de ingressos disponíveis"""
    tipos_ingresso = TipoIngresso.objects.filter(ativo=True).order_by('preco')
    promocoes_ativas = Promocao.objects.filter(
        ativo=True,
        data_inicio__lte=timezone.now(),
        data_fim__gte=timezone.now()
    )
    
    context = {
        'tipos_ingresso': tipos_ingresso,
        'promocoes_ativas': promocoes_ativas,
        'titulo': 'Ingressos do Infinity Park',
        'descricao': 'Escolha seu ingresso e venha viver momentos mágicos no parque!'
    }
    
    return render(request, 'ingressos/lista.html', context)

def detalhe_ingresso(request, id):
    """Detalhe de um tipo específico de ingresso"""
    tipo_ingresso = get_object_or_404(TipoIngresso, id=id, ativo=True)
    promocoes_aplicaveis = Promocao.objects.filter(
        ativo=True,
        data_inicio__lte=timezone.now(),
        data_fim__gte=timezone.now(),
        tipos_aplicaveis=tipo_ingresso
    )
    
    context = {
        'tipo_ingresso': tipo_ingresso,
        'promocoes_aplicaveis': promocoes_aplicaveis,
    }
    
    return render(request, 'ingressos/detalhe.html', context)

@login_required
def carrinho(request):
    """Carrinho de compras - sessão temporária"""
    carrinho_items = request.session.get('carrinho', {})
    
    # Calcular totais
    subtotal = Decimal('0.00')
    items_carrinho = []
    
    for tipo_id, quantidade in carrinho_items.items():
        try:
            tipo_ingresso = TipoIngresso.objects.get(id=tipo_id, ativo=True)
            total_item = tipo_ingresso.preco * quantidade
            subtotal += total_item
            
            items_carrinho.append({
                'tipo_ingresso': tipo_ingresso,
                'quantidade': quantidade,
                'total': total_item
            })
        except TipoIngresso.DoesNotExist:
            continue
    
    # Verificar promoções aplicáveis
    promocoes = Promocao.objects.filter(
        ativo=True,
        data_inicio__lte=timezone.now(),
        data_fim__gte=timezone.now(),
        valor_minimo__lte=subtotal
    )
    
    context = {
        'items_carrinho': items_carrinho,
        'subtotal': subtotal,
        'promocoes': promocoes,
        'titulo': 'Seu Carrinho'
    }
    
    return render(request, 'ingressos/carrinho.html', context)

@login_required
def adicionar_carrinho(request):
    """Adicionar item ao carrinho via AJAX"""
    if request.method == 'POST':
        tipo_id = request.POST.get('tipo_id')
        quantidade = int(request.POST.get('quantidade', 1))
        
        try:
            tipo_ingresso = TipoIngresso.objects.get(id=tipo_id, ativo=True)
            carrinho = request.session.get('carrinho', {})
            
            if tipo_id in carrinho:
                carrinho[tipo_id] += quantidade
            else:
                carrinho[tipo_id] = quantidade
            
            request.session['carrinho'] = carrinho
            request.session.modified = True
            
            # Calcular novo total do carrinho
            total_items = sum(carrinho.values())
            
            return JsonResponse({
                'success': True,
                'message': f'{tipo_ingresso.nome} adicionado ao carrinho!',
                'total_items': total_items
            })
            
        except TipoIngresso.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Tipo de ingresso inválido!'
            })
    
    return JsonResponse({'success': False})

@login_required
def remover_carrinho(request):
    """Remover item do carrinho via AJAX"""
    if request.method == 'POST':
        tipo_id = request.POST.get('tipo_id')
        carrinho = request.session.get('carrinho', {})
        
        if tipo_id in carrinho:
            del carrinho[tipo_id]
            request.session['carrinho'] = carrinho
            request.session.modified = True
            
            return JsonResponse({
                'success': True,
                'message': 'Item removido do carrinho!'
            })
    
    return JsonResponse({'success': False})

@login_required
def aplicar_promocao(request):
    """Aplicar código promocional via AJAX"""
    if request.method == 'POST':
        codigo = request.POST.get('codigo').upper()
        
        try:
            promocao = Promocao.objects.get(
                codigo=codigo,
                ativo=True,
                data_inicio__lte=timezone.now(),
                data_fim__gte=timezone.now()
            )
            
            if not promocao.pode_usar(request.user):
                return JsonResponse({
                    'success': False,
                    'message': 'Você já utilizou esta promoção o máximo de vezes permitido!'
                })
            
            # Calcular desconto
            carrinho = request.session.get('carrinho', {})
            subtotal = Decimal('0.00')
            
            for tipo_id, quantidade in carrinho.items():
                tipo_ingresso = TipoIngresso.objects.get(id=tipo_id)
                subtotal += tipo_ingresso.preco * quantidade
            
            if subtotal < promocao.valor_minimo:
                return JsonResponse({
                    'success': False,
                    'message': f'Valor mínimo para esta promoção é R$ {promocao.valor_minimo}'
                })
            
            if promocao.tipo_desconto == 'percentual':
                desconto = subtotal * (promocao.valor_desconto / 100)
            else:
                desconto = promocao.valor_desconto
            
            total = subtotal - desconto
            
            # Salvar promoção na sessão
            request.session['promocao_aplicada'] = {
                'id': promocao.id,
                'codigo': promocao.codigo,
                'desconto': float(desconto),
                'total': float(total)
            }
            request.session.modified = True
            
            return JsonResponse({
                'success': True,
                'message': f'Promoção {promocao.nome} aplicada!',
                'desconto': float(desconto),
                'total': float(total)
            })
            
        except Promocao.DoesNotExist:
            return JsonResponse({
                'success': False,
                'message': 'Código promocional inválido ou expirado!'
            })
    
    return JsonResponse({'success': False})

@login_required
def checkout(request):
    """Finalizar compra"""
    carrinho = request.session.get('carrinho', {})
    
    if not carrinho:
        messages.error(request, 'Seu carrinho está vazio!')
        return redirect('ingressos:lista')
    
    if request.method == 'POST':
        try:
            with transaction.atomic():
                # Calcular valores
                subtotal = Decimal('0.00')
                items = []
                
                for tipo_id, quantidade in carrinho.items():
                    tipo_ingresso = TipoIngresso.objects.get(id=tipo_id, ativo=True)
                    total_item = tipo_ingresso.preco * quantidade
                    subtotal += total_item
                    items.append({
                        'tipo': tipo_ingresso,
                        'quantidade': quantidade,
                        'total': total_item
                    })
                
                # Aplicar promoção se houver
                promocao_data = request.session.get('promocao_aplicada')
                promocao = None
                desconto = Decimal('0.00')
                
                if promocao_data:
                    promocao = Promocao.objects.get(id=promocao_data['id'])
                    desconto = Decimal(str(promocao_data['desconto']))
                
                total = subtotal - desconto
                
                # Criar compra
                compra = Compra.objects.create(
                    usuario=request.user,
                    valor_subtotal=subtotal,
                    valor_desconto=desconto,
                    valor_total=total,
                    promocao=promocao,
                    codigo_promocional=promocao.codigo if promocao else '',
                    nome_completo=request.POST.get('nome_completo'),
                    cpf=request.POST.get('cpf'),
                    email=request.POST.get('email'),
                    telefone=request.POST.get('telefone'),
                    status='confirmado'
                )
                
                # Criar itens da compra
                for item in items:
                    ItemCompra.objects.create(
                        compra=compra,
                        tipo_ingresso=item['tipo'],
                        quantidade=item['quantidade'],
                        preco_unitario=item['tipo'].preco,
                        preco_total=item['total']
                    )
                
                # Criar ingressos individuais
                visitantes = json.loads(request.POST.get('visitantes', '[]'))
                
                for i, item in enumerate(items):
                    for j in range(item['quantidade']):
                        visitante_index = sum(prev_item['quantidade'] for prev_item in items[:i]) + j
                        visitante = visitantes[visitante_index] if visitante_index < len(visitantes) else {}
                        
                        # Data de validade baseada no tipo de ingresso
                        data_validade = timezone.now() + timezone.timedelta(days=item['tipo'].validade_dias)
                        
                        Ingresso.objects.create(
                            compra=compra,
                            tipo_ingresso=item['tipo'],
                            usuario=request.user,
                            data_validade=data_validade,
                            nome_visitante=visitante.get('nome', request.user.get_full_name()),
                            cpf_visitante=visitante.get('cpf', ''),
                            idade=visitante.get('idade')
                        )
                
                # Atualizar uso da promoção
                if promocao:
                    promocao.quantidade_usada += 1
                    promocao.save()
                
                # Limpar carrinho e promoção da sessão
                del request.session['carrinho']
                if 'promocao_aplicada' in request.session:
                    del request.session['promocao_aplicada']
                request.session.modified = True
                
                messages.success(request, f'Compra realizada com sucesso! Código: {compra.codigo}')
                return redirect('ingressos:compra_sucesso', codigo=compra.codigo)
                
        except Exception as e:
            messages.error(request, f'Erro ao processar compra: {str(e)}')
    
    # Preparar dados para o formulário
    items_carrinho = []
    subtotal = Decimal('0.00')
    
    for tipo_id, quantidade in carrinho.items():
        tipo_ingresso = TipoIngresso.objects.get(id=tipo_id)
        total_item = tipo_ingresso.preco * quantidade
        subtotal += total_item
        items_carrinho.append({
            'tipo_ingresso': tipo_ingresso,
            'quantidade': quantidade,
            'total': total_item
        })
    
    promocao_data = request.session.get('promocao_aplicada')
    desconto = Decimal(str(promocao_data['desconto'])) if promocao_data else Decimal('0.00')
    total = subtotal - desconto
    
    context = {
        'items_carrinho': items_carrinho,
        'subtotal': subtotal,
        'desconto': desconto,
        'total': total,
        'promocao_data': promocao_data,
        'titulo': 'Finalizar Compra'
    }
    
    return render(request, 'ingressos/checkout.html', context)

def compra_sucesso(request, codigo):
    """Página de sucesso da compra"""
    compra = get_object_or_404(Compra, codigo=codigo)
    
    # Verificar se o usuário tem permissão para ver esta compra
    if request.user.is_authenticated and compra.usuario != request.user:
        if not request.user.is_staff:
            messages.error(request, 'Você não tem permissão para ver esta compra.')
            return redirect('ingressos:lista')
    
    context = {
        'compra': compra,
        'titulo': 'Compra Realizada com Sucesso!'
    }
    
    return render(request, 'ingressos/compra_sucesso.html', context)

@login_required
def meus_ingressos(request):
    """Lista os ingressos do usuário"""
    ingressos = Ingresso.objects.filter(usuario=request.user).order_by('-data_validade')
    
    context = {
        'ingressos': ingressos,
        'titulo': 'Meus Ingressos'
    }
    
    return render(request, 'ingressos/meus_ingressos.html', context)

def verificar_promocao(request):
    """Verificar se código promocional é válido via AJAX"""
    codigo = request.GET.get('codigo', '').upper()
    
    try:
        promocao = Promocao.objects.get(
            codigo=codigo,
            ativo=True,
            data_inicio__lte=timezone.now(),
            data_fim__gte=timezone.now()
        )
        
        return JsonResponse({
            'valido': True,
            'nome': promocao.nome,
            'descricao': promocao.descricao,
            'tipo_desconto': promocao.tipo_desconto,
            'valor_desconto': float(promocao.valor_desconto),
            'valor_minimo': float(promocao.valor_minimo)
        })
        
    except Promocao.DoesNotExist:
        return JsonResponse({'valido': False})