from turtle import mode
from django.db import models

# Create your models here.
class news(models.Model):
    city:str
    tempreature:int
    pressure:int
    humidity:int

class Weather(models.Model):
    coordinate=models.TextField(null=True,blank=True)
    longitude=models.TextField(null=True,blank=True)
    longitude=models.TextField(null=True,blank=True)
    latitude=models.TextField(null=True,blank=True)
    id=models.TextField(primary_key=True)
    description=models.CharField(max_length=100,null=True,blank=True)
    tempreature=models.TextField(null=True,blank=True)
    tempmin=models.TextField(null=True,blank=True)
    tempmax=models.TextField(null=True,blank=True)
    pressure=models.TextField(null=True,blank=True)
    humidity=models.TextField(null=True,blank=True)