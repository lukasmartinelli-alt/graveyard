from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegistrationForm, ContactForm
from .whois import check_domain_availability

def register_domain(request):
    if request.method == "GET":
        form = RegistrationForm(request.GET)
        if form.is_valid():
            domain = "{0}.{1}".format(form.cleaned_data["domain"],
                                      form.cleaned_data["tld"])
            availability = check_domain_availability(domain)
            return render(request, "registration.html", {"domain": domain, "available": availability})
    elif request.method == "POST":
        form = ContactForm(request.POST)
        address_list = request.POST.getlist("new_mail")
        domain = request.GET["domain"]
        tld = request.GET["tld"]
        domain = "{0}.{1}".format(domain, tld)

        if form.is_valid():
            print(form.cleaned_data)
            print(address_list)

        return render(request, "billing.html", {"domain": domain})
