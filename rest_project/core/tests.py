import pytest

from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory
from django.urls import resolve
from django.urls import reverse_lazy

from .views import ApplicationSet


@pytest.fixture(scope='module')
def factory():
    return RequestFactory()


@pytest.mark.django_db
@pytest.mark.parametrize(
    'parameters', (
        ('create_api_key', ApplicationSet),
    )
)
def test_ananimus_user_views(parameters, factory):
    """Тест GET запросов по урлам."""
    url, view = parameters
    path = reverse_lazy(url)
    request = factory.get(url)
    request.user = AnonymousUser()
    response = view.as_view()(request)
    assert resolve(path).func.view_class == view
    assert resolve(path).view_name == url
    assert response.status_code == 403
