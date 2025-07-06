#!/usr/bin/env python3
"""
Script para executar o Infinity Park Django - Parque de Diversões
"""

import os
import sys
import subprocess
import time

def print_header():
    """Mostrar header do Infinity Park"""
    print("\n" + "="*60)
    print("🎢 INFINITY PARK - PARQUE DE DIVERSÕES 🎢")
    print("🎠 Sistema de Gerenciamento Completo 🎠")
    print("="*60)

def execute_command(command, description):
    """Executar comando com descrição"""
    print(f"\n🔧 {description}...")
    print(f"💻 Executando: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        if result.stdout:
            print("✅ Sucesso!")
            if "migrate" in command.lower():
                print(f"📊 Saída: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro: {e}")
        if e.stderr:
            print(f"🚨 Detalhes: {e.stderr}")
        return False

def check_requirements():
    """Verificar se o Django está instalado"""
    try:
        import django
        print(f"✅ Django {django.get_version()} encontrado")
        return True
    except ImportError:
        print("❌ Django não encontrado. Instalando...")
        return execute_command("pip install django", "Instalando Django")

def setup_database():
    """Configurar banco de dados"""
    print("\n📊 CONFIGURANDO BANCO DE DADOS")
    print("-" * 40)
    
    # Fazer migrações
    if not execute_command("python manage.py makemigrations", "Criando migrações"):
        return False
    
    # Aplicar migrações
    if not execute_command("python manage.py migrate", "Aplicando migrações"):
        return False
    
    return True

def populate_database():
    """Popular banco com dados do parque"""
    print("\n🎢 POPULANDO BANCO COM DADOS DO PARQUE")
    print("-" * 40)
    
    if os.path.exists("popular_parque_dados.py"):
        return execute_command("python popular_parque_dados.py", 
                             "Criando atrações, áreas e serviços")
    else:
        print("⚠️ Arquivo de dados não encontrado, continuando...")
        return True

def collect_static():
    """Coletar arquivos estáticos"""
    print("\n🎨 COLETANDO ARQUIVOS ESTÁTICOS")
    print("-" * 40)
    
    return execute_command("python manage.py collectstatic --noinput", 
                         "Coletando CSS, JS e imagens")

def create_superuser():
    """Criar superusuário se não existir"""
    print("\n👤 VERIFICANDO USUÁRIO ADMINISTRADOR")
    print("-" * 40)
    
    try:
        # Verificar se já existe superuser
        result = subprocess.run(
            'python manage.py shell -c "from django.contrib.auth.models import User; print(User.objects.filter(is_superuser=True).exists())"',
            shell=True, capture_output=True, text=True
        )
        
        if "True" in result.stdout:
            print("✅ Usuário administrador já existe")
            print("🔑 Login: admin / Senha: admin123")
            return True
        else:
            print("⚠️ Usuário administrador será criado pelo script de dados")
            return True
            
    except Exception as e:
        print(f"⚠️ Erro ao verificar usuário: {e}")
        return True

def start_server():
    """Iniciar servidor Django"""
    print("\n🚀 INICIANDO SERVIDOR DO INFINITY PARK")
    print("-" * 40)
    print("🌐 O Infinity Park estará disponível em:")
    print("   • http://localhost:5000")
    print("   • http://0.0.0.0:5000")
    print("\n📋 Acesso Admin:")
    print("   • URL: http://localhost:5000/admin/")
    print("   • Usuário: admin")
    print("   • Senha: admin123")
    print("\n⚡ Pressione Ctrl+C para parar o servidor")
    print("-" * 40)
    
    try:
        subprocess.run("python manage.py runserver 0.0.0.0:5000", shell=True)
    except KeyboardInterrupt:
        print("\n\n🛑 Servidor parado pelo usuário")
        print("🎢 Obrigado por usar o Infinity Park!")

def show_features():
    """Mostrar funcionalidades disponíveis"""
    print("\n🎯 FUNCIONALIDADES DISPONÍVEIS")
    print("-" * 40)
    features = [
        "🏠 Página Principal com design moderno",
        "🎢 Atrações com detalhes completos",
        "🗺️ Mapa interativo do parque",
        "⭐ Sistema de avaliações",
        "❤️ Favoritos dos usuários", 
        "🎭 Shows e eventos",
        "🍽️ Restaurantes temáticos",
        "🏨 Hotéis e hospedagem",
        "🎫 Sistema de ingressos",
        "👥 Gerenciamento de usuários",
        "🔧 Painel administrativo completo",
        "📱 Design responsivo (mobile-friendly)",
        "🎨 Interface similar a Disney/Universal"
    ]
    
    for feature in features:
        print(f"   {feature}")

def main():
    """Função principal"""
    print_header()
    
    # Verificar diretório
    if not os.path.exists("manage.py"):
        print("❌ Erro: Execute este script no diretório do Django!")
        print("💡 Navegue para: InfinityPark/WebMola/InfinityPark/DjangoHelloWorld/")
        sys.exit(1)
    
    # Verificar requirements
    if not check_requirements():
        sys.exit(1)
    
    # Configurar tudo
    steps = [
        (setup_database, "Configuração do banco de dados"),
        (populate_database, "População com dados do parque"), 
        (collect_static, "Coleta de arquivos estáticos"),
        (create_superuser, "Verificação de usuário admin")
    ]
    
    for step_func, step_name in steps:
        if not step_func():
            print(f"\n❌ Falha na etapa: {step_name}")
            print("🔧 Verifique os erros acima e tente novamente")
            sys.exit(1)
    
    # Mostrar funcionalidades
    show_features()
    
    # Aguardar confirmação para iniciar
    print("\n" + "="*60)
    print("✅ INFINITY PARK CONFIGURADO COM SUCESSO!")
    print("="*60)
    
    input("\n🚀 Pressione ENTER para iniciar o servidor...")
    
    # Iniciar servidor
    start_server()

if __name__ == "__main__":
    main()