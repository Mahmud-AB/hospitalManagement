from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import catagory, doctors,profile,Reviews
from .forms import  userinfo
from appointment.models import  Appointment
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
@login_required(login_url='login')
def home(request):


    blog=Reviews.objects.all
    context={
         "blog":blog
    }
    return render(request,"home/home.html",context)

@login_required(login_url='login')
def doctor(request):
    doctor=doctors.objects.all
    field=catagory.objects.all
    context = {
        'info' : doctor,
        'field': field
    }
    return render(request,"doctor/doctor.html",context)
    


def showinfo(request,pk):
    detail = doctors.objects.get(id=pk)
    context = {
        'details' : detail
    }
    return render(request, 'showinfo/showinfo.html', context)

def userprofile(request):
    profile=request.user.profile
    appointment=Appointment.objects.all
    review=Reviews.objects.all
    context={
         "profile":profile,
         "appointment":appointment,
         "review":review
    }
    return render(request,"profile/profile.html",context)

def editinfo(request):
    profile=request.user.profile
    forms = userinfo(instance=profile)
    if request.method=="POST":
         form =userinfo(request.POST,request.FILES,instance=profile)
         if form.is_valid():
              form.save()
              return redirect("profile")
    context = { 'forms' : forms}
    return render(request,'editinfo/editinfo.html', context)


def reviews(request,pk):
    
    detail = Reviews.objects.get(id=pk)
    context = {
        'details' : detail
    }
    return render(request, 'reviews/reviews.html', context)

def addreview(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        title=request.POST.get('title')
        description=request.POST.get('description')
    
        date=request.POST.get('date')
        Reviews.objects.create(name=name,title=title,description=description,datetime=date)
        messages.success(request,'Succecfully Added')
        # forms = InputForm(request.POST)
    #     if forms.is_valid():
    #             forms.save()
    #             print(forms.errors)
    #             context_details ={
    #                 'forms' : forms
    #             }
    #             #After donor registation donor details display
    #             messages.success(request,'Succecfully Book')
    #             return render(request, '/appointment.html', context_details)
    #     else:
    #         messages.error(request,'Form INVALID')
    # context = {
    #             'forms' : forms,
    #         }
    return render(request,'addreview/addreview.html')

def reviewspage(request):
    blog=Reviews.objects.all
    context={
         "blog":blog
    }
    return render(request,"reviewpage/reviewspage.html",context)