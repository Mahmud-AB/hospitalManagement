from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("cabin", view=views.Cabin,name="cabin"),
    # path("cinfo/<str:pk>/", view=views.cinfo,name="cinfo"),
    path("cbook", view=views.cbook,name="cbook"),
]