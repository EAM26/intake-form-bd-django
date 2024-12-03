from datetime import datetime
from django.shortcuts import render, redirect
from .forms import IntakeForm
from .models import Form, Item  # Import the Item model


def index(request):
    if request.method == "POST":
        form = IntakeForm(request.POST)
        if form.is_valid():
            # Save the form data to the database and create the form instance
            form_instance = Form.objects.create(
                name=form.cleaned_data["name"],
                address=form.cleaned_data["address"],
                zip_code=form.cleaned_data["zip_code"],
                city=form.cleaned_data["city"],
                requesting_party=form.cleaned_data["requesting_party"],
                risk_class=form.cleaned_data["risk_class"],
                date=datetime.now().date(),
                email=form.cleaned_data["email"],
                organizational=form.cleaned_data["organizational"],
                constructional=form.cleaned_data["constructional"],
                compartment=form.cleaned_data["compartment"],
                carryaway=form.cleaned_data["carryaway"],
                electronic=form.cleaned_data["electronic"],
                shield=form.cleaned_data["shield"],
                alarm=form.cleaned_data["alarm"],
                verification=form.cleaned_data["verification"],
                reaction=form.cleaned_data["reaction"],
                customization=form.cleaned_data["customization"],
                partial_security=form.cleaned_data["partial_security"],
                maintenance=form.cleaned_data["maintenance"],
                frequency=form.cleaned_data["frequency"]
            )

            # Handle the dynamic items
            item_names = request.POST.getlist('item_name[]')
            item_values = request.POST.getlist('item_value[]')

            for name, value in zip(item_names, item_values):
                if name and value:  # Ensure no empty fields are saved
                    Item.objects.create(form=form_instance, name=name,
                                        value=float(value))

            return redirect('index')
        else:
            # Debugging: Print form errors
            print(form.errors)
    else:
        form = IntakeForm()

    return render(request, 'index.html', {'form': form})
