from datetime import datetime

from django.contrib import messages
from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from .forms import IntakeForm
from .message import Message
from .models import Form, Item  # Import the Item model


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
            date = datetime.now().date()
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
            frequency = form.cleaned_data["frequency"]
            # Save the form data to the database and create the form instance

            form_instance = Form.objects.create(
                name=name, address=address, zip_code=zip_code, city=city,
                requesting_party=requesting_party, risk_class=risk_class,
                date=date, email=email, organizational=organizational,
                constructional=constructional, compartment=compartment,
                carryaway=carryaway, electronic=electronic, shield=shield,
                alarm=alarm, verification=verification, reaction=reaction,
                customization=customization,
                partial_security=partial_security, frequency=frequency
            )

            # Handle the dynamic items
            item_names = request.POST.getlist('item_name[]')
            item_values = request.POST.getlist('item_value[]')
            item_attractiveness = request.POST.getlist('item_attractiveness[]')

            for atrr_name, value, attractiveness in zip(item_names,
                                                        item_values,
                                                        item_attractiveness):
                if atrr_name and value and attractiveness:  # Ensure no empty
                    # fields are saved
                    Item.objects.create(form=form_instance,
                                        attr_name=atrr_name,
                                        value=float(value),
                                        attractiveness=attractiveness)

            message_body = Message.get_body(name, city, date, requesting_party,
                                            risk_class, email, organizational,
                                            constructional, compartment,
                                            carryaway, electronic, shield,
                                            alarm,
                                            verification, reaction,
                                            customization, partial_security,
                                            frequency, item_names,
                                            item_values, item_attractiveness)

            email_message = EmailMessage("Intake Form submission",
                                         message_body, to=["synco@casyri.nl"]
                                         )

            email_message.send()

            messages.success(request, "FORM SUBMITTED SUCCESSFULLY!")
            return redirect('index')
        else:
            # Debugging: Print form errors
            print(form.errors)
            messages.error(request,
                           "There were errors in your form. Please fix them "
                           "and try again.")
    else:
        form = IntakeForm()

    return render(request, 'index.html', {'form': form})
