from django.shortcuts import render

def sobre_nos(request):
    """Página Sobre Nós"""
    context = {
        'titulo': 'Sobre o Infinity Park',
        'descricao': 'Conheça a história e a magia por trás do parque de diversões mais incrível do Brasil.'
    }
    return render(request, 'paginas/sobre_nos.html', context)

def termos_uso(request):
    """Página Termos de Uso"""
    context = {
        'titulo': 'Termos de Uso',
        'descricao': 'Leia nossos termos e condições de uso do Infinity Park.'
    }
    return render(request, 'paginas/termos_uso.html', context)

def politica_privacidade(request):
    """Página Política de Privacidade"""
    context = {
        'titulo': 'Política de Privacidade',
        'descricao': 'Saiba como protegemos seus dados pessoais no Infinity Park.'
    }
    return render(request, 'paginas/politica_privacidade.html', context)

def faq(request):
    """Página de Perguntas Frequentes"""
    
    # Perguntas frequentes organizadas por categoria
    perguntas_frequentes = {
        'Ingressos': [
            {
                'pergunta': 'Como posso comprar meus ingressos?',
                'resposta': 'Você pode comprar ingressos online em nosso site, no app oficial ou na bilheteria do parque. Recomendamos a compra antecipada para garantir sua entrada e aproveitar descontos especiais.'
            },
            {
                'pergunta': 'Crianças precisam de ingresso?',
                'resposta': 'Crianças de 0 a 2 anos não pagam ingresso. Crianças de 3 a 12 anos pagam meia-entrada. É necessário apresentar documento comprobatório de idade.'
            },
            {
                'pergunta': 'Posso cancelar ou alterar meu ingresso?',
                'resposta': 'Sim, você pode cancelar ou alterar seu ingresso até 24 horas antes da data da visita. Acesse sua conta no site ou entre em contato conosco.'
            }
        ],
        'Atrações': [
            {
                'pergunta': 'Qual a altura mínima para as atrações?',
                'resposta': 'Cada atração tem sua própria restrição de altura por segurança. Verifique as informações específicas de cada atração em nosso site ou no parque.'
            },
            {
                'pergunta': 'O que é o Fast Pass?',
                'resposta': 'O Fast Pass é um sistema que permite furar a fila em atrações selecionadas. Está disponível para ingressos VIP ou pode ser adquirido separadamente.'
            }
        ],
        'Visitação': [
            {
                'pergunta': 'Qual o horário de funcionamento?',
                'resposta': 'O parque funciona de terça a domingo, das 9h às 22h. Segundas-feiras o parque está fechado para manutenção, exceto em feriados.'
            },
            {
                'pergunta': 'O parque é acessível para pessoas com deficiência?',
                'resposta': 'Sim, o Infinity Park é totalmente acessível. Oferecemos cadeiras de rodas gratuitas, elevadores, rampas e atrações adaptadas.'
            }
        ]
    }
    
    context = {
        'titulo': 'Perguntas Frequentes',
        'descricao': 'Encontre respostas para as dúvidas mais comuns sobre o Infinity Park.',
        'perguntas_frequentes': perguntas_frequentes
    }
    return render(request, 'paginas/faq.html', context)