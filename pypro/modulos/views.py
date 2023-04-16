from django.shortcuts import render
from pypro.modulos import facede


def detalhe(request, slug):
    modulo = facede.encontrar_modulo(slug)
    aulas = facede.listar_aulas_de_modulos_ordenadas(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})


def aula(request, slug):
    aula = facede.encontrar_aula(slug)
    return render(request, 'modulos/aula_detalhe.html', {'aula': aula})
