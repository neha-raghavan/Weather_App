import requests
import json


city='Kochi'

API_KEY='073bd01b8b193f3dfc7db66c5a7a8c94'

weather_url=requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}')
weather_data=weather_url.json()

temp=round(weather['main']['temp'])