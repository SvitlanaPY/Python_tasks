# Метод — это функция, применяемая к объекту, в данном случае — к строке.
# Метод вызывается в виде:  Имя_объекта.Имя_метода(параметры).
# Например, S.find("e") — это применение к строке S метода find с одним параметром "e".


# 3.1. Методы find и rfind
# Метод find находит в данной строке (к которой применяется метод) данную подстроку
# (которая передается в качестве параметра). Функция возвращает индекс первого вхождения искомой подстроки.
# Если же подстрока не найдена, то метод возвращает значение -1.
#
# Аналогично, метод rfind возвращает индекс последнего вхождения данной строки (“поиск справа”).
# Если вызвать метод find с тремя параметрами S.find(T, a, b), то поиск будет осуществляться в срезе S[a:b].
# Если указать только два параметра S.find(T, a), то поиск будет осуществляться в срезе S[a:],
# то есть начиная с символа с индексом a и до конца строки.
# Метод S.find(T, a, b) возращает индекс относительно строки S, а не индекс относительно среза S[a:b].
w = 'abrakadabrakaaba'
print('index k1 = ', w.find('k', 1, 7))   # 4
print('index k2 = ', w.find('k', 5, 13))  # 11

# 3.2. Метод replace
# Метод replace заменяет все вхождения одной строки на другую.
# Формат: S.replace(old, new) — заменить в строке S все вхождения подстроки old на подстроку new.
#
# Если методу replace задать еще один параметр: S.replace(old, new, count), то заменены будут не все вхождения,
# а только не больше, чем первые count из них.


# 3.3. Метод count
# Подсчитывает количество вхождений одной строки в другую строку. Простейшая форма вызова S.count(T)  возвращает число вхождений строки T внутри строки S.
# При этом подсчитываются только непересекающиеся вхождения.
# При указании трех параметров S.count(T, a, b), будет выполнен подсчет числа вхождений строки T в срезе S[a:b].
s = 'hello world'
print('count "a" is: ', s.count('a'))   # 0
print('count "l" is: ', s.count('l'))   # 3
print('count "l" is: ', s.count('l', 3))   # 2
print('count "l" is: ', s.count('l', 4, len(s) + 1))   # 1


d = '111'
print(d.rjust(7, '0'))   # 0000111

q = '   hello   \n'
print(q.strip())   # hello
# .strip() - видаляє зі строки всі пробіли і переноси на нову строку зліва і справа


nn = input("Enter few words (hello hello hello): ").upper().replace(' ', '!!!')
print(nn)   # HELLO!!!HELLO!!!HELLO

m = 'ivanov ivan ivanovych'
print(m.split())   # ['ivanov', 'ivan', 'ivanovych']
print(len(m.split()))   # 3

ip = '192.168.0.105'
tt = ip.split('.')
print(tt)   # ['192', '168', '0', '105']

tt_ = "==".join(tt)
print(tt_)   # 192==168==0==105

print(",,,".join(ip.split('.')))   # 192,,,168,,,0,,,105

# text = 'Smells Like Teen Spirit'
print(",".join(input("Enter text (Smells Like Teen Spirit): ").split()))   # Smells,Like,Teen,Spirit
