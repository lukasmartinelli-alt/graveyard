from django.forms import Form, CharField, ChoiceField, EmailField

SUPPORTED_TLDS_CHOICES = (
    ("ch", ".ch"),
    ("com", ".com"),
    ("me", ".me"),
)

class RegistrationForm(Form):
    domain = CharField()
    tld = ChoiceField(SUPPORTED_TLDS_CHOICES)

class ContactForm(Form):
    name = CharField()
    old_mail = EmailField()

