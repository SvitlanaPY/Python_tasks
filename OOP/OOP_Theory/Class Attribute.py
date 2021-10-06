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
Доступитись до атрибутів класу:
<назва класу>/ <назва екземпляра класу>.<назва атрибуту>:
CarNew.model 
с.model 

До атрибутів класу можна звертатись також через ф-ію getattr():
getattr(<об"єкт, до атрибуту якого ми звертаємось>, <"сам атрибут">),
де об"єкт - це клас чи екземпляр класу
<сам атрибут> має бути в лапках!!!
getattr(CarNew, "model")  -- через клас
getattr(c, "model")  -- через екземпляр класу

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
CarNew.model = 'Opel'

або використовуючи функцію setattr():
setattr(CarNew, "model", "Audio") 
"""
CarNew.model = 'Opel'
pprint.pprint(CarNew.model)
# 'Opel'
setattr(CarNew, "model", "Audio")
pprint.pprint(CarNew.color)
# 'Audio'


"""
СТВОРИТИ атрибут класу:
setattr(Person, "height", 180) 
або
Person.weight = 60 
"""
Person.weight = 60
pprint.pprint(Person.weight)
# 60

setattr(Person, "height", 180)
pprint.pprint(Person.height)
# 180

"""
Всі атрибути, які створені в класі, НЕ знаходяться в просторі імен екземпляра класу, но ми можемо до них звертатись!

Створюючи атрибут через виклик екземпляру класу, ми створимо атрибут у області видимості лише екземпляру класу, 
а не в класі і цей атрибут НЕ буде доступний через виклик класу - отримаємо AttributeError
a.surname = 'Ivanov'  (де а - є екземпляром класу Person)
pprint.pprint(Person.surname)   # AttributeError: type object 'Person' has no attribute 'surname'
"""


"""
Щоб вибалити атрибут класу: 
del Person.age 
delattr(Person, "age")
"""
del Person.age
# pprint.pprint(Person.age)   # AttributeError, бо атрибут age вже видалиено
pprint.pprint(Person.__dict__)
delattr(Person, "name")
pprint.pprint(Person.__dict__)

"""
всі атрибути, які створені в класі, НЕ знаходяться в просторі імен екземпляра класу, но ми можемо до них звертатись
"""


# class Student:
#     """
#     Add an 'email' attribute of the object student and set its value
#     Assign the new attribute to 'student_email' variable and print it by using getattr
#     """
#     id = 0
#     name = ""
#
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(101, 'Jim')
setattr(student, 'email', 'email_1@gmail.com')
student_email = 'email_2@gmail.com'        # create 'student_email' variable
setattr(student, 'email', student_email)
print('student.email=', getattr(student, "email"))
# OUTPUT: student.email= email2@gmail.com
