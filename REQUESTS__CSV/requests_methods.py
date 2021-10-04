import requests
# https://smartiqa.ru/blog/python-requests
# Примеры HTTP методов в Requests:
# Помимо GET, большой популярностью пользуются такие методы, как POST, PUT, DELETE, HEAD, PATCH и OPTIONS.
# Для каждого из этих методов существует своя сигнатура, которая очень похожа на метод get().

# response = requests.post('https://httpbin.org/post', data={'key':'value'})
# response = requests.put('https://httpbin.org/put', data={'key':'value'})
# response = requests.delete('https://httpbin.org/delete')
# response = requests.head('https://httpbin.org/get')
# response = requests.patch('https://httpbin.org/patch', data={'key':'value'})
# response = requests.options('https://httpbin.org/get')


response = requests.post('https://httpbin.org/post', json={'key': 'value'})
json_response = response.json()
print("json_response: ", json_response)
print(json_response['data'])
print("url: ", response.request.url)
# url:  https://httpbin.org/post

response = requests.head('https://httpbin.org/get')
print(response.headers['Content-Type'])
# 'application/json'

response = requests.delete('https://httpbin.org/delete')
json_response = response.json()
print(json_response['args'])
