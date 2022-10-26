from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("home",views.home,name='home'),
   path("doctor",views.doctor,name='doctor'),
   path("profile",views.userprofile,name='profile'),
   path("editinfo",views.editinfo,name='editinfo'),
   path("reviews/<str:pk>/",views.reviews,name='reviews'),
   path("addreview",views.addreview,name='addreview'),
   path("showinfo/<str:pk>/",views.showinfo,name='showinfo'),
   path("reviewspage",views.reviewspage,name='reviewspage'),
   
]