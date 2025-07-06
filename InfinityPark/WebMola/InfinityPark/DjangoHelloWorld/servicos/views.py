from django.shortcuts import render
from django.http import HttpResponse

def lista(request):
    return HttpResponse("Lista de Serviços - Em Construção")

def detalhe(request, servico_id):
    return HttpResponse(f"Detalhe do Serviço {servico_id} - Em Construção")

def lista_por_categoria(request, categoria_id):
    return HttpResponse(f"Serviços da Categoria {categoria_id} - Em Construção")

def mapa_servicos(request):
    return HttpResponse("Mapa de Serviços - Em Construção")