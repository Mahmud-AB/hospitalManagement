from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import  Registration
from django.contrib.auth.models import auth

def reg(request):
    forms = Registration()
    if request.method == 'POST':
        forms = Registration(request.POST)
        if forms.is_valid():
                forms.save()
                print(forms.errors)
                context_details ={
                    'forms' : forms
                }
                #After donor registation donor details display
                messages.success(request,'Succecfully Registerd')
                return render(request, 'reg/registration.html', context_details)
        else:
            messages.error(request,'Form INVALID')
    context = {
                'forms' : forms,
            }
    return render(request,'reg/registration.html', context)

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
             messages.error(request,'invalid Login') 
             return redirect('/login.html')
    else:
        return render(request,"login/login.html")