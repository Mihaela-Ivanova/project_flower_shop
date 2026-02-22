from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from common.forms import ContactForm
from products.models import Flower

def home(request: HttpRequest) -> HttpResponse:
    products = Flower.objects.all()
    return render(request, 'home.html', {'products': products})

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Вашето съобщение беше изпратено успешно!")
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})