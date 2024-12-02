from django.db import models


class Form(models.Model):
    name = models.CharField(max_length=80)
    address = models.CharField(max_length=80)
    zip_code = models.CharField(max_length=80)
    city = models.CharField(max_length=80)
    requesting_party = models.CharField(max_length=80)
    risk_class = models.CharField(max_length=80)
    date = models.DateField()
    email = models.EmailField()
