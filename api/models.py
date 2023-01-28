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

    def delete(self,*args,**kwargs):
        self.n.delete()
        super().delete(*args, **kwargs)
   


class Contents(models.Model):
    type = models.CharField(max_length=200 , null=False , blank=False)
    title = models.CharField(max_length=200 , null=False , blank=False)
    image = models.ImageField(upload_to="images")
    desc = models.TextField(max_length=500)
    technologies = models.CharField(null=True , max_length=200)
    
    def __str__(self):
        return self.title
    
    def delete(self,*args,**kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)






class Services(models.Model):
    icon = models.FileField(upload_to="images")
    ser = models.CharField(max_length=200 , null=False , blank=False)
    desc = models.CharField(max_length=200 , null=False , blank=False)
  
    def __str__(self):
        return self.ser

    def delete(self,*args,**kwargs):
        self.icon.delete()
        super().delete(*args, **kwargs)


class Education(models.Model):
    year = models.CharField(max_length=8, null=False, blank=False)
    cource = models.CharField(max_length=200 , null=False , blank=False)
    institute = models.CharField(max_length=200 , null=False , blank=False)
  
    def __str__(self):
        return self.cource

class Experience(models.Model):
    year = models.CharField(max_length=20)
    position = models.CharField(max_length=200 )
    company = models.CharField(max_length=200 )
  
    def __str__(self):
        return self.position
