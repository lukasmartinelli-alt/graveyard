from django.forms import Form, CharField

class RegistrationForm(Form):
    domain = CharField()
    tld = CharField()
