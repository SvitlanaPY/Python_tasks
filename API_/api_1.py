import requests
import json

api_url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    'q': 'London',
    'appid': 'f003dd12f2976bc2cf3789bd7e5f9354'
}

res = requests.get(api_url, params=parameters)
print(res.status_code)   # 200
print(res.headers["Content-Type"])   # application/json; charset=utf-8
print(res.json())  # = print(json.loads(res.text)_
# data = json.loads(res.text)
# print(data)

data = res.json()
print("DATA:", data)
print(data["main"])
print(data["main"]["temp"])
