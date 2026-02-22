from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Грешно потребителско име или парола.')

    return render(request, 'login.html')

def register_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Паролите не съвпадат.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Потребителското име е заето.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Имейлът вече е зает.')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, user)
        return redirect('home')

    return render(request, 'register.html')

from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'profile.html')

def logout_view(request: HttpRequest) -> HttpResponse:
    logout(request)
    return redirect('home')