import pprint
class Person:
    age = 33
    name = "Ivan"

p = Person()


class Car:
    model = "BMW"
    engine = 1.6
    color = "blue"

    def func(self):
        print("Hello")

a1 = Car()
a2 = Car()
pprint.pprint(Car.__dict__)

"""
Звертатись до атрибутів екземплярів класу:
a1.engine
"""
pprint.pprint(a1.engine)
# 1.6  - доступ до атрибуту engine з простору імен класу, в просторі імен екземпляру класу а1 цього атрибуту немає
pprint.pprint(a1.__dict__)   # {}
print("CAR: ", Car.__dict__)
# створюємо атрибути екземпляру класу
a1.model = "Lada"
a1.seat = 4
pprint.pprint(a1.__dict__)
# {'model': 'Lada', 'seat': 4}
pprint.pprint(a2.__dict__)
# {}
pprint.pprint(Car.__dict__)

"""
При створенні класу і атрибутів класу, всі атрибути класу стають доступними для всіх екземплярів цього класу
але створювати чи змінювати атрибути класу через виклик екземплярів класу ми не можемо, 
при цьому ми створимо чи змінимо атрибути даного екземпляра класу, а не атрибути самого класу.

Створити/змінити атрибути екземплярів класу можна лише через звернення до екземплярів класу, 
при цьому створений атрибут буде в області видимості лише даного екземпляру, але не самого класу, чи іншого екземпляра класу
і доступ до створеного атрибуту обєкту через клас буде викликати AttributeError
"""

