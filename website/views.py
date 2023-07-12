from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib import messages


def home(request):
    return render(request, "website/home.html")


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful.")
            redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
            return redirect("login")
    else:
        return render(request, "website/login.html")
