from django import forms


class IntakeForm(forms.Form):
    name = forms.CharField(max_length=80)
    address = forms.CharField(max_length=80)
    zip_code = forms.CharField(max_length=80)
    city = forms.CharField(max_length=80)
    requesting_party = forms.CharField(max_length=80)
    risk_class = forms.CharField(max_length=80)
    email = forms.EmailField()
