from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        password = request.POST.get("password")
        login = request.POST.get("login")
        if login and password:
            User.objects.create(username=login, password=password)
            return redirect("app/")

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        passcode = request.POST.get("passcode")
        if User.objects.filter(username=nickname, password=passcode):
            return HttpResponse("Login applied")
        else:
            return HttpResponse("Error, username or password is incorrect")
    return render(request, "login.html")