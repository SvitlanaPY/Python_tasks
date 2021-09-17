import requests

res = requests.get("https://docs.python.org/3.5/")

print("REQUEST Status_Code:  ", res.status_code)
print("REQUEST CONTENT-TYPE:  ", res.headers['Content-Type'])

# Свойство text показывает тело ответа сервера в текстовом формате (актуально для html-страниц),
# content – результат в виде байтов (удобно при скачивании графической, аудио- или видеоинформации),
# метод json() приводит содержимое ответа к обычному словарю
# (если данные к нему приводимы, в противном случае будет ошибка; актуально для API-запросов).
print("REQUEST BINARY CONTENT:  ", res.content)      # binary content
print("REQUEST TEXT CONTENT:  ", res.text)        # text content


res_png = requests.get("https://docs.python.org/3.5/_static/py.png")
print(res_png.status_code)
print(res_png.headers['Content-Type'])
print("REQUEST BINARY/PNG CONTENT:", res_png.content)   # binary info

with open("python_png.png", "wb") as f:
    f.write(res_png.content)

parameters = {
    "q": "python",
    "test": "test1",
    "name": "Name With Spaces",
    "list": ["test1", "test2"]
}
res_param = requests.get("https://www.google.com/search",
                         params=parameters)
print(res_param.status_code)
# 200
print()
print(res_param.headers['Content-Type'])
# text/html; charset=ISO-8859-1
print()
print("URL with params:", res_param.url)
# https://www.google.com/search?q=python&test=test1&name=Name+With+Spaces&list=test1&list=test2

print()
# print("REQUEST text CONTENT:", res_param.text)
