from django.shortcuts import render
from django.http import HttpResponse

def lista(request):
    return HttpResponse("Lista de Ingressos - Em Construção")

def comprar(request):
    return HttpResponse("Comprar Ingressos - Em Construção")

def meus_ingressos(request):
    return HttpResponse("Meus Ingressos - Em Construção")

def validar(request, codigo):
    return HttpResponse(f"Validar Ingresso {codigo} - Em Construção")

def lista_por_categoria(request, categoria_id):
    return HttpResponse(f"Ingressos da Categoria {categoria_id} - Em Construção")