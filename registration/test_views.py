from django.core.urlresolvers import resolve
from django.http import HttpRequest

from .views import register_domain
from .forms import RegistrationForm

def test_url_solves_to_register_view():
    found = resolve("/registration/domain/")
    assert found.func == register_domain

def test_register_domain_returns_view(rf):
    data = {"domain": "mailgenic", "tld": ".com"}
    request = rf.post("/registration/domain", data)
    response = register_domain(request)
    assert "Registration" in response.content.decode("utf-8")

# FORMS TEST

def test_registration_form_is_valid():
    data = {"domain": "mailgenic", "tld": ".com"}
    form = RegistrationForm(data=data)
    assert form.is_valid()

def test_registration_form_is_invalid():
    data = {"domain": "", "tld": ".com"}
    form = RegistrationForm(data=data)
    assert not form.is_valid()
