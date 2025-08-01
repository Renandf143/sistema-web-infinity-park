# 🎢 Sistema Web Infinity Park

Sistema completo de gerenciamento para parque de diversões desenvolvido em Django.

## 🎯 Sobre o Projeto

O Infinity Park é um sistema web completo para gerenciamento de parques de diversões, inspirado nos grandes parques temáticos como Disney e Universal. O sistema oferece uma experiência completa tanto para visitantes quanto para administradores.

## ✨ Funcionalidades

### Para Visitantes
- 🏠 **Página Principal** com design moderno e responsivo
- 🎢 **Catálogo de Atrações** com detalhes completos
- 🗺️ **Mapa Interativo** do parque
- ⭐ **Sistema de Avaliações** das atrações
- ❤️ **Lista de Favoritos** personalizada
- 🎭 **Shows e Eventos** programados
- 🍽️ **Restaurantes Temáticos**
- 🏨 **Hotéis e Hospedagem**
- 🎫 **Sistema de Ingressos** online
- 👤 **Cadastro e Login** de usuários

### Para Administradores
- 🔧 **Painel Administrativo** completo
- 📊 **Gerenciamento de Atrações**
- 🎪 **Controle de Eventos**
- 👥 **Gestão de Usuários**
- 📈 **Relatórios e Analytics**

## 🛠️ Tecnologias Utilizadas

- **Backend**: Django 5.2.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Banco de Dados**: SQLite (desenvolvimento)
- **Imagens**: Pillow
- **Configuração**: python-decouple
- **Arquivos Estáticos**: whitenoise
- **Deploy**: Gunicorn

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/Renandf143/sistema-web-infinity-park.git
cd sistema-web-infinity-park
```

2. **Navegue para o diretório do projeto Django**
```bash
cd "InfinityPark/Infinity Park/InfinityPark/Projeto django"
```

3. **Instale as dependências**
```bash
pip install -r requirements.txt
```

4. **Execute o script de configuração automática**
```bash
python executar_infinity_park.py
```

O script irá:
- ✅ Verificar dependências
- 🗄️ Configurar o banco de dados
- 📊 Popular com dados iniciais
- 🎨 Coletar arquivos estáticos
- 👤 Criar usuário administrador
- 🚀 Iniciar o servidor

### Acesso ao Sistema

Após a execução, o sistema estará disponível em:
- **Site Principal**: http://localhost:5000
- **Painel Admin**: http://localhost:5000/admin/

**Credenciais de Administrador:**
- Usuário: `admin`
- Senha: `admin123`

## 📁 Estrutura do Projeto

```
InfinityPark/
├── administracao/          # App de administração
├── atracoes/              # App de atrações do parque
├── eventos/               # App de shows e eventos
├── hoteis/                # App de hospedagem
├── ingressos/             # App de sistema de ingressos
├── paginas/               # Páginas estáticas
├── restaurantes/          # App de restaurantes
├── servicos/              # App de serviços gerais
├── usuarios/              # App de gerenciamento de usuários
├── templates/             # Templates HTML
├── static/                # Arquivos estáticos (CSS, JS, imagens)
├── staticfiles/           # Arquivos estáticos coletados
└── manage.py              # Script de gerenciamento Django
```

## 🎨 Design e Interface

O sistema possui uma interface moderna e responsiva, otimizada para:
- 💻 **Desktop** - Experiência completa
- 📱 **Mobile** - Interface adaptada para dispositivos móveis
- 🎨 **Tema Parque** - Visual inspirado em grandes parques temáticos

## 🔧 Scripts Disponíveis

- `executar_infinity_park.py` - Script principal de execução
- `executar_sistema.py` - Script simplificado
- `configurar_infinity_park.py` - Configuração do sistema
- `popular_parque_dados.py` - População de dados iniciais
- `criar_dados_iniciais.py` - Criação de dados base

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 👨‍💻 Desenvolvedor

Desenvolvido por **Renan Gomes Lobo**

### 🌐 Redes Sociais
- 📱 **Instagram**: [@renan.gomeslobo](https://instagram.com/renan.gomeslobo)
- 💻 **GitHub**: [@Renandf143](https://github.com/Renandf143)

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para:
1. Fazer um Fork do projeto
2. Criar uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abrir um Pull Request

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas, abra uma [issue](https://github.com/Renandf143/sistema-web-infinity-park/issues) no GitHub.

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no repositório!**