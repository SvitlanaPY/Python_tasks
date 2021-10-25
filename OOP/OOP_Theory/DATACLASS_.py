"""
DataClass - це такий тип класу, який використовується для зберігання даних без будь-яких функціональних можливостей;
методів чи якогось функціоналу у ньому не може бути, він лише як сховище даних.
Ці DataClass-и вони є mutable, та імпортуються з бібліотеки dataclasses.

Це такий контейнер, сховище, де зберігаємо дані, така собі БД.
Ці класи - це звичайні класи, основна мета яких полягає в збереженні даних в одному конкретному місці не знаючи логіки програми.
Маючи DataClass досить легко пеевіряти типи даних, здійснювати пошук.

Бібліотека DataClass є вбудована, але її треба імпортнути: import dataclasses
Також потрібно використати декоратор @dataclasses.dataclass.
А далі описуємо наш DataClass-клас, який нам слугує шаблоном і далі створюємо об"єкт цього класу.

У DataClass доступ до даних відбув-ся через крапку:
artcl1 = Article("OOP Lecture #2", 'Rostyslav Kitsylinskyy', 'EN', 'CURSOR', 17)
print(artcl1.page)
На відміну від словників, DataClass дозволяють визначити/задати тип даних,
хоча він не є обовязковим і помилка не видається, коли дані будуть іншого типу.

Можна дані зберігати і в звичайному словнику, замість DataClass:
article_dict = {
    "topic": "OOP Lecture #2",
    "contributor": "Rostyslav Kitsylinskyy"
    "language": "EN"
    "author": "CURSOR"
    "page": 17
    }
У словниках досиуп до даних складніший - по ключу:
article_dict['page']

"""

import dataclasses
@dataclasses.dataclass
class Article:
    topic: str
    contributor: str
    language: str
    author: str
    page: int


artcl1 = Article("OOP Lecture #2", 'Rostyslav Kitsylinskyy', 'EN', 'CURSOR', 17)
print(artcl1)
# Article(topic='OOP Lecture #2', contributor='Rostyslav Kitsylinskyy', language='EN', author='CURSOR', page=17)
print(artcl1.page)
# 17


"""
Ці DataClass-и вони є mutable.
"""
print("page_before change: ", artcl1.page)   # page_before change:  17
artcl1.page = 25
print("page_after change: ", artcl1.page)   # page_after change:  25


"""
DataClass можна зробити immutable - Frozen dataclass:
потрібно використати декоратор @dataclasses.dataclass(frozen=True)
"""
@dataclasses.dataclass(frozen=True)
class Book:
    title: str
    author: str

book1 = Book("Lisova Pisnya", "Lesya Ukrainka")
# book1.author = "Shevchenko"   # dataclasses.FrozenInstanceError: cannot assign to field 'author'
book2 = Book("Kobzar", "Taras Shevchenko")

books = (book1, book2)
for b in books:
    print(f'I read "{b.title}" written by {b.author}.')
# I read "Lisova Pisnya" written by Lesya Ukrainka
# I read "Kobzar" written by Taras Shevchenko

"""
Можемо створити якийсь клас і в ньому зробити об"єкти DataClass-у
"""
class Car:
    book1 = Book("Lisova Pisnya", "Lesya Ukrainka")
    book2 = Book("Kobzar", "Taras Shevchenko")



print("@ "*15)
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields:
#     key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """

from dataclasses import dataclass

@dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

address_book = AddressBookDataClass(101,
                               'John Smith',
                               '(888) 558-9004',
                               '123 Main St, Pasadena, CA',
                               ' jsmith@comcast.net',
                               '01 January 2000',
                               21)
print(address_book)
# OUTPUT: AddressBookDataClass(key=10, name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age=21)
print(address_book.name)
# OUTPUT: John Smith
