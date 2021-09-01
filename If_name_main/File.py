import Module_

print("File")
print("Call outside the module. Sum=", Module_.sum(4, 6))
print(__name__)


# or
# from Module_ import sum
# print("File")
# print("Call outside the module. Sum=", sum(4, 6))
# print(__name__)
