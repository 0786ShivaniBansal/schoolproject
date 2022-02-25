
from django.db import models
# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=100,null=True,blank=True)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    city=models.CharField(max_length=100,null=True,blank=True)
    state=models.CharField(max_length=100,null=True,blank=True)
    emailaddress=models.EmailField(max_length=100,null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    DOB=models.TextField(max_length=100,null=True,blank=True)
    gender=models.TextField(null=True,blank=True)
    mothersname=models.CharField(max_length=100,null=True,blank=True)
    fathersname=models.CharField(max_length=100,null=True,blank=True)
    fatheroccupation=models.CharField(max_length=100,null=True,blank=True)
    

class Book(models.Model):
    title=models.TextField(null=True,blank=True)
    author=models.TextField(null=True,blank=True)
    isbn=models.TextField(null=True,blank=True)

class Bookinv(models.Model):
    Title=models.TextField(null=True,blank=True)
    Author=models.TextField(null=True,blank=True)
    ISBN=models.TextField(null=True,blank=True)
    Publisher=models.TextField(null=True,blank=True)
    year=models.IntegerField(null=True,blank=True)
    

class index(models.Model):
    addbook=models.TextField(null=True,blank=True)
    issuebook=models.TextField(null=True,blank=True)