
# 🎢 Infinity Park

Bem-vindo ao meu parque de diversões virtual! Criei este projeto como uma forma de aprender Django e me divertir no processo.

## Como rodar

Você vai precisar do Python instalado (versão 3.8+). Se não tem, baixa do site oficial.

### Jeito rápido

1. Baixa o projeto
2. Vai na pasta:
   ```bash
   cd InfinityPark/WebMola/InfinityPark/DjangoHelloWorld
   ```

3. Roda o script que fiz:
   ```bash
   python iniciar_projeto.py
   ```

### Se quiser fazer na mão

Caso prefira fazer passo a passo:

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput
python popular_parque_dados.py  # isso aqui popula com dados legais
python manage.py runserver 0.0.0.0:8000
```

## Acessando

Depois que rodar, vai em:
- Site: http://localhost:8000
- Admin: http://localhost:8000/admin/

**Login:** admin / admin123

## O que tem no projeto

Consegui implementar bastante coisa:
- Home page que ficou bem legal
- Umas 15 atrações diferentes (peguei inspiração na Disney)
- Mapa interativo (demorei pra fazer funcionar)
- Sistema de favoritos
- Shows e eventos
- Área de restaurantes
- Compra de ingressos
- Painel admin completo
- Responsivo (funciona no celular)

## Como está organizado

```
DjangoHelloWorld/
├── atracoes/           # onde ficam as atrações
├── eventos/            # shows e eventos
├── restaurantes/       # comidas do parque
├── ingressos/          # vendas de ingresso
├── usuarios/           # cadastro e login
├── templates/          # páginas HTML
├── static/             # CSS, JS, imagens
└── manage.py           # arquivo principal do Django
```

## Se der problema

### Erro nas dependências
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Banco de dados bugou
```bash
python manage.py makemigrations
python manage.py migrate
```

### CSS não carrega
```bash
python manage.py collectstatic --clear --noinput
```

## Stack técnica

Usei Django 5.2.4 com SQLite. Frontend é HTML/CSS/JS básico mesmo, mas tentei deixar bonito inspirado nos parques da Disney.

## Onde testei

Rodei em Windows, Mac e Linux. Funciona no VS Code, PyCharm e até no Replit.

## Deploy

Se quiser colocar online, funciona no Heroku, Railway, PythonAnywhere... qualquer lugar que rode Django.

---

*Projeto feito com muito café e nostalgia dos parques da Disney! 🎢☕*

**PS:** Se encontrar algum bug, me manda um email ou abre uma issue. Ainda tô aprendendo Django então qualquer feedback é bem-vindo!
