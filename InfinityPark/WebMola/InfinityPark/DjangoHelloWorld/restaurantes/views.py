from django.shortcuts import render
from django.http import HttpResponse

def lista(request):
    return HttpResponse("Lista de Restaurantes - Em Construção")

def detalhe(request, restaurante_id):
    return HttpResponse(f"Detalhe do Restaurante {restaurante_id} - Em Construção")

def lista_por_categoria(request, categoria_id):
    return HttpResponse(f"Restaurantes da Categoria {categoria_id} - Em Construção")

def lista_por_area(request, area_id):
    return HttpResponse(f"Restaurantes da Área {area_id} - Em Construção")

def cardapio(request, restaurante_id):
    return HttpResponse(f"Cardápio do Restaurante {restaurante_id} - Em Construção")