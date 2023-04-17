import pytest
from model_bakery import baker
# from pypro.modulos import facede
from pypro.modulos.models import Modulo


@pytest.fixture
def modulos(db):
    return [baker.make(Modulo, titulo=s) for s in 'Depois Antes'.split()]


"""
def test_listar_modulos_ordenados(modulos):
    assert list(sorted(modulos, key=lambda modulo: modulo.titulo)) == facede.listar_modulos_ordenados()
"""
