# Перевірка умов ДО першого True, після True всі решту за ним умови НЕ перевірятимуться.
# day = int(input())
# if day == 1:
#     print("Monday")
# elif day == 2:
#     print("Tuesday")
# elif day == 3:
#     print("Wednesday")
# elif day == 4:
#     print("Thursday")
# elif day == 5:
#     print("Friday")
# elif day == 6:
#     print("Saturday")
# elif day == 7:
#     print("Sunday")
# else:
#     print("ERROR")
# print("end")


# КОЖНА умова перевіриться!
# day = int(input())
# if day == 1:
#     print("Monday")
# if day == 2:
#     print("Tuesday")
# if day == 3:
#     print("Wednesday")
# if day == 4:
#     print("Thursday")
# if day == 5:
#     print("Friday")
# if day == 6:
#     print("Saturday")
# if day == 7:
#     print("Sunday")
# else:
#     print("ERROR")
# print("end")

a = int(input())
if a < 0 or a >= 10000:
    print("ERROR!")
elif a < 10:
    print("1 digit")
elif a < 100:
    print("2 digits")
elif a < 1000:
    print("3 digits")
elif a < 10000:
    print("4 digits")
