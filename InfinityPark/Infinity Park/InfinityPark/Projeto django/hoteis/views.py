from django.shortcuts import render
from django.http import HttpResponse

def lista(request):
    return HttpResponse("Lista de Hotéis - Em Construção")

def detalhe(request, hotel_id):
    return HttpResponse(f"Detalhe do Hotel {hotel_id} - Em Construção")

def lista_por_categoria(request, categoria_id):
    return HttpResponse(f"Hotéis da Categoria {categoria_id} - Em Construção")

def reservas(request):
    return HttpResponse("Minhas Reservas - Em Construção")

def reservar(request, hotel_id):
    return HttpResponse(f"Reservar Hotel {hotel_id} - Em Construção")