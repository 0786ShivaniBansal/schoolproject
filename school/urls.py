
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
path('/reg',views.reg ,name='reg'),
path('',views.books,name='books'),
path('/bookin',views.bookinv,name='bookinv')
]