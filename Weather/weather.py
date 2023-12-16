import requests
from pprint import pprint

API_KEY = '19fc96ed1a1daebe000e661170eff8d6'

city = input('Enter a city name: ')

base_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + API_KEY

weather_data = requests.get(base_url).json()

pprint(weather_data)