from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError
from django.core.validators import MinLengthValidator
    
    
#appointment forms create        
class InputForm(forms.Form):
 
    p_name = forms.CharField(max_length = 200)
    email = forms.EmailField(max_length = 200)
    d_name = forms.CharField(max_length = 200)
    speciality = forms.CharField(max_length = 200)        
    phoneNumber = forms.CharField(max_length = 200)