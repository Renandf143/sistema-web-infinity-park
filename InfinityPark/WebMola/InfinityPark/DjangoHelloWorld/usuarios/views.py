from django.shortcuts import render
from django.http import HttpResponse

def login_view(request):
    return HttpResponse("Login - Em Construção")

def logout_view(request):
    return HttpResponse("Logout - Em Construção")

def cadastro(request):
    return HttpResponse("Cadastro - Em Construção")

def perfil(request):
    return HttpResponse("Perfil do Usuário - Em Construção")

def editar_perfil(request):
    return HttpResponse("Editar Perfil - Em Construção")