# перевести число в 2-ову систему числення:
x = int(input())
new_num = ''
while x > 0:
    last_num = x % 2   # де 2 - це двійкова система числення;
    print(last_num)   # - виводимо цифри з кінця
    new_num = new_num + str(last_num)
    x = x // 2
    print(x)
print(new_num)

# перевести число в 16-ову систему числення:
# x = int(input())
# new_num = ''
# while x > 0:
#     last_num = x % 16   # де 16 - це 16-кова система числення;
#     print(last_num)   # - виводимо цифри з кінця
#     new_num = new_num + str(last_num)
#     x = x // 16
# print(new_num)

