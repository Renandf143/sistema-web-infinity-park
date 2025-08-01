
#!/usr/bin/env python3
"""
Script simplificado para executar o Infinity Park
"""

import os
import sys
import subprocess

def main():
    print("🎢 INFINITY PARK - INICIANDO SISTEMA 🎢")
    print("=" * 50)
    
    # Ir para o diretório correto
    os.chdir('/home/runner/BookingClone/InfinityPark/WebMola/InfinityPark/DjangoHelloWorld')
    
    # Comandos em sequência
    comandos = [
        ("python manage.py makemigrations", "Criando migrações"),
        ("python manage.py migrate", "Aplicando migrações"),
        ("python manage.py collectstatic --noinput", "Coletando arquivos estáticos"),
        ("python configurar_infinity_park.py", "Configurando sistema completo")
    ]
    
    for comando, descricao in comandos:
        print(f"\n🔧 {descricao}...")
        try:
            subprocess.run(comando, shell=True, check=True)
            print(f"✅ {descricao} - Concluído")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro em {descricao}: {e}")
            continue
    
    print("\n🚀 Sistema pronto! Acesse: http://localhost:5000")

if __name__ == '__main__':
    main()
