import requests

post_params = {'user': 'admin', 'password': 'admin_pass1'}


response = requests.post('https://httpbin.org/post', data=post_params)
print("text: ", response.text)

print("url: ", response.url)

json_data = response.json()
print("json_data: ", json_data)
print(type(json_data))   # <class 'dict'>

print(response.json()['form'])   # = print(json_data['form'])
# {'password': 'admin_pass1', 'user': 'admin'}

# Свойство text показывает тело ответа сервера в текстовом формате (актуально для html-страниц),
# content – результат в виде байтов (удобно при скачивании графической, аудио- или видеоинформации),
# метод json() приводит содержимое ответа к обычному словарю
# (если данные к нему приводимы, в противном случае будет ошибка; актуально для API-запросов).
