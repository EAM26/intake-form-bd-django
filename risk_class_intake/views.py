from datetime import datetime
from django.shortcuts import render, redirect
from .forms import IntakeForm
from .models import Form


def index(request):
    if request.method == "POST":
        form = IntakeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            address = form.cleaned_data["address"]
            zip_code = form.cleaned_data["zip_code"]
            city = form.cleaned_data["city"]
            requesting_party = form.cleaned_data["requesting_party"]
            risk_class = form.cleaned_data["risk_class"]
            date = datetime.now().date()  # Get the current date
            email = form.cleaned_data["email"]
            organizational = form.cleaned_data["organizational"]
            constructional = form.cleaned_data["constructional"]
            compartment = form.cleaned_data["compartment"]
            carryaway = form.cleaned_data["carryaway"]
            electronic = form.cleaned_data["electronic"]
            shield = form.cleaned_data["shield"]
            alarm = form.cleaned_data["alarm"]
            verification = form.cleaned_data["verification"]
            reaction = form.cleaned_data["reaction"]
            customization = form.cleaned_data["customization"]
            partial_security = form.cleaned_data["partial_security"]
            maintenance = form.cleaned_data["maintenance"]

            # Debugging: Print the cleaned data
            print(f"Name: {name}, Address: {address}, Zip Code: {zip_code},"
                  f" City: {city}, Requesting Party: {requesting_party},"
                  f" Risk Class: {risk_class}, Date: {date}, Email: {email}")

            # Save the form data to the database
            Form.objects.create(name=name, address=address, zip_code=zip_code,
                                city=city, requesting_party=requesting_party,
                                risk_class=risk_class, date=date, email=email,
                                organizational=organizational, constructional=
                                constructional, compartment=compartment,
                                carryaway=carryaway, electronic=electronic,
                                shield=shield, alarm=alarm, verification=
                                verification, reaction=reaction,
                                customization=customization, partial_security=
                                partial_security, maintenance=maintenance)
            return redirect('index')
        else:
            # Debugging: Print form errors
            print(form.errors)
    else:
        form = IntakeForm()

    return render(request, 'index.html', {'form': form})
