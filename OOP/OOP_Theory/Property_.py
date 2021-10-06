#
# class BankAcc:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError('Balance should be numeric')
#         self.__balance = value
#     def delete_balance(self):
#         del self.__balance
#     balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
#
# a = BankAcc('Ivan', 100)
# b = BankAcc('Vasya', 100)
# print(b.get_balance())
# b.set_balance(400)
# print(b.get_balance())
# c = BankAcc('Tanya', 200)
# #c.set_balance('hello')
# print(c.get_balance())
#
# # balance = property(fget=get_balance(), fset=set_balance())
# d = BankAcc('Misha', 400)
# print(d.balance)   # not attribute, but property
# d.balance = 700
# print(d.balance)    # 777
# # add delete function/method
# w = BankAcc('Misha', 400)
# print(w.balance)
# # del w.balance
# # print(w.balance)
# # w.balance = 999
# # print(w.balance)
# x = property()
# print(x)  # <property object at 0x7fb0e9794770>
#
#
# class BankAcc2:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
#     def get_balance(self):
#         return self.__balance
#     def set_balance(self, value):
#         if not isinstance(value, (int, float)):
#             raise ValueError('Balance should be numeric')
#         self.__balance = value
#     def delete_balance(self):
#         del self.__balance
#     my_balance = property()
#     my_balance = my_balance.getter(get_balance)
#     my_balance = my_balance.setter(set_balance)
#     my_balance = my_balance.deleter(delete_balance)
# #    balance = property(fget=get_balance, fset=set_balance, fdel=delete_balance)
#
# a = BankAcc2('Olga', 100)
# print(a.my_balance)
# a.my_balance = 111
# print(a.my_balance)


print(dir(object))



print('\n########## 11* ##########')
# class Celsius:
#     """
#     By using @property convert the celsius to fahrenheit
#     Hint: (temperature * 1.8) + 32)
#     """
#     def __init__(self, temperature=0):
#         self._temperature = temperature
#
#
# # create an object
# {obj} = ...
#
# print({obj}.temperature)

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def celsius_to_farenheit(self):
        return (self._temperature * 1.8) + 32

temp = Celsius(35)
print('temp. in fahrenheit:', temp.celsius_to_farenheit)
# OUTPUT: temp. in fahrenheit: 95.0


print('\n########## 9 ##########')
# class Person:
#     """
#     Change the value of the age property of the person object
#     """
#     name = "John"
#     age = 36
#     country = "USA"

class Person:
    def __init__(self, name, country, age = 0):
        self.name = name
        self.country = country
        self.age = age

    @property
    def age(self):
        # print('Get age')
        return self._age

    @age.setter
    def age(self, new_age):
        # print('Set age')
        self._age = new_age

person = Person('John', 'USA', 36)
print(person.age)
# OUTPUT: 36
person.age = 25   # save value in property age (call setter)
print('new age=', person.age)
# OUTPUT: new age= 25


print('\n########## 5* ##########')
# class Concert:
#     """
#     Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
#     In case of setting visitors_count - max_visitors_num should be checked,
#     if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
#     Example:
#         Concert.max_visitor_num = 50
#         concert = Concert()
#         concert.visitors_count = 1000
#         print(concert.visitors_count)  # 50
#     """

class Concert:
    max_visitors_num = 0
    def __init__(self, visitors_count = 0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, count):
        self._visitors_count = count if count <= Concert.max_visitors_num else Concert.max_visitors_num

Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 10
print(concert.visitors_count)
# OUTPUT: 50
Concert.max_visitors_num = 50
concert = Concert()
concert.visitors_count = 10
print(concert.visitors_count)
# OUTPUT: 10
