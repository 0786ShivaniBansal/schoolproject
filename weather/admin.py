from django.contrib import admin
from .models import Weather

from weather.api import weather

# Register your models here.
admin.site.register(Weather)