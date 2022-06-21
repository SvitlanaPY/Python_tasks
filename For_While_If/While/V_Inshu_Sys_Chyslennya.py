"""  Перевести число в 2-ову систему числення  """
x = int(input())
new_num = []
while x > 0:
    last_num = x % 2   # де 2 - це двійкова система числення;
    new_num.append(last_num)
    x = x // 2
new_num.reverse()
print(*new_num)


"""  Перевести число в 5-ову систему числення  """
# x = int(input())
# new_num = []
# while x > 0:
#     last_num = x % 5   # де 5 - це 5-ова система числення;
#     new_num.append(last_num)
#     x = x // 5
# new_num.reverse()
# print(*new_num)


"""  Перевести число в 16-ову систему числення  """
# x = int(input())
# new_num = []
# while x > 0:
#     last_num = x % 16   # де 16 - це 16-ова система числення;
#     new_num.append(last_num)
#     x = x // 16
# new_num.reverse()
# print(*new_num)


"""   ПОЯСНЕННЯ АЛГОРИТМУ   """
# x = int(input())
# new_num = []
# while x > 0:
#     last_num = x % 2   # де 2 - це двійкова система числення;
#     print(last_num)   # - виводимо цифри з кінця
#     new_num.append(last_num)
#     x = x // 2
#     print(x)
# new_num.reverse()
# print(*new_num)
