# "Рейтинг таксистов"
# Руководитель таксопарка хочет увидеть отчет по всем таксистам,
# где нужно указать имя таксиста и его среднюю оценку.
# Информацию в отчете нужно расположить по убыванию средней оценки таксиста.
# После каждого успешно выполненного заказа, клиент выставляет таксисту оценку - целое число от 1 до 5.
#
# Входные данные
# Программа будет принимать строки, в которых сперва указывается имя таксиста,
# а затем через запятую с пробелом его оценка за заказ.
# Строка "конец" является последней строкой и означает окончание ввода
#
# Выходные данные
# Нужно расположить таксистов в порядке убывания их средней оценке
# и вывести имя каждого таксиста и его среднюю оценку в отдельной строке.
# В случае совпадения средних оценок расположить таксистов нужно отсортировать имена таксистов по алфавиту
#
# Sample Input 1:
# Джек, 2
# Джек, 3
# Билл, 5
# Билл, 4
# Билл, 4
# Билл, 3
# конец
# Sample Output 1:
# Билл 4.0
# Джек 2.5

# Sample Input 2:
# Зина, 5
# Зина, 3
# Гермиона, 4
# Гермиона, 4
# конец
# Sample Output 2:
# Гермиона 4.0
# Зина 4.0

text = []
d = {}
while True:
    text = input().split(', ')
    if text[0] == "конец":
        break
    d[text[0]] = d.get(text[0], []) + [int(text[1])]
lst = []
# print(d)   # {'Джек': [2, 3], 'Билл': [5, 4, 4, 3]}
for key, val in d.items():
    summ = 0
    for i in range(len(val)):
        summ = summ + val[i]
    average = summ / len(val)
    lst.append((-average, key))
lst_new = sorted(lst)
for i in lst_new:
    print(i[1], -i[0])



# #  -average у lst.append((-average, key))
# text = []
# d = {}
# while True:
#     text = input().split(', ')
#     if text[0] == "конец":
#         break
#     d[text[0]] = d.get(text[0], []) + [int(text[1])]
# lst = []
# lst1 = []
# # print(d)   # {'Джек': [2, 3], 'Билл': [5, 4, 4, 3]}
# for key, val in d.items():
#     summ = 0
#     for i in range(len(val)):
#         summ = summ + val[i]
#     average = summ / len(val)
#     lst1.append((average, key))
#     lst.append((-average, key))
# # !!!!!!!!! чому -average у lst.append((-average, key)) !!!!!!!!!!
# # sorted по замовчуванню сортує по зростанню
# # по першому елементу кортежу: [(2.5, 'Джек'), (4.0, 'Билл')],
# # якщо перші елементи однакові - то сортуання іде тоді по другому елементу ліста/кортежу
# print("lst1", lst1)    # lst1 [(2.5, 'Джек'), (4.0, 'Билл')]
# lst1_new = sorted(lst1)
# print("sorted lst1_new", lst1_new)
# # sorted lst1_new [(2.5, 'Джек'), (4.0, 'Билл')]
#
# print("lst", lst)    # lst [(-2.5, 'Джек'), (-4.0, 'Билл')]
# lst_new = sorted(lst)
# print("sorted lst_new", lst_new)
# # sorted lst_new [(-4.0, 'Билл'), (-2.5, 'Джек')]
#
# for i in lst_new:
#     print(i[1], -i[0])



# №2:
# text = []
# d = {}
# while True:
#     text = input().split(', ')
#     if text[0] == "конец":
#         break
#     if text[0] not in d:
#         d[text[0]] = [int(text[1])]
#     else:
#         d[text[0]] = d[text[0]] + [int(text[1])]
# lst = []
# for key, val in d.items():
#     summ = 0
#     for i in range(len(val)):   # length = len(val)
#         summ = summ + val[i]
#     average = summ / len(val)  # length = len(val)
#     lst.append((-average, key))
# lst_new = sorted(lst)
# for i in lst_new:
#     print(i[1], -i[0])
