from django.db import models


# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name
      

class BannerSlider(models.Model):
    title=models.CharField(max_length=50)
    image=models.ImageField(upload_to='Banner_Image')

    def __str__(self):
        return self.title
    
class Department(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=100)
    dept=models.ForeignKey(Department,on_delete=models.CASCADE)
    Birth_year=models.DateField()

    def __str__(self):
        return self.name
    
class CardInfo(models.Model):
    title=models.CharField(max_length=60)
    description=models.TextField(max_length=250)
    image=models.ImageField(upload_to='CardImage')

    def __str__(self):
        return self.title
    


class SignUp(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name+'   '+self.password
    
      
        
    
       
