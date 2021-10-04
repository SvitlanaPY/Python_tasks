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