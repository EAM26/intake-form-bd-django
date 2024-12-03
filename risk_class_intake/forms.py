from django import forms


class IntakeForm(forms.Form):
    name = forms.CharField(max_length=80)
    address = forms.CharField(max_length=80)
    zip_code = forms.CharField(max_length=80)
    city = forms.CharField(max_length=80)
    requesting_party = forms.CharField(max_length=80)
    risk_class = forms.CharField(max_length=80)
    email = forms.EmailField()
    organizational = forms.CharField(max_length=80)
    constructional = forms.CharField(max_length=80)
    compartment = forms.CharField(max_length=80)
    carryaway = forms.CharField(max_length=80)
    electronic = forms.CharField(max_length=80)
    shield = forms.CharField(max_length=80)
    alarm = forms.CharField(max_length=80)
    verification = forms.CharField(max_length=80)
    reaction = forms.CharField(max_length=80)
    customization = forms.CharField(max_length=80)
    partial_security = forms.CharField(max_length=80)
    frequency = forms.IntegerField()
