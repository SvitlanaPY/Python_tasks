# Дана строка, состоящая из слов, разделенных пробелами.
# Определите, сколько в ней слов. Используйте для решения задачи метод count

# s = input()
s = 'hello world! I am learning python!'
print(s.count(' ') + 1)

# Подсчитывает количество вхождений одной строки в другую строку. Простейшая форма вызова S.count(T)  возвращает число вхождений строки T внутри строки S.
# При этом подсчитываются только непересекающиеся вхождения
# При указании трех параметров S.count(T, a, b), будет выполнен подсчет числа вхождений строки T в срезе S[a:b].

# подсчитать сколько раз в строке встречается латинская буква "e" (учитывать как маленькие, так и заглавные буквы)
s = 'Elen, hello!'
print(s.count('e') + s.count('E'))   # 3

