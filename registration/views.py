from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegistrationForm

def register_domain(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)

        domain = request.POST["domain"]
        tld = request.POST["tld"]
        form = RegistrationForm()

        return render(request, "registration.html", {"form": form})
