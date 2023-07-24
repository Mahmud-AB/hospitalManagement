from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.user_login,name="index"),
    path("registration", view=views.reg,name="reg"),
    path("logout/", view=views.user_logout, name="logout"),
]