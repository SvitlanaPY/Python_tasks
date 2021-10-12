"""
@STATICMETHOD

Якщо створити звичайну ф-ію всередині класу Example (наприклад def hello(): ....),
то її можна викликати від самого класу : Example.hello()
но не можемо викликати цю ф-ію від екземпляра класу:
ex = Example();
ex.hello()  ===> виникає TypeError: hello() takes 0 positional arguments but 1 was given

Щоб ми могли викликати функцію від екземплярів, ми створюємо методи, наприклад (def instance_hello(self): ..... ):
тепер ми можемо викликати наш метод/ф-ію def instance_hello() від екземпляра:
ex2 = Example();
ex2.instance_hello()
але не можемо викликати наш метод/ф-ію def instance_hello() від класу:
Example.instance_hello()  ===> виникає # TypeError: instance_hello() missing 1 required positional argument: 'self'

Щоб функцію можна було викликати як від класу, так і від екземпляра класу - потрібно створити staticmethod
Щоб функція визначилась як staticmethod, потрібно на ф-ію повісити відповідний декоратор: @staticmethod
Коли ми створюємо статік-метод, то він не прив"язується ні до класу, ні до екземпляру класу і
ми можемо спокійно викликати цей метод як у класу, так і в екземплярів класу

Статік метод можна використовувати тоді, коли нам потрібна звичайна функція,
но ми хочемо реалізувати її всередині класу, а не виносити її поза клас.
"""

class Example:
    def hello():    # можемо викликати від класу, но не можемо викликати від екземпляра класу
        print('hello')

    def instance_hello(self):   # можемо викликати від екземпляра класу, но не можемо викликати від класу
        print(f'функція instance_hello {self}')

    @staticmethod
    def static_hello():
        print('static_hello')


print(Example.hello)
# <function Example.hello at 0x7f490bdb38b0>
ex = Example()
print(ex.hello)   # <bound method Example.hello of <__main__.Example object at 0x7fb58a427fa0>>

print()

# викликаємо ф-ію hello() від класу Example:
Example.hello()   # hello
# викликаємо ф-ію hello()  від екземпляра ex:
# ex.hello()    # TypeError: hello() takes 0 positional arguments but 1 was given

print()

ex2 = Example()
# викликаємо ф-ію instance_hello()  від екземпляра ex2:
ex2.instance_hello()   # функція instance_hello <__main__.Example object at 0x7fab36304b80>
# викликаємо ф-ію instance_hello() від класу Example:
# Example.instance_hello()   # TypeError: instance_hello() missing 1 required positional argument: 'self'

print()

ex3 = Example()
# викликаємо ф-ію instance_hello()  від екземпляра ex3:
ex3.static_hello()    # static_hello
# викликаємо ф-ію static_hello() від класу Example:
Example.static_hello()    # static_hello


print('\n########## 3 ##########')
# class Calc:
#     """
#     Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#     Note: this method should be static
#     """

class Calc:

    @staticmethod
    def add_nums(a, b, c):
        return a + b + c

addnums = Calc()
print(addnums.add_nums(1, 2, 3))
# OUTPUT: 6
print(Calc.add_nums(1, 2, 3))
# OUTPUT: 6


print()
class Calc:

    @staticmethod
    def add_nums(*args):
        return sum(args)

addnums = Calc()
print(addnums.add_nums(6, 2, 3, 5))   # виклик ф-ії "add_nums" від екземпляра класу
# OUTPUT: 16

print(Calc.add_nums(6, 2, 3, 5))   # виклик ф-ії "add_nums" від класу
# OUTPUT: 16


print("= "*15)
import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def is_adult(years):
        return years > 18

person = Person('Mary', 21)
print(Person.is_adult(8))    # False
print(Person.is_adult(28))   # True


print("* "*15)
"""
@CLASSMETHOD

класметод приймає першим параметром клас - cls. 
При викликові метода від екземпляра класу, у параметр прилетить назва класу нашого екземпляра
exmpl1.class_hello()   # class_hello <class '__main__.Exmpl'>
Пайтон сам визначить, що класом нашого екземпляра exmpl1 є клас Exmpl і передасть назву класу у параметр cls нашого класметоду

Щоб визначити, який є клас у екземпляра класу, потрібно до екземпляра застосувати магічний метод __class__: 
print(exmpl1.__class__)
# <class '__main__.Exmpl'>

Класметоди потрібні, коли ми хочемо робити якусь обробку НЕ над екземплярами класу, а над цілим класом.
"""

class Exmpl:

    @classmethod
    def class_hello(cls):
        print(f'class_hello {cls}')

exmpl1 = Exmpl()
Exmpl.class_hello()   # class_hello <class '__main__.Exmpl'>
exmpl1.class_hello()   # class_hello <class '__main__.Exmpl'>
print(exmpl1.__class__)   # <class '__main__.Exmpl'>  --->  класом екземпляра exmpl1 є клас Exmpl


print("- "*15)
class MyClass:
    Total_objects = 0

    def __init__(self):
        MyClass.Total_objects += 1

    @classmethod
    def total_objects(cls):
        print("Total objects: ", cls.Total_objects)


my_obj1 = MyClass()
my_obj2 = MyClass()
my_obj3 = MyClass()
MyClass.total_objects()


print('\n########## 4* ##########')
# class Pasta:
#     """
#     Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
#     It should have 2 methods:
#     carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
#     which should create Pasta instances with predefined list of ingredients.
#
#     Example:
#         pasta_1 = Pasta(["tomato", "cucumber"])
#         pasta_1.ingredients will equal to ["tomato", "cucumber"]
#         pasta_2 = Pasta.bolognaise()
#         pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
#     """

class Pizza:
    def __init__(self, ingredients=[]):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pizza(['forcemeat', 'tomatoes'])   # Pizza() - створення об"єкту класу Pizza

    @classmethod
    def bolognaise(cls):
        return Pizza(['bacon', 'parmesan', 'eggs'])

pizza_carbonara = Pizza.carbonara()
print('pizza_carbonara:', pizza_carbonara.ingredients)
print(pizza_carbonara)   # <__main__.Pizza object at 0x7f9d69804f70>

pizza_bolognaise = Pizza.bolognaise()
print('pizza_bolognaise:', pizza_bolognaise.ingredients)
print(pizza_bolognaise)
# <__main__.Pizza object at 0x7f73e7334ca0>

pasta_1 = Pizza(["tomato", "cucumber"])
print(pasta_1.ingredients)
