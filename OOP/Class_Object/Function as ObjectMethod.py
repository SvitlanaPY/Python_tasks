
class Cat:
    def hello():
        print("Hello world from kitty")

bob = Cat()
print(Cat.hello())
# Hello world from kitty
# None

# print(bob.hello())
# TypeError: hello() takes 0 positional arguments but 1 was given

# FUNCTION:
print(Cat.hello)   # <function Cat.hello at 0x7f5b68fe50d0>
# METHOD:
print(bob.hello)   # <bound method Cat.hello of <__main__.Cat object at 0x7f5b69075970>>

"""
METHOD - це та ж функція, але оголошена всередині якогоськласу, і метод прив"язаний до певного екземпляру класу, 
а функція ні з ким не пов"язана і її можна окремо викликати.
При виклику метода, той об"єкт/екземпляр класу, з яким він пов"язаний, буде автоматично проставлятись в аргумент функції, 
тобто передаватись у функцію/метод як її параметр
bob.hello
"""

class Cat:
    def hello(*args):
        print("Hello world from kitty!!!")
        print(args)

jim = Cat()
print(jim.hello())
# Hello world from kitty!!!
# (<__main__.Cat object at 0x7f48603f32e0>,)
print(jim)   # <__main__.Cat object at 0x7f48603f32e0>

"""
Через екземпляр класу, який попадає нам першим аргументом всередину нашого методу, 
ми можемо отримувати доступ до атрибутів класу: self.breed
class Cat:
    breed = 'pers'
    def show_breed(self):
        print(f'My breed is {self.breed}')
"""

class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty!!!")
        print(args)
    def show_breed(instance):
        print(f'My breed is {instance.breed}')

walt = Cat()
print(walt.show_breed())
# My breed is pers
walt.breed = "siam"
print(walt.show_breed())
# My breed is siam

bob = Cat()
print(bob.show_breed())
# My breed is pers

class Cat:
    breed = 'pers'
    def hello(*args):
        print("Hello world from kitty!!!")
        print(args)
    def show_breed(instance):
        print(f'My breed is {instance.breed}')

    def show_surname(instance):
        print(f'My surname is {instance.surname}')

    def show_name(instance):
        if hasattr(instance, "name"):
            print(f'My name is {instance.name}')
        else:
            print("NOTHING")

    def set_value(kitty, value, age=0):
        kitty.name = value
        kitty.age = age



mary = Cat()
mary.surname = "MARY"
print(mary.show_surname())
# My surname is MARY

murka = Cat()
print(murka.show_name())
# NOTHING

murka.name = "MURKA"
print(murka.show_name())
# My name is MURKA


# метод set_value НЕ зможемо викликати БЕЗ параметра, бо він приймає один аргумент
tom = Cat()
print(tom.show_name())
# NOTHING
tom.set_value("TOM")
print(tom.name)
# TOM
print(tom.show_name())
# My name is TOM

jerry = Cat()
print(jerry.show_name())
# NOTHING
jerry.set_value("Jerry")
print(jerry.name)
# Jerry
jerry.set_value("Jerry", age=5)
print(jerry.age)
# 5

"""
self - це загальноприйняте назва об"єкту, у якого був викликаний метод

"""
