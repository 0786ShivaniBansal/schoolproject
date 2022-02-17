from pyexpat import model
from rest_framework import serializers
from weather . models import Weather
class weatherserializer(serializers.ModelSerializer):
    model = Weather
    fields = '__all__'
     