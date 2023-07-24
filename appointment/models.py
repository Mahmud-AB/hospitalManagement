
from django.db import models

# Create your models here.
class Appointment(models.Model):
    p_name = models.CharField(max_length = 200,null=True,blank=True)
    email = models.EmailField(max_length = 200,null=True,blank=True)
    d_name = models.CharField(max_length = 200,null=True,blank=True)
    speciality = models.CharField(max_length = 200,null=True,blank=True)        
    phoneNumber = models.CharField(max_length = 200,null=True,blank=True)
    datetime=models.DateField(null=True,blank=True)

    def __str__(self):
        return f"Name :{self.p_name} Doctor:{self.d_name}"