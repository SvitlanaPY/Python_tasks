# метод read() - зчитує файл і повертає строкове його предаставлення, додаючи символ переносу рядка;
# якщо НЕ приймає параметрів - то зчитується ВЕСЬ файл
# параметр вказує на к-сть символів, які потрібно зчитати, запам"ятовуючи місце останнього зчитаного,
# при наступному виклику read() зчитування буде продовжуватись із місця, останнього зчитаного символа
f = open('333.txt')
# print(type(f))   # <class '_io.TextIOWrapper'>
x = f.read(5)
print("read first 5 symbols:  ")
print(x)
# First

f = open('333.txt')
y = f.read()
print("read ALL file")
print(y)

# метод read() - повертає строкове предаставлення зчитаного тексту із символ переносу рядка;
f_ = open('333.txt')
yy = f_.read()
print("repr yy: ", repr(yy))
# 'First Line\nSecond Line\nThird Line'


# метод readlines() повертає список, елементами якого будуть рядки із символом переносу рядка - \n
file = open('333.txt')
c = file.readlines()
print("c: ", c)
# print(file.readlines())
# c:  ['First Line\n', 'Second Line\n', 'Third Line']


# щоб видалити службовий символ переносу рядку - метод splitlines():
ff = open('test.txt')
z = ff.read()
print("z: ", z)
print("type(z): ", type(z))   # <class 'str'>
print("z: ", repr(z))    # виводимо представлення z у якості строки; z - буде строка
# z:  'First Line\nSecond Line\nThird Line'
# до строки можна застосувати метод splitlines(), який розбиває нашу строку/текст на стрічки і запихає в list без \n
# метод splitlines() - повертає список (list) всіх рядків БЕЗ службового символу переносу строки (без \n)
zz = z.splitlines()
print("zz: ", zz)
# ['First Line', 'Second Line', 'Third Line']
# z = ff.read().splitlines()


# метод readline() - зчитує по рядку і повертає строкове представлення зчитаного рядка;
fff = open('333.txt')
q = fff.readline()
print("type(q): ", type(q))
print("q: ", q)
print("зчитаний ОДИН рядок - q: ", repr(q))
# зчитаний ОДИН рядок - q:  'First Line\n'
# метод строки rstrip() видаляє справа в строці всі пробільні символи і символи переносу строки, повернеться строка
qq = q.rstrip()
print("qq: ", qq)
# First Line
# q = fff.readline().rstrip()


f.close()
f_.close()
ff.close()
file.close()
fff.close()
