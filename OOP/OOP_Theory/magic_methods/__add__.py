"""
об"єкти/екземпляри класу НЕ підтримують математичних бінарних операцій (+, *, /, -) !
When we add two objects with binary ‘+’ operator - it throws an error,
because compiler don’t know how to add two objects.

The same error happens when we add other types with our class object.

У всіх бінарних операціях з об"єктами - у першого об"єкту (лівого) викликається відповідний магічний метод,
і в цей мегічний метод у якості параметру підставляється інший об"єкт:

a1 + a2 = a1.__add__(a2)
a1 = Dodavannya(11)
a2 = Dodavannya(22)

"""

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


b = BankAccount('Ivan', 900)
print("balance: ", b.balance)   # balance:  900
print(b.balance + 400)   # 1300
# print(b + 700)   # TypeError: unsupported operand type(s) for +: 'BankAccount' and 'int'
"""
print(b + 700)   # TypeError: unsupported operand type(s) for +: 'BankAccount' and 'int' --- 
отже, клас, який ми створюємо, НЕ може додаватись з будь-якими іншими типами
ми не можемо додавати два об"єкти.
"""
# c = BankAccount('Jep', 100)
# print("b + c = ", b+c)


print('='*15)
"""
Перевизначимо метод __add__, щоб можна було додавати  об"єкт + інт/float
а також  об"єкт + об"єкт
"""
class BankAccount1:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print('__add__ called')

        # щоб можна було додавати об"єкт + об"єкт
        if isinstance(other, BankAccount1):
            return self.balance + other.balance
        # щоб можна було додавати об"єкт + інт/float
        if isinstance(other, (int, float)):
            return self.balance + other

        raise NotImplemented


bb = BankAccount1('Mike', 78)
print("balance: ", bb + 12)     # 78 + 12
# __add__ called
# balance:  90
"""
bb + 12 працює наступним чином: 
до об"єкту bb викликався метод __add__ і переметром йому передавався other, який =12
"""
tt = BankAccount1('Tanya', 900)
print("додаємо ДВА ОБЄКТИ: ", bb + tt)


print('# '*10)
class BankAcc:
    def __init__(self, name, balance):
        print("new_obj init")
        self.name = name
        self.balance = balance

    def __repr__(self):
        return f"Client {self.name} with balance {self.balance}"

    def __add__(self, other):
        print('__add__ called')

        if isinstance(other, BankAccount1):
            return self.balance + other.balance
        if isinstance(other, (int, float)):
            return BankAcc(self.name, self.balance + other)
        raise NotImplemented


ba = BankAcc('IVAN', 200)    # new_obj init
print(ba + 30)
# __add__ called
# new_obj init
# Client IVAN with balanbe 230


print("& "*10)
""" 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value
which is greater than 10. And perform this add (+) of two instances.
"""

class Dodavannya:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):      # self = a1, other = a2
        if self.value > 10 or other.value > 10:    # other.value = a2.value (attribute of the second object a2); self.value = a1.value
            return self.value * other.value
        return self.value + other.value


a1 = Dodavannya(11)
a2 = Dodavannya(7)
print(a1 + a2)
# OUTPUT: 77
b1 = Dodavannya(5)
b2 = Dodavannya(3)
print(b1 + b2)
# OUTPUT: 8

# c1 = Dodavannya(100)
# print(c1 + 222)


"""
How to overload the operators in Python? 
Consider that we have two objects which are a physical representation of a class (user-defined data type) 
and we have to add two objects with binary ‘+’ operator it throws an error, 
because compiler don’t know how to add two objects. 

So we define a method for an operator and that process is called operator overloading. 
We can overload all existing operators but we can’t create a new operator. 
To perform operator overloading, Python provides some special function or magic function 
that is automatically invoked when it is associated with that particular operator. 
For example, when we use + operator, the magic method __add__ is automatically invoked 
in which the operation for + operator is defined.
"""
print('+ '*10)
# Python Program illustrate how to overload an binary '+' operator
class A:
    def __init__(self, a):
        self.a = a

    # adding two objects
    def __add__(self, other):
        return self.a + other.a


obj1 = A(1)
obj2 = A(2)
obj3 = A("Geeks")
obj4 = A("For")

print(obj1 + obj2)
print(obj3 + obj4)


print('- '*10)
# Python Program to perform addition of two complex numbers using binary '+' operator overloading.
class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # adding two objects
    def __add__(self, other):
        return self.a + other.a, self.b + other.b

Ob1 = Complex(1, 2)
Ob2 = Complex(2, 3)
Ob3 = Ob1 + Ob2
print(Ob3)


print('* '*10)
# declare our own string class
class String:

    # magic method to initiate object
    def __init__(self, string):
        self.string = string

    def __add__(self, other):
        return self.string + other
        # if isinstance(other, str):
        #     return self.balance + other


string1 = String('Hello')
print(string1 + ' Geeks')
# print(string1 + 10)    # TypeError: can only concatenate str (not "int") to str
