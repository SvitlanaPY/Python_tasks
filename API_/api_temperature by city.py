import requests
# import json

city = input("City? ")
api_url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    'q': city,
    'appid': 'f003dd12f2976bc2cf3789bd7e5f9354',
    'units': 'metric',
    'lang': 'ua'
}

res = requests.get(api_url, params=parameters)
data = res.json()
print("DATA:", data)

template = 'Current temperature in {} is {}'
print(template.format(city, data["main"]["temp"]))
print(data["main"]["temp"])
