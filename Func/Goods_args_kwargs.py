def print_goods(*args):
    listt = []
    for i in range(len(args)):
        if str(args[i]).isalpha() and (str(args[i]) not in ('True', 'False')):
            listt.append(args[i])
        # elif str(args[i]).isdigit() and (str(args[i]) not in ('True', 'False')):
        #     continue
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
# print(print_goods('apple', 'banana', 'orange'))
# print(print_goods(1, True, 'Грушечка', '', 'Pineapple'))
# print(print_goods([], {}, 1, 2))


# №3:
# def print_goods(*args):
#     count = 0
#     for a in args:
#         if isinstance(a, str) and a != '' and a != ' ':   # = if type(a) is str and a != '' and a != ' ':
#             count += 1
#             print(str(count) + '.', a)
#     if count == 0:
#         print('Нет товаров')