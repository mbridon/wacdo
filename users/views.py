from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from dashboard.views import RestaurantListView


def home_view(request):
    return render(request, "home.html")


def register_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect("restaurant-list")

    else:
        form = CustomUserCreationForm()

    return render(request, "register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect("restaurant-list")

        return render(request, "login.html", {"form": form, "error": "Identifiants incorrects"})

    else:
        form = AuthenticationForm()

        return render(request, "login.html", {"form": form})


@login_required
def logout_view(request):
    logout(request)

    return redirect(login_view)