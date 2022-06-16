# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов. Используйте для решения задачи метод count

# works wrong when sentence ends with space
# s = input()
s = "hello world! I am learning python! "
print(s.count(' ') + 1)   # 7

# sss = input("Enter some sentence: ")   # hello world! I am learning python!
sss = 'hello world! I am learning python! '
sss = sss.split()
# print(sss)  # ['hello', 'world!', 'I', 'am', 'learning', 'python!']
print(len(sss))   # 6
# Подсчитывает количество вхождений одной строки в другую строку. Простейшая форма вызова S.count(T)  возвращает число вхождений строки T внутри строки S.
# При этом подсчитываются только непересекающиеся вхождения
# При указании трех параметров S.count(T, a, b), будет выполнен подсчет числа вхождений строки T в срезе S[a:b].

# подсчитать сколько раз в строке встречается латинская буква "e" (учитывать как маленькие, так и заглавные буквы)
s2 = 'Elen, hello!'
print(s2.count('e') + s2.count('E'))   # 3

