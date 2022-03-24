from django.db import models

# Create your models here.
class form(models.Model):
    emailaddress=models.EmailField(max_length=100,null=True,blank=True)
    password=models.TextField()