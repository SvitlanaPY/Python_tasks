"""
Приватні private змінні в Пайтоні прийнято позначати двома нижніми підкресленнями
"""

class BankAccount3:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)


account3 = BankAccount3('Sam', 300000, 777777777)
account3.print_private_data()   # доступ до атрибутів через метод класу,
# але доступ ззовні класу(outdoor access) НЕ можливий -  буде AttributeError
"""
outdoor access, тобто доступ до приватних атрибутів ззовні класу НЕможливий:
"""
# print(account3.__name)      # AttributeError
# print(account3.__balance)   # AttributeError
# print(account3.__passport)  # AttributeError

"""
але ми можемо звертатись до приватних атрибутів всередині класу, тобто через метод 
(прийшовши у банк, зробивши запит в банкові і сам банк роздруковує нам ці дані)
цей метод називається - ІНКАПСУЛЯЦІЯ (приховування обробки захищених атрибутів)
ENCAPSULATION/ ІНКАПСУЛЯЦІЯ - підхід/механізм/принцип, що полягає у обмеженні прямого доступу до даних (полів, проперті, методів, атрибутів...) 
тобто, користувачеві дається метод по користуванню з приватними даними і 
через цей метод користувач може отримати певний доступ до захищених атрибутів, 
а який саме доступ вирішують самі програмісти, але напряму звернутись до захищених атрибутів користувач НЕ може
тим самим ці дані інкапсулюємо/скриваєму у наш метод/в інтерфейс
"""

account3.print_private_data()    # 'Sam 300000 777777777

"""
Захищеними можуть бути не лише атрибути, але і методи
Методи теж можуть починатись із двох нижніх підкреслень.,  і доступ до цього методу є лише всередині класу.
"""
# access to private data through public method:
class BankAccount4:

    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def print_public_data(self):
        self.__print_private_data()

    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)

account4 = BankAccount4('КАТЯ', 400000, 888888888)
# account4.__print_private_data()
# AttributeError: 'BankAccount' object has no attribute '__print_private_data'

"""
ДОСТУП ДО ПРИВАТНОГО МЕТОДУ ЧЕРЕЗ public method - викликаємо метод public, а всередині нього викликається private метод.
"""
account4.print_public_data()   # access to private data through public method
# КАТЯ 400000 888888888

"""
До захищених атрибутів і методів можна доступись, але не напряму.
Глянемо, які ж атрибути є у нашого об"єкту account4:
print(dir(account4)) - всі вони починаються з нижнього підкреслення, тоді іде клас, а тоді сама назва захищеного атрибуту:
['_BankAccount4__balance', '_BankAccount4__name', '_BankAccount4__passport', '_BankAccount4__print_private_data', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'print_public_data']
Отже, ми можемо отримати доступ до нашого приватного методу, якщо викликати наш метод таким чином:
account4._BankAccount__print_private_data()
і таким же способом можемо отримати доступ і до наших захищених атрибутів, написавши:
account4._BankAccount__name
account4._BankAccount__balance
account4._BankAccount__passport
"""
print(dir(account4))    # щоб подивитись, які атрибути є у нашого об"єкту account4
# ['_BankAccount4__balance', '_BankAccount4__name', '_BankAccount4__passport', '_BankAccount4__print_private_data', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'print_public_data']
account4._BankAccount4__print_private_data()
# КАТЯ 400000 888888888
print(account4._BankAccount4__name)
# КАТЯ
print(account4._BankAccount4__balance)
# 400000
print(account4._BankAccount4__passport)
# 888888888
