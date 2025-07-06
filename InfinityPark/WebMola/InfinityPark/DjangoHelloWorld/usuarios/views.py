from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from atracoes.models import FavoritoUsuario, AvaliacaoAtracao
from eventos.models import EventoFavorito, AvaliacaoEvento
from ingressos.models import Compra
from django.db.models import Count

def login_view(request):
    if request.user.is_authenticated:
        return redirect('atracoes:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'atracoes:home')
            messages.success(request, f'Bem-vindo de volta, {user.get_full_name() or user.username}!')
            return redirect(next_url)
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'usuarios/login.html')

def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('atracoes:home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        # Validações
        if not all([username, email, password1, password2, first_name, last_name]):
            messages.error(request, 'Todos os campos são obrigatórios.')
            return render(request, 'usuarios/cadastro.html')
        
        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'usuarios/cadastro.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Nome de usuário já existe.')
            return render(request, 'usuarios/cadastro.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return render(request, 'usuarios/cadastro.html')
        
        try:
            validate_password(password1)
        except ValidationError as e:
            messages.error(request, f'Senha inválida: {", ".join(e.messages)}')
            return render(request, 'usuarios/cadastro.html')
        
        # Criar usuário
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        
        # Login automático
        login(request, user)
        messages.success(request, 'Conta criada com sucesso! Bem-vindo ao Infinity Park!')
        return redirect('atracoes:home')
    
    return render(request, 'usuarios/cadastro.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você foi desconectado com sucesso.')
    return redirect('atracoes:home')

@login_required
def minha_conta(request):
    # Estatísticas do usuário
    favoritos_atracoes = FavoritoUsuario.objects.filter(usuario=request.user).count()
    favoritos_eventos = EventoFavorito.objects.filter(usuario=request.user).count()
    avaliacoes_atracoes = AvaliacaoAtracao.objects.filter(usuario=request.user).count()
    avaliacoes_eventos = AvaliacaoEvento.objects.filter(usuario=request.user).count()
    
    # Compras de ingressos
    compras = Compra.objects.filter(usuario=request.user).order_by('-data_compra')[:5]
    total_gasto = sum(compra.valor_total for compra in compras)
    
    # Atividades recentes
    atividades_recentes = []
    
    # Favoritos recentes
    favoritos_recentes = FavoritoUsuario.objects.filter(usuario=request.user).order_by('-criado_em')[:3]
    for fav in favoritos_recentes:
        atividades_recentes.append({
            'tipo': 'favorito',
            'descricao': f'Adicionou {fav.atracao.nome} aos favoritos',
            'data': fav.criado_em,
            'icone': 'fas fa-heart'
        })
    
    # Avaliações recentes
    avaliacoes_recentes = AvaliacaoAtracao.objects.filter(usuario=request.user).order_by('-criado_em')[:3]
    for aval in avaliacoes_recentes:
        atividades_recentes.append({
            'tipo': 'avaliacao',
            'descricao': f'Avaliou {aval.atracao.nome} com {aval.nota}★',
            'data': aval.criado_em,
            'icone': 'fas fa-star'
        })
    
    # Ordenar por data
    atividades_recentes.sort(key=lambda x: x['data'], reverse=True)
    
    context = {
        'favoritos_atracoes': favoritos_atracoes,
        'favoritos_eventos': favoritos_eventos,
        'avaliacoes_atracoes': avaliacoes_atracoes,
        'avaliacoes_eventos': avaliacoes_eventos,
        'compras': compras,
        'total_gasto': total_gasto,
        'atividades_recentes': atividades_recentes[:10],
    }
    
    return render(request, 'usuarios/minha_conta.html', context)

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        # Verificar se o email já está em uso por outro usuário
        if User.objects.filter(email=email).exclude(id=request.user.id).exists():
            messages.error(request, 'Este email já está em uso.')
            return render(request, 'usuarios/editar_perfil.html')
        
        # Atualizar dados
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        request.user.save()
        
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('usuarios:minha_conta')
    
    return render(request, 'usuarios/editar_perfil.html')

@login_required
def alterar_senha(request):
    if request.method == 'POST':
        senha_atual = request.POST.get('senha_atual')
        nova_senha = request.POST.get('nova_senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        # Verificar senha atual
        if not request.user.check_password(senha_atual):
            messages.error(request, 'Senha atual incorreta.')
            return render(request, 'usuarios/alterar_senha.html')
        
        # Verificar se as senhas coincidem
        if nova_senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'usuarios/alterar_senha.html')
        
        # Validar nova senha
        try:
            validate_password(nova_senha, request.user)
        except ValidationError as e:
            messages.error(request, f'Senha inválida: {", ".join(e.messages)}')
            return render(request, 'usuarios/alterar_senha.html')
        
        # Alterar senha
        request.user.set_password(nova_senha)
        request.user.save()
        
        messages.success(request, 'Senha alterada com sucesso!')
        return redirect('usuarios:minha_conta')
    
    return render(request, 'usuarios/alterar_senha.html')

@login_required
def minhas_compras(request):
    compras = Compra.objects.filter(usuario=request.user).order_by('-data_compra')
    total_gasto = sum(compra.valor_total for compra in compras)
    
    context = {
        'compras': compras,
        'total_gasto': total_gasto,
    }
    
    return render(request, 'usuarios/minhas_compras.html', context)

def verificar_username(request):
    username = request.GET.get('username')
    if username:
        exists = User.objects.filter(username=username).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})

def verificar_email(request):
    email = request.GET.get('email')
    if email:
        exists = User.objects.filter(email=email).exists()
        return JsonResponse({'exists': exists})
    return JsonResponse({'exists': False})