"""
NamedTuple (іменований кортеж) - це також клас, який містить незмінні дані, але у форматі кортежу,
доступ до яких здійснюється по імені/атрибуту (author_1.name), або по індексу: author_1[0].

Вони імпортуються з бібліотеки collections.
Команда namedtuple створює клас з переліком атрибутів і
цей створений клас зберегають в змінну як правило із такою ж назвою, що і назва створюваного клкасу.
А вже через цю змінну далі створюється екземпляр класу.
Наша змінна буде також належати до кортежу: print(isinstance(<назва змінної>, tuple))
і в неї є методи, які належать до кортежу: print(dir(<назва змінної>))

"""
from collections import namedtuple
Author = namedtuple('Author', ['topic', 'name', 'language'])
"""
де Author - це клас, а далі іде перелік атрибутів цього класу - ['topic', 'name', 'language']
команда namedtuple('Author', ['topic', 'name', 'language']) - створює клас Author з переліком атрибутів
(які записуються в ліст чи в строку) і це все потрібно буде десь зберегти, і як правило зберігають в змінній з такою ж назвою як назва класу
(імя змінної, яка стоїть зліва = ім"я класу, що стоїть справа: Author = namedtuple('Author', ...)
"""
author_1 = Author("ООП частина2", "Ростислав", "Англ.")
# де author_1 - об"єкт класу Author з переліком значень атрибутів
print(author_1[0])   # доступ до даних через індекс
# ООП частина2
print(author_1.name, ":", author_1.topic)   # доступ до даних по імені/атрибуту
# Ростислав : ООП частина2


Author_new = namedtuple('Author_new', 'topic name language')
# перелік імен атрибутів можна вказувати в лісті, чи в стрічці, чи в кортежі...
author_2 = Author_new('OOP part 2', 'Rostyslav', 'EN')
print(author_2[0])     # OOP part 2
print(author_2.name)   # Rostyslav

print()
author_3 = Author_new(topic='OOP part 3', name='Svitlana', language='Ukr')
print(author_3[0])   # OOP part 3
print(author_3[1])   # Svitlana
print(author_3[2])   # Ukr


print('$ '*20)
Human = namedtuple('Person', 'name surname date country age id')
# в Human міститься посилання на клас Person,
# і тепер через змінну Human ми будемо створювати екземпляру класу
person_1 = Human('Megan', 'Jones', '1988-10-24', 'Bolivia', "10", "10")

# наша змінна person_1 є також кортежем
print(isinstance(person_1, tuple))    # True
# отже в неї є методи, які належать до кортежу, а також є інші специфічні методи (напр. _asdict())
print(dir(person_1))
print(person_1.count('10'))   # 2
print(person_1._asdict())
# {'name': 'Megan', 'surname': 'Jones', 'date': '1988-10-24', 'country': 'Bolivia', 'age': 10, 'id': 10}

# ми можемо доступатись до атрбутів по імені:
print(person_1.age, person_1.name, person_1.date)   # 10 Megan 1988-10-24

# но ми НЕ можемо змінювати значення цих атрибутів:
# person_1.name = "Анна"    # AttributeError: can't set attribute

# але існує закритий метод _replace(), за допомогою якого ми все ж можемо змінити значення атрибутів
person_1 = person_1._replace(name="АННА")
print(person_1.name)
print(person_1)
# Person(name='АННА', surname='Jones', date='1988-10-24', country='Bolivia', age=10, id=10)


print("* "*20)
# Create the same class AddressBookDataClass but using NamedTuple:
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields:
#     key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """

from collections import namedtuple
AddressBookNamedTuple = namedtuple('AddressBookNamedTuple', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
ab = AddressBookNamedTuple('10', 'John Smith', '(888) 558-1004', '123 Main St, Pasadena, CA', ' jsmith@comcast.net', '01 January 2000', '10')
print(ab)
# OUTPUT: AddressBookNamedTuple(key='10', name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age='21')
print(isinstance(ab, tuple))
# True
# оск ab - це кортеж, то ми можемо робити зрізи і застосвувати методи кортежів
print(ab[0:3])
# OUTPUT: ('10', 'John Smith', '(888) 558-9004')
print(ab.count('10'))
# 2
print('address:', ab.address)
# OUTPUT: address: 123 Main St, Pasadena, CA


print("!-"*20)
from typing import NamedTuple
from datetime import datetime

class Personn(NamedTuple):
    id: int
    name: str
    surname: str
    date: datetime
    country: str
    age: int

z = Personn(10, 'Megan', 'Jones', datetime(2002, 12, 4, 20, 30, 00), 'Bolivia', 10)
# print(datetime.now())
print(z.id)   # 10
print(z.name, z.surname)   # Megan Jones
print(z.date)   # 2002-12-04 20:30:00
print(z.country)   # Bolivia
print(z.age)   # 10
