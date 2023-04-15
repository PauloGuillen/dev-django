from django.shortcuts import render
from pypro.modulos import facede


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facede.listar_modulos_ordenados()})
