from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import Registration
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout

def reg(request):
    forms = Registration()
    if request.method == 'POST':
        forms = Registration(request.POST)
        if forms.is_valid():
            forms.save()
            print(forms.errors)
            context_details ={
                'forms': forms
            }
            # After donor registration, donor details display
            messages.success(request, 'Successfully Registered')
            return render(request, 'reg/registration.html', context_details)
        else:
            messages.error(request, 'Form INVALID')
    context = {
        'forms': forms,
    }
    return render(request, 'reg/registration.html', context)

def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Login')
            return redirect('login')
    else:
        return render(request, "login/login.html")

def user_logout(request):
    logout(request)
    return redirect('index')
