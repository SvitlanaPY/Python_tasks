import pprint
"""
ОБ"ЄКТ - це контейнер, який склад-ся із:
- даних (атрибути/змінн)
- поведінки (методи/ф-ії)
Атрибути, як правило визначаються/задаються в __init__, це змінні, які ми передаємо класу чи ф-ії
а поведінка/ф-ії реалізовуємо в методах. До атрибутів класу можна звернутись зерез крапку
Метод - це ф-ія, яка застосовується до об"єкту.
Методі викликаються: <імя об"єкту>.<імя методу>(аргументи/параметри).
Кожен об"єкт належить певному класу і це перевіряється за дом ф-ії type
"""
s = 'abcd'
print(type(s))   # <class 'str'>

"""
Також приналежність об"єкти до певного класу можна перевірити за допомогою ф-ії isinstance()
першим параметром передається сам об"єкт,  який ми хочемо перевірити, 
а другим параметром передається клас, який ми перевіряємо
"""
print(isinstance(4, int))
# True

"""
За допомогою ф-ії isinstance() ми можемо перевірити, що кожне значення в пайтоні представляє собою об"єкт
"""
print(isinstance(4, object))
# True

# самі класи теж є об"єктами:
print(isinstance(int, object))
# True
print(type(str))
# <class 'type'>

"""
КЛАС - це шаблон, за допомогою якого створюються об"єкти. Вони описують поведінку об"єкта даного класу.
Це механізм і синтаксис для опису власних типів даних.
Створюючи об"єкт певного класу, цьому об"єкту під капотом надається певна поведінка(методи класу).
Кожен клас має конструктор - механізм, яким створюються нові об"єкти/екземпляри класу
Створивши клас, ми можемо викликати в ньому конструктор: CarNew()
а також можемо звертатись до атрибутів створеного класу: CarNew.model
"""

class Car:
    pass

a = Car()
# щоразу, викликаючи клас, результатом буде повернення екземпляру класу
print(type(a))
# <class '__main__.Car'>   --- наша змінна а є екземпляром класу Car
print(isinstance(a, Car))   # наша змінна а є екземпляром класу Car
# True
