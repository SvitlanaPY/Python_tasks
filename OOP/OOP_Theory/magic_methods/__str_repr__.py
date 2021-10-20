"""
magic methods = dunder methods (Double UNDERscore) -
це спеціальні методи, які починаються і закінчуються на два нижніх підкреслення.
Ці методи мають певний функціонал і викликаються всередині класу у певний момент.

Обидва ці методи відповідають за текстове представлення нашого об"єкта в системі:
__repr__ буде відповідати за те, як будуть бачити розробники наш екземпляр класу,
__str__ буде відповідати за те, як наш метотод буде відображатись, якщо до нього застосувати такі ф-ії як str() чи print

repr - для серіалізації та відладки, є виводом, який є читабельним для інтерпретатора Python.
__repr__ дає строку, оціночне строкове представлення об'єкта.
# >>> x = 'foo'
# >>> x.__repr__()
"'foo'"
# >>> repr(x)
"'foo'"

str - використовується для створення виводу, який має бути читабельним для кінцевого користувача,
це по суті є print()
# >>> str('hello world')
'hello world'
__str__ викликаєттся, коли ми наш об"єкт передаємо у ф-ію print():
hum = Human('СВІТЛАНА')
print(hum)
----------
# >>> repr('hello world')
"'hello world'"
"""

class Human:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person has name {self.name}"

    def __str__(self):
        return f"My name is {self.name}"

    def info(self):
        print(self)

hum = Human('СВІТЛАНА')
hum.info()
# викличеться метод __str__, а не __repr__ і виведе на друк:
# My name is СВІТЛАНА
print("hum: ", hum)
# hum:  My name is СВІТЛАНА


import datetime
today = datetime.datetime.now()
print(str(today))    # 2021-08-30 18:49:00.352057
print(repr(today))   # datetime.datetime(2021, 8, 30, 18, 49, 0, 352057) - официальное представление обєкта дати


# >>> str('hello world')
# 'hello world'
# >>> repr('hello world')
# "'hello world'"


class Lion:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Lion - {self.name}"

    def __repr__(self):
        return f"The object Lion - {self.name}"


q = Lion('Vasya')
>>> q   # звертаємось до об"єкта у консолі напряму, то спрацьовує __repr__
# The object Lion - Vasya
str(q)
# 'Lion - Vasya'
print(q)
# Lion - Vasya


"""
8. class AddressBook:
     Create regular class taking 7 params on __init__ - key, name, phone_number, address, email, birthday, age
     Make its str() representation the same as for AddressBookDataClass defined:
AddressBookDataClass(key=10, name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age=21)
"""

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"AddressBook(key={self.key}, name='{self.name}', phone_number='{self.phone_number}', address='{self.address}', email='{self.email}', birthday='{self.birthday}', age='{self.age}')"

a_b = AddressBook(10, 'John Smith', '(888) 558-9004', '123 Main St, Pasadena, CA', ' jsmith@comcast.net', '01 January 2000', 21)
print(a_b)
# OUTPUT: AddressBook(key=10, name='John Smith', phone_number='(888) 558-9004', address='123 Main St, Pasadena, CA', email=' jsmith@comcast.net', birthday='01 January 2000', age='21')


"""
9. Override a printable string representation of the City class and return: 
The population of the city {name} is {population}
"""

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population
    def __str__(self):
        return f"The population of the city {self.name} is {self.population}"

c = City('City3', 1000000)
print(c)
# OUTPUT: The population of the city City3 is 1000000
