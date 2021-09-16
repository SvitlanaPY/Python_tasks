import requests

# Поиск местонахождения для запросов на GitHub
# response = requests.get('https://api.github.com/search/repositories')
response = requests.get('https://api.github.com/search/repositories', params={'q': 'requests+language:python'})

print(response.text)   # бачимо, що зміст є JSON контентом
print()
print()
data = response.json()
print(type(data))   # <class 'dict'>
print()
print("data['items'] :", data['items'])
print()
print("==========================")
print()
print(data['items'][0]['name'])
# print(response.text)

# Анализ некоторых атрибутов местонахождения запросов
json_response = response.json()
repository = json_response['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+


print()
print("ALL HEADERS:   ", response.headers)
print("'Date' HEADER:  ", response.headers['Date'])
print("'Content-Type' HEADER:  ", response.headers['Content-Type'])
print("'Server' HEADER:  ", response.headers['Server'])
