from django.forms import Form, CharField, ChoiceField, EmailField

SUPPORTED_TLDS_CHOICES = (
    ("ch", ".ch"),
    ("com", ".com"),
    ("me", ".me"),
)


class DomainForm(Form):
    domain = CharField()
    tld = ChoiceField(SUPPORTED_TLDS_CHOICES)

    def full_domain(self):
        return "{0}.{1}".format(self.cleaned_data["domain"],
                                self.cleaned_data["tld"])


class ContactForm(Form):
    name = CharField()
    old_mail = EmailField()
