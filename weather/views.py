from nturl2path import url2pathname
from django.shortcuts import redirect, render
from django.template import context
from weather.models import news,Weather
import requests

# Create your views here.
def weather(request):
       if(request.method=='POST'):
           print(request.POST)
           return redirect('/ind')
       return render(request,'weather.html')
    
      

def index(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=ba24c6018ddd72041749018d0c1b1ef8&units=metric'

    city = 'London'
    r=requests.get(url.format(city)).json()
    city_weather={
        'city' : city,
        'tempreature' :r['main']['temp'],
        'description' :r['weather'][0]['description'],
        'temp_min'    :r['main']['temp_min'],
        'temp_max'    :r['main']['temp_max'],
        'feels_like'  :r['main']['feels_like']
        
    }
    context={'city_weather':city_weather}
    return render(request,'ind.html',context)




# def new(request):
#     url = 'https://api.openweathermap.org/data/2.5/weather?q=London&appid=ba24c6018ddd72041749018d0c1b1ef8&units=metric'

#     city = 'London'
#     r=requests.get(url.format(city)).json()
#     city_weather={
#         'city' : city,
#         'tempreature' :r['main']['temp'],
#         'description' :r['weather'][0]['description'],
#         'temp_min'    :r['main']['temp_min'],
#         'temp_max'    :r['main']['temp_max'],
#         'feels_like'  :r['main']['feels_like']
        
#     }
#     context={'city_weather':city_weather}
    
    
#     return render(request,'new.html',context)

def weatherapi(request):
    if(request.method=='POST'):
        print(request.POST)
        w=Weather.objects.create(coordinate=request.POST['coordinate'],longitude=request.POST['longitude'],latitude=request.POST['latitude'],id=request.POST['id'],description=request.POST['description'],tempreature=request.POST['tempreature'],tempmin=request.POST['tempmin'],tempmax=request.POST['tempmax'],pressure=request.POST['pressure'],humidity=request.POST['humidity'])
    return render(request,'weatherapi.html')