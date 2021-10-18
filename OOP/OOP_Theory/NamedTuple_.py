"""
NamedTuple - це також клас, який містить незмінні дані, але у форматі словника,
доступ до яких здійснюється за допомогою ключа/імені (author_1.name), або можна використовувати індекс: author_1[0].
Вони імпортуються з бібліотеки collections.

"""
from collections import namedtuple
Author = namedtuple('author', ['topic', 'name', 'language'])
# де Author - це клас, а ['topic', 'name', 'language'] - перелік змінних
author_1 = Author("ООП частина2", "Ростислав", "Англ.")
# де author_1 - об"єкт класу Author з переліком значень змінних
print(author_1[0])   # доступ до даних через індекс
# ООП частина2
print(author_1.name, ":", author_1.topic)   # доступ до даних по ключу
# Ростислав : ООП частина2


# Create the same class AddressBookDataClass but using NamedTuple:
# class AddressBookDataClass:
#     """
#     Create dataclass with 7 fields:
#     key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
#     """

from collections import namedtuple
AddressBookNamedTuple = namedtuple('AddressBook_', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
ab = AddressBookNamedTuple('10', 'John Smith', '(888) 558-9004', '123 Main St, Pasadena, CA', ' jsmith@comcast.net', '01 January 2000', '21')
print(ab)
# OUTPUT: AddressBookNamedTuple(key='10', name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age='21')
print(ab[0:3])
# OUTPUT: ('10', 'John Smith', '(888) 558-9004')
print('address:', ab.address)
# OUTPUT: address: 123 Main St, Pasadena, CA
