from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Cabinbooking(models.Model):
    p_name = models.CharField(max_length = 200,null=True,blank=True)
    email = models.EmailField(max_length = 200,null=True,blank=True)
    d_name = models.CharField(max_length = 200,null=True,blank=True)
    nid = models.CharField(max_length = 200,null=True,blank=True)        
    phoneNumber = models.CharField(max_length = 200,null=True,blank=True)
    roomType = models.CharField(max_length = 200,null=True,blank=True)

    def __str__(self):
        return f"Name :{self.p_name} Room:{self.roomType}"




class Cabininfo(models.Model):
    img=models.ImageField(null=True,blank=True)
    roomType=models.CharField(max_length =100,null=True,blank=True)
    description=models.CharField(max_length =500,null=True,blank=True)
    available=models.IntegerField(null=True,blank=True)
    rent=models.IntegerField(null=True,blank=True)
    
   

    def __str__(self):
        return f"Name :{self.roomType}"

