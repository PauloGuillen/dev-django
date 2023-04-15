from pypro.modulos import facede


def listar_modulos(request):
    return {'MODULOS': facede.listar_modulos_ordenados()}
