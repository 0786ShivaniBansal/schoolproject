from unicodedata import name
from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views. weather ,name='weather'),
    path('ind',views.index,name='ind'),
    
    # path('new',views.new ,name='new'),
    path('weather',views.weatherapi,name='weatherapi')
]
