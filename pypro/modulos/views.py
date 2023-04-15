from django.shortcuts import render
from pypro.modulos import facede


def detalhe(request, slug):
    modulo = facede.encontrar_modulo(slug)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo})
