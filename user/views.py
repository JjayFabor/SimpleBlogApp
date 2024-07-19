from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

from .forms import *
from django.contrib.auth.models import auth


@login_required
def homeView(request):
    return render(request, "home.html")


def loginView(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect("user:home")
    return render(request, "login.html", {"form": form})


def signupView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user:login")
    else:
        form = SignUpForm()
    return render(request, "signup.html", {"form": form})


def logoutView(request):
    logout(request)
    return redirect("user:login")