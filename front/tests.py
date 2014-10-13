from django.core.urlresolvers import resolve
from front.views import Home, Register

def test_root_url_resolves_to_home_view():
    found = resolve("/")
    assert found.view_name == "home"

def test_registration_url_resolves_to_view():
    found = resolve("/register/")
    assert found.view_name == "register"

def test_registration_returns_html(client):
    response = client.get("/register/")
    assert "Register" in response.content

