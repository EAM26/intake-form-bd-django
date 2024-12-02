from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=80, null=True, blank=True)
    address = models.CharField(max_length=80, null=True, blank=True)
    zip_code = models.CharField(max_length=80, null=True, blank=True)
    city = models.CharField(max_length=80, null=True, blank=True)
    requesting_party = models.CharField(max_length=80, null=True, blank=True)
    risk_class = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField()
    email = models.EmailField(max_length=80, null=True, blank=True)
    organizational = models.CharField(max_length=80, null=True, blank=True)
    constructional = models.CharField(max_length=80, null=True, blank=True)
    compartment = models.CharField(max_length=80, null=True, blank=True)
    carryaway = models.CharField(max_length=80, null=True, blank=True)
    electronic = models.CharField(max_length=80, null=True, blank=True)
    shield = models.CharField(max_length=80, null=True, blank=True)
    alarm = models.CharField(max_length=80, null=True, blank=True)
    verification = models.CharField(max_length=80, null=True, blank=True)
    reaction = models.CharField(max_length=80, null=True, blank=True)
    customization = models.CharField(max_length=80, null=True, blank=True)
    partial_security = models.CharField(max_length=80, null=True, blank=True)
    maintenance = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return f"{self.name}\n {self.city}"
