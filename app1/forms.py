from django import forms

class PriceForm(forms.Form):
    ACADEMIC_LEVEL_CHOICES = [
        ('high-school', 'High School'),
        ('undergraduate', 'Undergraduate'),
        # Add more academic level options here
    ]
    SERVICE_TYPE_CHOICES = [
        ('editing', 'Editing'),
        ('writing', 'Writing from Scratch'),
        # Add more service type options here
    ]
    CURRENCY_CHOICES = [
        ('USD', 'USD'),
        ('GBP', 'GBP'),
        ('EUR', 'EUR'),
        ('AUD', 'AUD'),
    ]
    academic_level = forms.ChoiceField(choices=ACADEMIC_LEVEL_CHOICES)
    service_type = forms.ChoiceField(choices=SERVICE_TYPE_CHOICES)
    currency = forms.ChoiceField(choices=CURRENCY_CHOICES)
