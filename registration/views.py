from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegistrationForm
from .whois import check_domain_availability

def register_domain(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            domain = form.cleaned_data["domain"] + form.cleaned_data["tld"]
            availability = check_domain_availability(domain)
            return render(request, "registration.html", {"domain": domain, "availability": availability})
