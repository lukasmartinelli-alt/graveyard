from django.core.urlresolvers import resolve
from django.contrib.auth.views import login
from front.views import Home

def test_root_url_resolves_to_home_view():
    found = resolve("/")
    assert found.view_name == "home"

def test_registration_url_resolves_to_view():
    found = resolve("/register/")
    assert found.func == login

def test_registration_returns_html(client):
    response = client.get("/register/")
    assert "Register" in response.content

