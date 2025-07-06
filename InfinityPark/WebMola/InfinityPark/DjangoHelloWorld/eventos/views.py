from django.shortcuts import render
from django.http import HttpResponse

def lista(request):
    return HttpResponse("Lista de Eventos - Em Construção")

def detalhe(request, evento_id):
    return HttpResponse(f"Detalhe do Evento {evento_id} - Em Construção")

def lista_por_categoria(request, categoria_id):
    return HttpResponse(f"Eventos da Categoria {categoria_id} - Em Construção")

def eventos_hoje(request):
    return HttpResponse("Eventos de Hoje - Em Construção")

def calendario(request):
    return HttpResponse("Calendário de Eventos - Em Construção")