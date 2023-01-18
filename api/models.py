from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=200, null=False , blank = False);
    designation = models.CharField(max_length=200, null= False , blank=False)
    n  = models.ImageField(upload_to="Profile")
    mobile = models.IntegerField( null=False)
    email = models.EmailField(null=False)
    location = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Cats(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    

    def __str__(self):
        return self.name


class Contents(models.Model):
    type = models.ForeignKey(Cats,on_delete=models.CASCADE)
    title = models.CharField(max_length=200 , null=False , blank=False)
    image = models.ImageField(upload_to="images")
    desc = models.TextField(max_length=500)
    technologies = models.CharField(null=True , max_length=200)
    
    def __str__(self):
        return self.title





class Services(models.Model):
    icon = models.FileField(upload_to="images")
    ser = models.CharField(max_length=200 , null=False , blank=False)
    desc = models.CharField(max_length=200 , null=False , blank=False)
  
    def __str__(self):
        return self.ser