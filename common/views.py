from django.contrib import messages
from django.core.exceptions import ValidationError
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import FormView

from common.forms import ContactForm
from common.services.contact import create_contact_message
from products.models import Flower


def home(request: HttpRequest) -> HttpResponse:
    # Ако искаш, можем да го заменим със selector по-късно
    products = Flower.objects.all()
    return render(request, "home.html", {"products": products})


def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            try:
                create_contact_message(
                    name=form.cleaned_data["name"],
                    email=form.cleaned_data["email"],
                    subject=form.cleaned_data["subject"],
                    message=form.cleaned_data["message"],
                )
                messages.success(request, "Вашето съобщение беше изпратено успешно!")
                return redirect("contact")
            except ValidationError as e:
                messages.error(request, str(e))
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})


class ContactView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = "/contact/"

    def form_valid(self, form):
        create_contact_message(
            name=form.cleaned_data["name"],
            email=form.cleaned_data["email"],
            subject=form.cleaned_data["subject"],
            message=form.cleaned_data["message"],
        )
        return super().form_valid(form)