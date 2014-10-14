from django.core.urlresolvers import resolve
from django.contrib.auth.views import login
from .views import Home

def test_root_url_resolves_to_home_view():
    found = resolve("/")
    assert found.view_name == "home"

def test_home_view_has_price(client):
    response = client.get("/")
    assert "price" in response.context

def test_home_view_has_domains(client):
    response = client.get("/")
    assert "tlds" in response.context

def test_home_view_has_domains(client):
    response = client.get("/")
    assert "tlds" in response.context

