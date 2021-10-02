import pprint

class Car:
    model = "Jeep"
    engine = 2.6
    color = "black"

    def drive():
        print("Let's go!!!")

print(Car.drive)
# <function Car.drive at 0x7f3b750d54c0>
print(getattr(Car, "drive"))
# <function Car.drive at 0x7f3b750d54c0>

# ВИКЛИК ФУНКЦІЇ ЯК АТРИБУТУ КЛАСУ:
print(Car.drive())
# Let's go!!!
# None
print(getattr(Car, "drive")())
# Let's go!!!
# None

c = Car()
print(c.drive)
# <bound method Car.drive of <__main__.Car object at 0x7fe42f49e190>>
print(Car.drive)
# <function Car.drive at 0x7f3b750d54c0>

# для екземпляру класу (def drive()) - це метод, а для класу (def drive()) - це функція!!!
# при спробі викликати ф-ію через екземпляр класу - отримаємо TypeError
# print(c.drive())   # TypeError: drive() takes 0 positional arguments but 1 was given

"""
При створенні функції як атрибуту класу, ми зможе викликати функцію від класу, 
але не зможемо викликати ф-ію від екземпляру класу
"""