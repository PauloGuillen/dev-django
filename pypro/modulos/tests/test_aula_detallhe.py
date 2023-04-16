from django.urls import reverse
from pypro.django_assertions import assert_contains
import pytest
from model_bakery import baker
from pypro.modulos.models import Modulo,  Aula


@pytest.fixture
def modulo(db):
    return baker.make(Modulo)


@pytest.fixture
def aula(modulo):
    return baker.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulo(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_vimeo_id(resp, aula: Aula):
    assert_contains(resp, f'https://player.vimeo.com/video/{ aula.vimeo_id }')
