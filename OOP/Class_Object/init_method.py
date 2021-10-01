class Cat:
    breed = 'pers'

    def show_name(self):
        print(f'My surname is {self.name}')

    def set_value(self, value, age=0):
        self.name = value
        self.age = age

bob = Cat()
# щоб створити атрибути name та age, нам потрібно викликати метод set_value()
bob.set_value('Bob')


"""
Магічний метод - це метод, назва якого поч-ся і закінчується з __ 
кожен магічний метод спрацьовує у певний момент
магічний метод __init__ спрацьовує одразу після створення екземпляра класу
цей метод приймає параметром сам екземпляр класу, який створюєтсья в процесі виклику нашого класу всередину цього методу
__init__ приймає на вхід наш об"єкт, який ми створюємо, викликаючи клас
спершу пайтон створить об"єкт, це робить ін магічний метод - __new__
а потім пайтон буде створювати простір імен всередині цього екземплара і викликати метод __init__
цей метод потрібен для ініціалізації, тобто заповнення нашого обєкта якимось значеннями
"""

class Person:
    def __init__(self):
        print("Hello from __init__", self)

p = Person()   # <__main__.Person object at 0x7f920ea4fe50>
# одразу після створення екземпляру класу р ми одразу побачили Hello from __init__
# Hello from __init__
print(p)   # <__main__.Person object at 0x7f920ea4fe50>


class Cat:
    def __init__(self, name, b='pers', age=1, color='white'):
        print("Hello from kitty: ", self, name, breed, age, color)
        self.name = name
        self.age = age
        self.breed = b
        self.color = color

Cat("Tom", "siam", 5, "black")
# Hello from kitty:  <__main__.Cat object at 0x7fad5dfdcb20> Tom siam 5 black

walt = Cat("Walt")
# Hello from kitty:  <__main__.Cat object at 0x7f19b591caf0> Walt pers 1 white

kelly = Cat('Kelly', age=40)
# Hello from kitty:  <__main__.Cat object at 0x7f2bb8b04b80> Kelly pers 40 white

"""
як правило імена аргументів функції(приймаються функціями/методами) співпадають з іменами атрибутів (містять self) 
"""
