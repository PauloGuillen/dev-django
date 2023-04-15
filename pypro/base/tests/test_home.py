from django.urls import reverse
from pypro.django_assertions import assert_contains
import pytest


@pytest.fixture
def resp(client, db):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Python Pro - home</title>')


def test_email_link(resp):
    assert_contains(resp, 'href="mailto:ramalho@python.pro.br"')
