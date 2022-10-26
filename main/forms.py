from django import forms
from django.forms import ModelForm
from .models import profile

    
    
#Donor registrarion forms create
class userinfo(ModelForm):
    class Meta:
        model = profile
        fields = ["profile_img" ,"Name" ,"Email" ,"Date_of_Birth" ,"PhoneNumber" ,"Gender" ]
       
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control','required':'True', 'placeholder':"Full Name"}),
            'Email' : forms.EmailInput(attrs={'class':'form-control', 'required':'True'}),
            'Gender' : forms.Select(attrs={'class':'form-control', 'required':'True'}),
            'Date_of_Birth' : forms.DateInput(attrs={'class':'form-control', 'type':'date', 'required':'True'}),
            'Phone_number' : forms.NumberInput(attrs={'class':'form-control', 'required':'True'}),
            
        }