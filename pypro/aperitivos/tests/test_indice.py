from django.urls import reverse
import pytest
from pypro.django_assertions import assert_contains
from model_bakery import baker
from ..models import Video


@pytest.fixture
def videos(db):
    return baker.make(Video, 3)


@pytest.fixture
def resp(client, videos):
    return client.get(reverse('aperitivos:indice'))


def test_status_code(resp):
    assert resp.status_code == 200


def test_titulo_video(resp, videos):
    for video in videos:
        assert_contains(resp, video.titulo)


def test_link_video(resp, videos):
    for video in videos:
        link_video = reverse('aperitivos:video', args=(video.slug,))
        assert_contains(resp, f'href="{ link_video }"')
