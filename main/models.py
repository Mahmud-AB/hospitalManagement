from django.db import models

from django.contrib.auth.models import User



# Create your models here.

class doctors(models.Model):
    profile_img=models.ImageField(null=True,blank=True)
    name=models.CharField(max_length =100,null=True,blank=True)
    education=models.CharField(max_length = 200,null=True,blank=True)
    speciality=models.CharField(max_length = 200,null=True,blank=True)
    visit=models.IntegerField(null=True,blank=True)
    phone=models.CharField(max_length = 15,null=True,blank=True)
    day=models.CharField(max_length = 15,null=True,blank=True)
    time1=models.TimeField(null=True,blank=True)
    time2=models.TimeField(null=True,blank=True)
    email=models.EmailField(max_length = 200,null=True,blank=True)

    def __str__(self):
        return f"Name :{self.name}  Field:{self.speciality} "

class catagory(models.Model):
    field=models.CharField(max_length = 200,null=True,blank=True)
    img=models.ImageField(null=True,blank=True)



class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_img=models.ImageField(null=True,upload_to='profiles/',blank=True,default="profiles/default.png")
    Name = models.CharField(max_length=20,blank=True,null=True)
    Email =  models.EmailField(blank=True,null=True)
    Date_of_Birth = models.DateField(blank=True,null=True)
    PhoneNumber= models.CharField(max_length=15,null=True,blank=True)
    gender_choices=[
        ('male',"Male"),
        ("female","Female"),
        ("other","Other")
    ]
    Gender =  models.CharField(
        max_length=6, blank=True, null=True,
        choices=gender_choices,
    )
    def __str__(self):
        return f"Name :{self.Name}"


class Reviews(models.Model):
    name=models.CharField(max_length =100,null=True,blank=True)
    title=models.CharField(max_length =100,null=True,blank=True)
    description=models.CharField(max_length =300,null=True,blank=True)
    datetime=models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return f"Name :{self.name}"