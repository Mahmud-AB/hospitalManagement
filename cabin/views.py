from sched import scheduler
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Cabininfo,Cabinbooking

#Create your views here.
def cbook(request):
    if request.method == 'POST':
        p_name=request.POST.get('p_name')
        email=request.POST.get('email')
        d_name=request.POST.get('d_name')
        nid=request.POST.get('nid')
        phoneNumber=request.POST.get('phone')
        roomType=request.POST.get('type')
        Cabinbooking.objects.create(p_name=p_name,email=email,d_name=d_name,nid=nid,phoneNumber=phoneNumber,roomType=roomType)
        messages.success(request,'Succecfully Booked')
    cabin=Cabininfo.objects.all
    serial=Cabinbooking.objects.all
    context = {
        'info' : cabin,
        'serial':serial
    }
    return render(request,'cbook/cbook.html',context)

def Cabin(request):
    cabin=Cabininfo.objects.all
    context = {
        'info' : cabin
    }
    return render(request,"cabin/cabin.html",context)


# def cinfo(request,pk):
#     detail = Cabininfo.objects.get(id=pk)
#     context = {
#         'details' : detail
#     }
#     return render(request, 'cabininfo/cabininfo.html', context)