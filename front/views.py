from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from registration import forms

class Home(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        context["price"] = "$2"
        context["tlds"] = forms.SUPPORTED_TLDS_CHOICES
        return context

