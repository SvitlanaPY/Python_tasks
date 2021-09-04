# Задача «Продажи»
# Дана база данных о продажах некоторого интернет-магазина.
# Каждая строка входного файла представляет собой запись вида Покупатель товар количество,
# где Покупатель — имя покупателя (строка без пробелов),
# товар — название товара (строка без пробелов), количество — количество приобретенных единиц товара.
#
# Создайте список всех покупателей,
# а для каждого покупателя подсчитайте количество приобретенных им единиц каждого вида товаров.
# Список покупателей, а также список товаров для каждого покупателя нужно выводить в лексикографическом порядке.

# INPUTS1:
# Ivanov paper 10
# Petrov pens 5
# Ivanov marker 3
# Ivanov paper 7
# Petrov envelope 20
# Ivanov envelope 5
# OUTPUTS1:
# Ivanov:
# envelope 5
# marker 3
# paper 17
# Petrov:
# envelope 20
# pens 5

d = {}
text = input()
while True:
    try:
        name, product, amount = text.split()
        if name not in d:
            d[name] = dict({product: int(amount)})
        else:
            d[name][product] = d[name].get(product, 0) + int(amount)
        text = input()
    except (ValueError, EOFError):
        break

for name in sorted(d.keys()):
    print(name + ":")
    for product in sorted(d[name].keys()):
        print(product, d[name][product])
