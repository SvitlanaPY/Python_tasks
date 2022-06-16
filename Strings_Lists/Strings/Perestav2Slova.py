# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами.
# Результат запишите в строку и выведите получившуюся строку.

# s = input()
s = 'Hello, world!'
space = s.find(' ')
# print(space)   # 6
slovo1 = s[:space]      # або slovo1 = s[:s.find(' ')]
slovo2 = s[space+1:]    # або slovo2 = s[s.find(' ')+1:]
ss = slovo2 + ' ' + slovo1
print(ss)
