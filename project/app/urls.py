from django.urls import path
from . import views

# Urls here

urlpatterns = [
    path("login/", views.login, name="index"),
    path("register/", views.register, name="register"),
    path("userpage/", views.userpage, name="userpage"),
]