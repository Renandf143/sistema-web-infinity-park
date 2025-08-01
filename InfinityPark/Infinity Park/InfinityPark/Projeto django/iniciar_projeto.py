
#!/usr/bin/env python3
"""
Script Universal para Iniciar o Infinity Park
Funciona em qualquer plataforma: Windows, Linux, macOS
"""

import os
import sys
import subprocess
import platform

def print_banner():
    print("\n" + "="*60)
    print("🎢 INFINITY PARK - PARQUE DE DIVERSÕES 🎢")
    print("🚀 Script Universal de Inicialização")
    print("💻 Plataforma:", platform.system())
    print("="*60)

def check_python():
    """Verificar versão do Python"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ é necessário!")
        sys.exit(1)
    print(f"✅ Python {sys.version.split()[0]} encontrado")

def install_dependencies():
    """Instalar dependências"""
    print("\n📦 Instalando dependências...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependências instaladas com sucesso!")
    except subprocess.CalledProcessError:
        print("❌ Erro ao instalar dependências")
        sys.exit(1)

def setup_database():
    """Configurar banco de dados"""
    print("\n🗄️ Configurando banco de dados...")
    
    commands = [
        [sys.executable, "manage.py", "makemigrations"],
        [sys.executable, "manage.py", "migrate"],
        [sys.executable, "manage.py", "collectstatic", "--noinput"]
    ]
    
    for cmd in commands:
        try:
            subprocess.run(cmd, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao executar: {' '.join(cmd)}")
            print(f"Erro: {e}")

def populate_data():
    """Popular dados do parque"""
    print("\n🎢 Populando dados do parque...")
    if os.path.exists("popular_parque_dados.py"):
        try:
            subprocess.run([sys.executable, "popular_parque_dados.py"], check=True)
            print("✅ Dados do parque carregados!")
        except subprocess.CalledProcessError:
            print("⚠️ Aviso: Erro ao popular dados, continuando...")

def start_server():
    """Iniciar servidor Django"""
    print("\n🚀 INICIANDO SERVIDOR DO INFINITY PARK")
    print("-" * 50)
    print("🌐 Acesse o projeto em:")
    print("   • http://localhost:8000")
    print("   • http://127.0.0.1:8000")
    print("\n👤 Admin:")
    print("   • URL: http://localhost:8000/admin/")
    print("   • Usuário: admin")
    print("   • Senha: admin123")
    print("\n⚡ Pressione Ctrl+C para parar")
    print("-" * 50)
    
    try:
        subprocess.run([sys.executable, "manage.py", "runserver", "0.0.0.0:8000"])
    except KeyboardInterrupt:
        print("\n🛑 Servidor finalizado!")

def main():
    print_banner()
    
    # Verificar se está no diretório correto
    if not os.path.exists("manage.py"):
        print("❌ Arquivo manage.py não encontrado!")
        print("💡 Execute este script no diretório do Django")
        sys.exit(1)
    
    check_python()
    install_dependencies()
    setup_database()
    populate_data()
    start_server()

if __name__ == "__main__":
    main()
