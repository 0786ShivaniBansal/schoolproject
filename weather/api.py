from rest_framework .views import APIView
from rest_framework .response import Response
from rest_framework import status
from . serializers import *
from weather import serializers

class weather(APIView):
    def get(self,request):
        model=Weather.objects.all()
        serializers=weatherserializer(model,many=True)
        return Response(serializers.data)