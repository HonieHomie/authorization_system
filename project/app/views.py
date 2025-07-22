from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User

# Create your views here.
def register(request):
    if request.method == "POST":
        password = request.POST.get("password")
        login = request.POST.get("login")
        if login and password:
            User.objects.create(username=login, password=password, is_logged=True)
            return redirect("app/")

    return render(request, "register.html")

def login(request):
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        passcode = request.POST.get("passcode")
        user_qs = User.objects.filter(username=nickname, password=passcode)
        if user_qs.exists():
            user = user_qs.first()
            user.is_logged = True
            user.save()
            return render(request, "userpage.html", {"user": user})
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

def userpage(request):
    # Try to get a logged-in user, fallback to None
    user = User.objects.filter(is_logged=True).first()
    return render(request, "userpage.html", {"user": user})

#end of code hahhahahaha