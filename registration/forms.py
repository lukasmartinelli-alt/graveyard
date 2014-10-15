from django.forms import Form, CharField, ChoiceField

SUPPORTED_TLDS_CHOICES = (
    ("ch", ".ch"),
    ("com", ".com"),
    ("me", ".me"),
)

class RegistrationForm(Form):
    domain = CharField()
    tld = ChoiceField(SUPPORTED_TLDS_CHOICES)

