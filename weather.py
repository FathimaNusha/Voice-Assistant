import requests
from key import *

api_add = "https://api.openweathermap.org/data/2.5/weather?q=colombo&appid="+key1
json_data = requests.get(api_add).json()



def temp():
  temprature = round(json_data["main"]["temp"]-273)
  return temprature

def des():
  description = json_data["weather"][0]["description"]
  return description





