from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse
from .forms import RegistrationForm, ContactForm
from .whois import check_domain_availability

def domain(request):
    if request.method == "GET":
        form = RegistrationForm(request.GET)
        if form.is_valid():
            domain = "{0}.{1}".format(form.cleaned_data["domain"],
                                      form.cleaned_data["tld"])
            availability = check_domain_availability(domain)
            return render(request, "domain.html", {"full_domain": domain, "available": availability})
    elif request.method == "POST":
        form = ContactForm(request.POST)
        domain = request.GET["domain"]
        tld = request.GET["tld"]
        full_domain = "{0}.{1}".format(domain, tld)
        availability = check_domain_availability(full_domain)

        if form.is_valid():
            print(form.cleaned_data)
            print(address_list)
        return redirect("{0}?domain={1}&tld={2}".format(reverse("contact"),
                                                        domain, tld))

def contact(request):
    if request.method == "GET":
        form = RegistrationForm(request.GET)
        domain = request.GET["domain"]
        tld = request.GET["tld"]
        if form.is_valid():
            full_domain = "{0}.{1}".format(form.cleaned_data["domain"],
                                      form.cleaned_data["tld"])
            availability = check_domain_availability(full_domain)
            return render(request, "contact.html", {"full_domain": full_domain, "available": availability})
    elif request.method == "POST":
        domain = request.GET["domain"]
        tld = request.GET["tld"]
        address_list = request.POST.getlist("new_mail")
        return redirect("{0}?domain={1}&tld={2}".format(reverse("payment"),
                                                        domain, tld))

def payment(request):
    if request.method == "GET":
        form = RegistrationForm(request.GET)
        if form.is_valid():
            domain = "{0}.{1}".format(form.cleaned_data["domain"],
                                      form.cleaned_data["tld"])
            availability = check_domain_availability(domain)
            return render(request, "billing.html", {"full_domain": domain, "available": availability})


