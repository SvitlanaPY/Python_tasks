"""
Агрегація - тип композиції, не передбачає права власності на об"єкт.
Об"єкт класу створюємо за межами класу і передаємо його як атрибут в інший клас:
engine1 = Engine()
car1 = Car(engine1)
Клас Car, який буде приймати об"єкт іншого (Engine) класу, повинен мати атрибут(self.engine),
щоб прийняти той об"єкт від іншого (Engine) класу.
"""
class Car:
    def __init__(self, engine_):
        self.engine = engine_
# У engine_ - об"єкт класу Engine: <__main__.Engine object at 0x7f785455f460>
# self.engine - атрибут об"єкту car1 класу Car
#  Клас, у

class Engine:
    def __init__(self):
        pass

engine1 = Engine()
car1 = Car(engine1)   # car1 = Car(Engine())
# Якщо ми видалимо об"єкт car1, то об"єкт engine1 все ще існуватиме


print("* "*15)
# class Guitar:
#     """
#     Make the class with aggregation
#     """
# class GuitarString:
#     """
#     Make the class with aggregation
#     """

class Guitar:
    def __init__(self, string):
        self.string = string
        print('Hi')
# У self.string буде летіти об"єкт gs класу GuitarString

class GuitarString:
    def __init__(self):
        pass

gs = GuitarString()
guitar = Guitar(gs)
print(guitar.string)
# OUTPUT: <__main__.GuitarString object at 0x7f398ed32070>

