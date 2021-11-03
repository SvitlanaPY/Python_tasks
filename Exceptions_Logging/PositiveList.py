"""
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом,
чтобы при попытке добавить неположительное целое число бросалось исключение NonPositiveError и число не добавлялось,
а при попытке добавить положительное целое число, число добавлялось бы как в стандартный list.
В данной задаче гарантируется, что в качестве аргумента x метода append всегда будет передаваться целое число.

Примечание:
Положительными считаются числа, строго большие нуля.
"""
print("1. ")
# class NonePositiveError(Exception):
#     pass
#
# class PositiveList(list):
#     def append(self, x):
#         while True:
#             x = int(input(f"Enter number: "))
#             if x > 0:
#                 super().append(x)
#                 print(self)
#             else:
#                 raise NonePositiveError("Negative Value entered!")
#
#
# obj = PositiveList()
# obj.append(5)


print("\n2. ")
class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super().append(x)
        else:
            print(self)
            raise NonPositiveError("Negative value entered!")

obj = PositiveList()
obj.append(5)
obj.append(8)
obj.append(6)
obj.append(10)
obj.append(0)


print("\n3. ")
# class NonPositiveError(Exception):
#     pass
#
# class PositiveList(list):
#     def append(self, x):
#         if x <= 0:
#             raise NonPositiveError
#         super().append(x)
