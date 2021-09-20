import requests

# api_url = "https://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=f003dd12f2976bc2cf3789bd7e5f9354"
# res = requests.get(api_url)
# or
#
api_url = "https://api.openweathermap.org/data/2.5/weather"
parameters = {
    'q': 'Madrid',
    'appid': 'f003dd12f2976bc2cf3789bd7e5f9354'
}
res = requests.get(api_url, params=parameters)

print("REQUESTS STATUS CODE: ", res.status_code)
# 200
print("REQUESTS CONTENT-TYPE:", res.headers["Content-Type"])
# application/json; charset=utf-8

print(res.json())  # = print(json.loads(res.text))
data = res.json()
print("DATA:", data)
print("data['main']:", data["main"])
print(data["main"]["temp"])

# data = json.loads(res.text)
# print(data)
