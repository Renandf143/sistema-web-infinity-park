
# 🎢 Infinity Park - Parque de Diversões

Sistema completo de gerenciamento de parque de diversões desenvolvido em Django.

## 🚀 Como Executar em Qualquer Plataforma

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### 📥 Instalação Rápida

1. **Clone ou baixe o projeto**
2. **Navegue para o diretório:**
   ```bash
   cd InfinityPark/WebMola/InfinityPark/DjangoHelloWorld
   ```

3. **Execute o script de inicialização:**
   ```bash
   python iniciar_projeto.py
   ```

### 🔧 Instalação Manual

Se preferir executar manualmente:

```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Configurar banco de dados
python manage.py makemigrations
python manage.py migrate

# 3. Coletar arquivos estáticos
python manage.py collectstatic --noinput

# 4. Popular dados do parque (opcional)
python popular_parque_dados.py

# 5. Iniciar servidor
python manage.py runserver 0.0.0.0:8000
```

## 🌐 Acesso ao Sistema

Após inicializar, acesse:
- **Site Principal:** http://localhost:8000
- **Painel Admin:** http://localhost:8000/admin/

### 👤 Credenciais de Acesso
- **Usuário:** admin
- **Senha:** admin123

## 🎯 Funcionalidades

- ✅ **Home Page** com design moderno
- ✅ **15+ Atrações** com detalhes completos
- ✅ **Mapa Interativo** do parque
- ✅ **Sistema de Favoritos** e avaliações
- ✅ **Shows e Eventos** programados
- ✅ **Restaurantes** temáticos
- ✅ **Sistema de Ingressos**
- ✅ **Painel Administrativo** completo
- ✅ **Design Responsivo** (mobile-friendly)

## 📁 Estrutura do Projeto

```
DjangoHelloWorld/
├── atracoes/           # App principal de atrações
├── eventos/            # Shows e espetáculos
├── restaurantes/       # Restaurantes do parque
├── ingressos/          # Sistema de ingressos
├── usuarios/           # Gerenciamento de usuários
├── templates/          # Templates HTML
├── static/             # Arquivos estáticos
├── manage.py           # Comando Django
├── settings.py         # Configurações
└── requirements.txt    # Dependências
```

## 🔧 Solução de Problemas

### Erro de Dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Erro de Banco de Dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### Problemas com Arquivos Estáticos
```bash
python manage.py collectstatic --clear --noinput
```

## 🌟 Características Técnicas

- **Framework:** Django 5.2.4
- **Banco de Dados:** SQLite (padrão)
- **Frontend:** HTML5, CSS3, JavaScript
- **Design:** Inspirado em Disney/Universal
- **Responsivo:** Compatível com mobile

## 📱 Plataformas Testadas

- ✅ Windows 10/11
- ✅ macOS
- ✅ Linux (Ubuntu, CentOS, etc.)
- ✅ VS Code
- ✅ PyCharm
- ✅ Sublime Text
- ✅ Replit
- ✅ CodePen
- ✅ Glitch

## 🎊 Pronto para Produção

O sistema está configurado para ser facilmente implantado em:
- Heroku
- Railway
- PythonAnywhere
- DigitalOcean
- AWS
- Google Cloud

---

**Desenvolvido com 💖 para criar experiências mágicas!**
