from django.shortcuts import render
from django import forms
from .models import Landing
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        name = request.POST["name"]
        url = request.POST["url"]
        l = Landing(username=request.user, name=name, url=url)
        l.save()
        return render(request, "user.html", {
            "message": "Added Sucessfully"
        })

    return render(request, "user.html")


def login_request(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid Credential"
            })
    return render(request, "login.html")


def logout_request(request):
    logout(request)
    return render(request, "login.html", {
        "message": "Logged Out"
    })


def showlinks(request, name):
    l = Landing.objects.filter(username=name)
    return render(request, 'index.html', {
        "check": l,
        "name": name
    })
