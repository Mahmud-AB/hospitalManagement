from sched import scheduler
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Appointment

# Create your views here.
def appointment(request):
    
    if request.method == 'POST':
        p_name=request.POST.get('p_name')
        email=request.POST.get('email')
        d_name=request.POST.get('d_name')
        speciality=request.POST.get('speciality')
        phoneNumber=request.POST.get('phone')
        date=request.POST.get('date')
        Appointment.objects.create(p_name=p_name,email=email,d_name=d_name,speciality=speciality,phoneNumber=phoneNumber,datetime=date)
        messages.success(request,'Succecfully Booked')
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
    return render(request,'appointment/appointment.html')
