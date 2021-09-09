def print_goods(*args):
    listt = []
    for i in range(len(args)):
        if str(args[i]).isalpha() and (str(args[i]) not in ('True', 'False')):
            listt.append(args[i])
    if len(listt) == 0:
        print("Нет товаров")
    else:
        for i in range(len(listt)):
            print(i + 1, '. ', listt[i], sep='')

# print(print_goods('apple', 'banana', 'orange'))
print(print_goods(1, True, 'Грушечка', '', 'Pineapple'))
# print(print_goods([], {}, 1, 2))


# №2
# def print_goods(*args):
#     k = 0
#     listt = []
#     for i in args:
#         i = str(i)
#         if i.isalpha() and (i not in ('True', 'False')):
#             k += 1
#             listt.append(i)
#     if len(listt) == 0:
#         print("Нет товаров")
#     else:
#         for i in range(len(listt)):
#             print(i + 1, '. ', listt[i], sep='')



# №3:
# def print_goods(*args):
#     count = 0
#     for a in args:
#         if isinstance(a, str) and a != '' and a != ' ':   # = if type(a) is str and a != '' and a != ' ':
#             count += 1
#             print(str(count) + '.', a)
#     if count == 0:
#         print('Нет товаров')



# Давайте теперь создадим функцию print_goods, которая печатает список покупок.
# На вход она будет принимать произвольное количество значений, а товаром мы будем считать любые непустые строки.
# То есть числа, списки, словари и другие нестроковые объекты вам нужно будет проигнорировать.
# Функция print_goods должна печатать список товаров в виде: <Порядковый номер товара>.
# <Название товара> (см. пример ниже).
# В случае, если в переданных значениях не встретится ни одного товара, необходимо распечатать текст "Нет товаров"
#
# print_goods('apple', 'banana', 'orange')
# """ данный вызов печатает следующие строки
# 1. apple
# 2. banana
# 3. orange
# """
# print_goods(1, True, 'Грушечка', '', 'Pineapple')
# """ Этот вызов распечатает следующее
# 1. Грушечка
# 2. Pineapple
# """
# print_goods([], {}, 1, 2)
# """ Этот вызов распечатает следующее
# Нет товаров
# """