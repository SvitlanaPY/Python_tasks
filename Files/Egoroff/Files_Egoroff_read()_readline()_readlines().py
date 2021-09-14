file1 = open('111.txt', encoding='utf-8')
# ф-ія open() приймає 2 параметри:
# 1. шлях до файлу + імя файлу, або лише імя файлу, якщо файл знах-ся у папці зі скріптом;
# 2. режим/ модифікатор доступу до файлу (r, w, a, r+, w+, rb, wb, ab, x)
# /home/svitlana/Projects/Python_Tasks/Files/Egoroff/111.txt  - абсолютний шлях до файлу
# при використанні абсолютного шляху варто не забувати про службові символи, і додавати перед шляхом r,
# щоб вказати пайтому, що в даній стрічці НЕмає службових символів і стрічку виводити як вона є (сирою: r = raw)
# file1 = open(r'1/home/svitlana/Projects/Python_Tasks/Files/Egoroff/111.txt', encoding='utf-8')

# print(file.read())   # read ALL text from '111.txt' file

print(file1.read(7))   # read only first SEVEN symbols from '111.txt' file remembering the possition of the last read symbol
# Краєм с
print(file1.read(4))   # continue reading the file starting from the possition of the last read symbol (from 7)
# віту

file1.seek(0)   # ставимо в позицію нуль, і зчитування почнеться зпочатку знову
print(file1.read(11))
# Краєм світу


file3 = open('333.txt')
print(file3.readline())
# метод readline() зчитує стрічку цілком, не приймає параметрів, запамятовуючи позицію,
# на якій зупинилось зчитування і при наступному виклику цього метода, вже зчитається наступний рядок,
# розділяючи пробілом рядки, бо кожна стрічка закінчується службовим символом переносу стрічки - \n
# First Line
print(file3.readline())
# Second Line


# метод readlines() повертає список, елементами якого будуть рядки із символом переносу рядка - \n
file4 = open('333.txt')
x = file4.readlines()
print(x)
# print(file4.readlines())
# ['First Line\n', 'Second Line\n', 'Third Line']
