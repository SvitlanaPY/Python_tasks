import pprint
class Person:
    age = 33
    name = "Ivan"

a = Person()


class CarNew:
    model = "BMW"
    engine = 1.6
    color = "blue"

    def func(self):
        print("Hello")

c = CarNew()
# <__main__.CarNew object at 0x7f548e016c40>

print("Attribute model in CarNew: ", CarNew.model)
print(isinstance(a, CarNew))
# False  - бо змінна 'а' належить класу Person, но не класу CarNew,

print(CarNew.func)    # <function CarNew.func at 0x7fe61250b8b0>

"""
Щоб побачити всі атрибути, які є в класі використовується магічна змінна __dict__
"""
pprint.pprint(CarNew.__dict__)

"""
До атрибутів класу звертатись через <назву класу/екземпляра класу>.<назва атрибуту>:
CarNew.model / с.model 

До атрибутів класу можна звертатись через ф-ію getattr(<об"єкт, до атрибуту якого ми звертаємось>, <"сам атрибут">)
<сам атрибут> має бути в лапках
getattr(CarNew, "model")  -- через клас
getattr(c, "model")  -- через об"єкт класу

У функції getattr може бути третій параметр, який повернеться нам, якщо не існує атрибута, до якого ми звертаємось:
getattr(CarNew, "window", "dark") - повернеться dark
CarNew.window = getattr(CarNew, "window", "dark") --- створимо новий атрибут window у класі CarNew
"""
print(getattr(CarNew, "model"))
print(getattr(c, "model"))
print(CarNew.model)   # BMW

CarNew.window = getattr(CarNew, "window", "dark")
print(CarNew.window)
b = CarNew()
pprint.pprint(CarNew.__dict__)
# dark
print(c.window)

"""
ЗМІНИТИ значення атрибуту класу:
c.model = "Opel" / CarNew.model = 'Opel'

або використовуючи функцію setattr():
setattr(CarNew, "model", "Audio") / setattr(c, "model", "Audio") 
"""
c.model = 'Opel'
pprint.pprint(c.model)
# 'Opel'
CarNew.model = 'Audio'
pprint.pprint(CarNew.model)
# 'Audio'
setattr(CarNew, "color", "red")
pprint.pprint(CarNew.color)
# 'red'
setattr(c, "color", "black")
pprint.pprint(c.color)
# 'black'

"""
СТВОРИТИ атрибут класу:
setattr(Person, "height", 180) / setattr(a, "height", 190)
або
Person.weight = 60 / a.weight = 65
"""
Person.weight = 60
pprint.pprint(Person.weight)
# 60
a.weight = 65
pprint.pprint(a.weight)
# 65
setattr(Person, "height", 180)
pprint.pprint(Person.height)
# 180
setattr(a, "height", 190)
pprint.pprint(a.height)
# 190

"""
Щоб вибалити атрибут класу: 
del Person.age / del a.age
delattr(Person, "age") / delattr(a, "age") 
"""
del Person.age
# pprint.pprint(Person.age)   # AttributeError, бо атрибут age вже видалиено
pprint.pprint(Person.__dict__)
delattr(Person, "name")
pprint.pprint(Person.__dict__)
