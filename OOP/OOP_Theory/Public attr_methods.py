class BankAccount1:
    def __init__(self, name, balance, passport):
        self.name = name
        self.balance = balance
        self.passport = passport
    def print_public_data(self):
        print(self.name, self.balance, self.passport)
account1 = BankAccount1('Bob', 100000, 4567896541)
account1.print_public_data()   # 'Bob' 100000 4567896541
# outdoor access:
print(account1.name)      # 'Bob'
print(account1.balance)   # 100000
print(account1.passport)  # 4567896541

class BankAccount2:
    def __init__(self, name, balance, passport):
        self._name = name
        self._balance = balance
        self._passport = passport
    def print_protected_data(self):
        print(self._name, self._balance, self._passport)
account2 = BankAccount2('Ted', 200000, 5555555555)
account2.print_protected_data()  # 'Ted' 200000 5555555555
# outdoor access:
print(account2._name)       # 'Ted'
print(account2._balance)    # 200000
print(account2._passport)   # 555555555

class BankAccount3:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    def print_private_data(self):
        print(self.__name, self.__balance, self.__passport)
account3= BankAccount3('Sam', 300000, 777777777)
account3.print_private_data()   # account3.print_private_data()   # 'Sam 300000 777777777
# outdoor access:
# print(account3.__name)      # AttributeError
# print(account3.__balance)   # AttributeError
# print(account3.__passport)  # AttributeError


#access to private data through public method:
class BankAccount:
    def __init__(self, name, balance, passport):
        self.__name = name
        self.__balance = balance
        self.__passport = passport
    def print_public_data(self):
        self.__print_private_data()
    def __print_private_data(self):
        print(self.__name, self.__balance, self.__passport)
account4 = BankAccount('Kate', 400000, 888888888)
account4.print_public_data()   # access to private data through public method
print(dir(account4))   # ['_BankAccount__balance', '_BankAccount__name', '_BankAccount__passport', '_BankAccount__print_private_data', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'print_public_data']
account4._BankAccount__print_private_data()   # Kate 400000 888888888
print(account4._BankAccount__balance)   # 400000


# print(SchoolBus.__mro__)
# print(SchoolBus.mro())
# SchoolBus is child class

print(dir(object))



class Human:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return f"Person has name {self.name}"
    def info(self):
        print(self)

hum = Human('Sveta')
hum.info()


class BankAcc:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should be numeric')
        self.__balance = value
    def delete_balance(self):
        del self.__balance
    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

a = BankAcc('Ivan', 100)
b = BankAcc('Vasya', 100)
print(b.get_balance())
b.set_balance(400)
print(b.get_balance())
c = BankAcc('Tanya', 200)
#c.set_balance('hello')
print(c.get_balance())

# balance = property(fget=get_balance(), fset=set_balance())
d = BankAcc('Misha', 400)
print(d.balance)   # not attribute, but property
d.balance = 700
print(d.balance)    # 777
# add delete function/method
w = BankAcc('Misha', 400)
print(w.balance)
# del w.balance
# print(w.balance)
# w.balance = 999
# print(w.balance)
x = property()
print(x)  # <property object at 0x7fb0e9794770>


class BankAcc2:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def set_balance(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('Balance should be numeric')
        self.__balance = value
    def delete_balance(self):
        del self.__balance
    my_balance = property()
    my_balance = my_balance.getter(get_balance)
    my_balance = my_balance.setter(set_balance)
    my_balance = my_balance.deleter(delete_balance)
#    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)

a = BankAcc2('Olga', 100)
print(a.my_balance)
a.my_balance = 111
print(a.my_balance)

