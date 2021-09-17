import requests
import json

# В этой задаче вам необходимо воспользоваться API сайта numbersapi.com
# http://numbersapi.com/#random/math
# Вам дается набор чисел. Для каждого из чисел необходимо узнать,
# существует ли интересный математический факт об этом числе.
# Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
# Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
#
# Пример запроса к интересному числу:
# http://numbersapi.com/31/math?json=true
#
# Пример запроса к скучному числу:
# http://numbersapi.com/999/math?json=true
#
# Пример входного файла:
# 31
# 999
# 1024
# 502
#
# Пример выходного файла:
# Interesting
# Boring
# Interesting
# Boring
#
#
# TESTING:
# api_url1 = "http://numbersapi.com/1969/year?json=true"
# response1 = requests.get(api_url1)
# data1 = json.loads(response1.text)   # або data = res.json()
# print("data1:", data1)


# api_url2 = "http://numbersapi.com/31/math?json=true"   # 31 is number
# api_url2 = "http://numbersapi.com/999/math?json=true"
# api_url2 = "http://numbersapi.com/1024/math?json=true"
# api_url2 = "http://numbersapi.com/502/math?json=true"

number = input("Enter number: ")
api_url2 = "http://numbersapi.com/{}/math?json=true".format(number)
response2 = requests.get(api_url2)
data2 = json.loads(response2.text)   # або data = response2.json()
print("data2:", data2)
print("'found':", data2["found"])


file = open("nums.txt")
x = file.read().splitlines()
print("nums:  ", x)
print("length x: ", len(x))
for i in range(len(x)):
    x[i] = int(x[i])
    api_url = "http://numbersapi.com/{}/math?json".format(x[i])
    response = requests.get(api_url)
    data = response.json()     # or:   data = json.loads(response.text)
    print("data:  ", data)
    if data['found'] is True:
        print("Interesting")
    else:
        print("Boring")

print("THE END")

file.close()
