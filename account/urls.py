from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.login,name="login"),
    path("login.html", view=views.login,name="login1"),
    path("registration", view=views.reg,name="reg"),
]