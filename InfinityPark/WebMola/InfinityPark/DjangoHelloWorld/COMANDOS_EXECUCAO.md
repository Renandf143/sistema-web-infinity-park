# Comandos para Executar o Infinity Park

## Comandos Básicos para Iniciar o Site

### 1. Navegar para o diretório do projeto
```bash
cd WebMola/InfinityPark/DjangoHelloWorld
```

### 2. Executar as migrações do banco de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Coletar arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

### 4. Popular o banco de dados com dados iniciais (OPCIONAL)
```bash
python manage.py shell < criar_dados_iniciais.py
```

### 5. Executar o servidor de desenvolvimento
```bash
python manage.py runserver 0.0.0.0:5000
```

## Comandos Completos em Sequência

Execute todos os comandos em sequência para garantir que tudo funcione:

```bash
# Navegar para o diretório
cd WebMola/InfinityPark/DjangoHelloWorld

# Configurar banco de dados
python manage.py makemigrations
python manage.py migrate

# Arquivos estáticos
python manage.py collectstatic --noinput

# Popular dados (opcional)
python manage.py shell < criar_dados_iniciais.py

# Executar servidor
python manage.py runserver 0.0.0.0:5000
```

## Acesso ao Site

Após executar os comandos, o site estará disponível em:
- **URL Local**: http://localhost:5000
- **URL Replit**: https://seu-projeto.replit.dev

## Funcionalidades Disponíveis

- ✅ **Página Principal**: Home com navegação completa
- ✅ **Atrações**: Lista e detalhes das atrações
- ✅ **Shows e Eventos**: Lista de shows e espetáculos
- ✅ **Restaurantes**: Lista de restaurantes
- ✅ **Hotéis**: Lista e detalhes dos hotéis
- ✅ **Ingressos**: Sistema de compra de ingressos
- ✅ **Cadastro/Login**: Sistema de usuários
- ✅ **Mapa**: Mapa do parque
- ✅ **Administração**: Painel administrativo

## Solução de Problemas

### Se aparecer erro de template:
```bash
python manage.py collectstatic --noinput
```

### Se aparecer erro de banco de dados:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Se não aparecer dados no site:
```bash
python manage.py shell < criar_dados_iniciais.py
```

## Observações Importantes

- O site usa **PostgreSQL** como banco de dados
- Todas as imagens são **SVG** geradas automaticamente
- O logo correto do **Infinity Park** está configurado
- Todas as páginas de **Shows e Eventos** funcionam corretamente
- O sistema está pronto para **produção**