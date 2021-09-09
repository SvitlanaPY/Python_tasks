# STRING FORMATTING:
int_a = 55
int_aa = 77
# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

print('\n"".FORMAT()')
# "".FORMAT()
# 4. With .format and curly braces {}
print("Anna has {1} apples and {0} peaches.".format(int_a, int_aa))
# OUTPUT: Anna has 55 apples and 55 peaches.

print()
# 5. With .format and curly braces {}
print("Anna has {} apples and {} peaches.".format(int_a, int_aa))
# OUTPUT: Anna has 55 apples and 55 peaches.

print()
# 6. By passing index numbers into the curly braces.
print("Anna has {0} apples and {1} peaches.".format(10, 20))
# OUTPUT: Anna has 10 apples and 20 peaches.

print()
# 7.1. By using keyword arguments into the curly braces.
print("Anna has {apples} apples and {peaches} peaches.".format(apples=15, peaches=25))
# OUTPUT: Anna has 15 apples and 25 peaches.

print()
# 7.2. By using keyword arguments into the curly braces.
apples_ = 35
peaches_ = 45
print("Anna has {a} apples and {p} peaches.".format(a=apples_, p=peaches_))
# OUTPUT: Anna has 15 apples and 25 peaches.

print()
# 8*. With indicators of field size (5 chars for the first and 3 for the second)
print("Anna has {0:5} apples and {1:3} peaches.".format(1, 2))
# OUTPUT: Anna has     1 apples and   2 peaches.

print('\n% OPERATOR')
# % OPERATOR
# 10. With % operator
green_apples = 'nine'
ripe_peaches = 55
print("Anna has %s apples and %d peaches." % (green_apples, ripe_peaches))
# OUTPUT: Anna has nine apples and 55 peaches.

print()
# 11*. With variable substitutions by name (hint: by using dict)
app = 5
pch = "two"
fruits_dict = {'one': app, 'two': pch}
print("Anna has %(one)d apples and %(two)s peaches." % fruits_dict)
# OUTPUT: Anna has 5 apples and two peaches.

# F-STRING:
print('\nF-STRINGS')
# 9. With f-strings and variables
apple = 11
peach = "ten"
print(f"Anna has {apple} apples and {peach} peaches.")
# OUTPUT: Anna has 11 apples and ten peaches.

print()
# 12:
name = 'John'
mid_name = 'Ivanov'
balance = 32.56
text = f"Дорогий {name.upper()} {mid_name.upper()}, баланс вашого рахунку складає {balance}грн."
print(text)
text2 = f"Дорогий {name.upper()} {mid_name.upper()}, баланс вашого рахунку подвоївся і тепер складає {balance*2}грн."
print(text2)

print()
# 13:
def func(x):
    return x ** 3
text3 = f"Дорогий {name.upper()} {mid_name.upper()}, ваш виграш складає {func(500)}грн."
print(text3)

print()
# 14:
d = {'name': 'Bob', 'mid_name': 'Smith', 'balance': 1500}
text4 = f"Дорогий {d['name']} {d['mid_name']}, ваш виграш складає {d.get('balance')}грн."
print(text4)   # Дорогий Bob Smith, ваш виграш складає 1500грн.
text5 = f"Шановний {d['name']} {d['mid_name']}, ваш виграш складає {d.get('bal')} грн."
print(text5)   # Шановний Bob Smith, ваш виграш складає None грн.
text6 = f"Дорогий {d['name']} {d['mid_name']}, ваш виграш складає {d.get(('bal'), 0)} грн."
print(text6)    # Дорогий Bob Smith, ваш виграш складає 0 грн.

# print()
# lst_ = [
#     ['Tom', 'Winnie', 1000], ['Jeck', 'Johnson', 2000], ['Diana', 'Smith', 3000]
# ]
# for i in lst_:
#     print(i)
#     ['Tom', 'Winnie', 1000]
#     ['Jeck', 'Johnson', 2000]
#     ['Diana', 'Smith', 3000]


print()
# 15:
lst = [
    ['Tom', 'Winnie', 1000], ['Jeck', 'Johnson', 2000], ['Diana', 'Smith', 3000]
]
for name, midname, balance in lst:
    # print(name, midname, balance)
    text7 = f"Dear {name} {midname}, you have {balance}$"
    print(text7)


print()
# 16:
gender = {'male': 'Шановний', 'female': 'Шановна'}
lst_t = [
    ['Tina', 'Woolf', 1000, 'female'], ['Bill', 'Henk', 2000, 'male'], ['Dorrie', 'Puooh', 3000, 'female']
]
for name, midname, balance, sex in lst_t:
    # print(name, midname, balance)
    text8 = f"{gender[sex]} {name} {midname}, у вас {balance}$ бонусів"
    print(text8)


print()
# 17: Необходимо вывести результат трех видов деления первого числа на второе в определенном формате
# Sample Input 1:
# 11
# 5
# Sample Output 1:
# 11 / 5 = 2.2
# 11 // 5 = 2
# 11 % 5 = 1
a, b = int(input("Enter val1: ")), int(input("Enter val2: "))
print(f'{a} / {b} = {a / b}\n{a} // {b} = {a // b}\n{a} % {b} = {a % b}')
