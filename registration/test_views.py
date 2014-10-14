from .views import register_domain 
from django.core.urlresolvers import resolve
from django.http import HttpRequest

def test_url_solves_to_register_view():
    found = resolve("/registration/domain/")
    assert found.func == register_domain 

def test_register_domain_returns_view(client):
    response = client.post("/registration/domain/", {"domain": "mailgenic", "tld": ".com"})
    assert "Registration" in response.content.decode("utf-8")
