# Задача «Словарь синонимов»
# Вам дан словарь, состоящий из пар слов.
# Каждое слово является синонимом к парному ему слову.
# Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
# INPUTS:
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
# OUTPUTS:
# Bye

n = int(input())
d = {}
for i in range(n):
    key, val = input().split()
    d[key] = val
word = input()
for key, val in d.items():
    if word == val:
        print(key)
    elif word == key:
        print(val)

# №2:
# n = int(input())
# d = {}
# for i in range(n):
#     key, val = input().split()
#     d[key] = val
# word = input()
# for key in d:
#    if word == key:
#        print(d[key])
#    if word == d[key]:
#        print(key)
