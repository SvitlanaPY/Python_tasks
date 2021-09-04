# Представьте, у нас есть список товаров и их стоимость, но мы хотим взглянуть на него в отсортированном виде.
# Вверху хотим видеть самые дорогие товары, внизу самые дешевые
# Программа будет принимать строки, в которых сперва указывается название товара,
# а затем через двоеточие с пробелом его цена - целое положительное число.
# Строка "конец" означает списка товаров и соответственно окончание ввода.
# Все товары имеют уникальные названия, цены не дублируются.
# Ваша задача вывести список товаров по уменьшению цены.

# Sample Input:
# Sony PlayStation 5: 46000
# Телевизор QLED Samsung QE65Q60TAU: 87090
# Смартфон Samsung Galaxy A11: 10000
# Планшет Samsung Galaxy Tab S6: 26600
# конец
#
# Sample Output:
# Телевизор QLED Samsung QE65Q60TAU
# Sony PlayStation 5
# Планшет Samsung Galaxy Tab S6
# Смартфон Samsung Galaxy A11

text = input().split(': ')
d = {}
while text != ['конец']:
    key = int(text[1])
    d[key] = text[0]
    text = input().split(': ')
for i in sorted(d, reverse=True):
    print(d[i])
#
# використання sorted() до словника:
# print(sorted(d))   # [10000, 26600, 46000, 87090]
# for i in sorted(d, reverse=True):
#     print(i, d[i])
# 87090 Телевизор QLED Samsung QE65Q60TAU
# 46000 Sony PlayStation 5
# 26600 Планшет Samsung Galaxy Tab S6
# 10000 Смартфон Samsung Galaxy A11



# №2:
# text = input().split()
# d = {}
# while text != ['конец']:
#     key = int(text[-1])
#     d[key] = text[:-1]
#     text = input().split()
# for k, v in sorted(d.items(), reverse=True):
#     t = ' '.join(v)
#     print(t[:-1])

# print(d.items())
# dict_items([(46000, ['Sony', 'PlayStation', '5:']), (87090, ['Телевизор', 'QLED', 'Samsung', 'QE65Q60TAU:']), (10000, ['Смартфон', 'Samsung', 'Galaxy', 'A11:']), (26600, ['Планшет', 'Samsung', 'Galaxy', 'Tab', 'S6:'])])

# print(sorted(d.items()))   # sorting by key
# [(10000, ['Смартфон', 'Samsung', 'Galaxy', 'A11:']), (26600, ['Планшет', 'Samsung', 'Galaxy', 'Tab', 'S6:']), (46000, ['Sony', 'PlayStation', '5:']), (87090, ['Телевизор', 'QLED', 'Samsung', 'QE65Q60TAU:'])]

# for k, v in sorted(d.items(), reverse=True):
#     print(k, v)
#     # 87090 ['Телевизор', 'QLED', 'Samsung', 'QE65Q60TAU:']
#     # 46000 ['Sony', 'PlayStation', '5:']
#     # 26600 ['Планшет', 'Samsung', 'Galaxy', 'Tab', 'S6:']
#     # 10000 ['Смартфон', 'Samsung', 'Galaxy', 'A11:']
#     t = ' '.join(v)
#     print(t[:-1])
#     # Телевизор QLED Samsung QE65Q60TAU
#     # Sony PlayStation 5
#     # Планшет Samsung Galaxy Tab S6
#     # Смартфон Samsung Galaxy A11
