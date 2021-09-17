import pprint
import requests
# https://smartiqa.ru/blog/python-requests

# Making a GET request
# res = requests.get('https://api.github.com/users/naveenkrnl')

response_ = requests.get('https://api.github.com/events')
print(type(response_))   # <class 'requests.models.Response'>; Мы получили объект класу Response с именем response_

pprint.pprint(dir(response_))   # всі доступні атрибути response_-object-a
# ['__attrs__',
#  '__bool__',
#  '__class__',
#  '__delattr__',
#  '__dict__',
#  '__dir__',
#  '__doc__',
#  '__enter__',
#  '__eq__',
#  '__exit__',
#  '__format__',
#  '__ge__',
#  '__getattribute__',
#  '__getstate__',
#  '__gt__',
#  '__hash__',
#  '__init__',
#  '__init_subclass__',
#  '__iter__',
#  '__le__',
#  '__lt__',
#  '__module__',
#  '__ne__',
#  '__new__',
#  '__nonzero__',
#  '__reduce__',
#  '__reduce_ex__',
#  '__repr__',
#  '__setattr__',
#  '__setstate__',
#  '__sizeof__',
#  '__str__',
#  '__subclasshook__',
#  '__weakref__',
#  '_content',
#  '_content_consumed',
#  '_next',
#  'apparent_encoding',
#  'close',
#  'connection',
#  'content',
#  'cookies',
#  'elapsed',
#  'encoding',
#  'headers',
#  'history',
#  'is_permanent_redirect',
#  'is_redirect',
#  'iter_content',
#  'iter_lines',
#  'json',
#  'links',
#  'next',
#  'ok',
#  'raise_for_status',
#  'raw',
#  'reason',
#  'request',
#  'status_code',
#  'text',
#  'url']

# print headers of request:
print("headers: ", response_.headers)
# {'Server': 'GitHub.com', 'Date': 'Thu, 16 Sep 2021 17:47:49 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Cache-Control': 'public, max-age=60, s-maxage=60', 'Vary': 'Accept, Accept-Encoding, Accept, X-Requested-With', 'ETag': 'W/"bd12674bd3ed3f8528c78f2b07a56ab42c9da81af116e9391c12cfcfa8d2ab57"', 'Last-Modified': 'Thu, 16 Sep 2021 17:42:48 GMT', 'X-Poll-Interval': '60', 'X-GitHub-Media-Type': 'github.v3; format=json', 'Link': '<https://api.github.com/events?page=2>; rel="next", <https://api.github.com/events?page=10>; rel="last"', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Resource, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '0', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'Content-Encoding': 'gzip', 'X-RateLimit-Limit': '60', 'X-RateLimit-Remaining': '56', 'X-RateLimit-Reset': '1631817386', 'X-RateLimit-Resource': 'core', 'X-RateLimit-Used': '4', 'Accept-Ranges': 'bytes', 'Content-Length': '17093', 'X-GitHub-Request-Id': '922C:BC59:1D2B9C4:1DBB9A0:61438350'}

# print status code on request:
print("status_code: ", response_.status_code)
# 200

# print requested url
print("url: ", response_.url)

# To see the content of request:
# Свойство text показывает тело ответа сервера в текстовом формате (актуально для html-страниц),
# content – результат в виде байтов (удобно при скачивании графической, аудио- или видеоинформации),
# метод json() приводит содержимое ответа к обычному словарю
# (если данные к нему приводимы, в противном случае будет ошибка; актуально для API-запросов).

print("content in text format: ", response_.text)   # text info; показывает тело ответа сервера в текстовом формате
# write text content into file:
with open("python_requests", 'w') as f:
    f.write(response_.text)

print(response_.content)   # binary info; результат (тело ответа сервера) в виде байтов

data = response_.json()   # метод json() приводит содержимое ответа к обычному словарю(если данные к нему приводимы)
print(data)
print(type(data))   # <class 'list'>
