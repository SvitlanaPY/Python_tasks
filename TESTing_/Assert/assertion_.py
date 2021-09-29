# Інструкція assert призначена для порівняння значень.
# Працює вона по принципу if, але якщо умова НЕ виконується, то кидається ексепшин.
# assert працює як логічний вираз, перевіряючи, чи задана умова є вірна чи хибна, тому у assert має бути булева умова.
# Якщо умова True, то нічого не відбувається і виконується наступна стрічка коду.
# Якщо ж умова False, то оператор assert зупиняє виконання програми і видає AssertionError.
# У цьому випадку assert працює як raise, і виводить ексепшин, який називається AssertionError.

# СИНТАКСИС ОПЕРАТОРА assert:
# assert <condition>, <message>
# <message> - є НЕобов"язковим, це опційне повідомлення, яке буде виводитись при помилці.
# num1 = 10
# num2 = 0
# assert num2 != 0, "The divisor is zero!!!"
# AssertionError: The divisor is zero!!!

assert sum([1, 2, 3]) == 6, "test error"
# test is passed, nothing happened

print()
# assert sum([1, 2, 3]) == 7, "test error"
# AssertionError: test error

print()
# num1 = 10
# num2 = 0
# assert num2 != 0, "The divisor is zero!!!"
# AssertionError: The divisor is zero!!!

print()
def func(a):
    if a is True:
        return "HELLO"
    else:
        return "BYE"

assert func(True) == "HELLO"
assert func(False) == "BYE"
# test are passed, nothing happened
# assert func(False) == "HELLO"
# # AssertionError


print()
def hyp(a, b):
    hyp = (a ** 2 + b ** 2) ** 0.5
    return hyp

assert hyp(3, 4) == 5
# тест не впав, отже функція hyp() реалізована вірно


print()
def hyp_wrong(a, b):
    hyp = (a ** 2 + b ** 2)
    return hyp

# assert hyp_wrong(3, 4) == 5
# # тест впав з AssertionError, отже функція hyp_wrong() реалізована НЕвірно


import logging

def hyp(a, b):
    hyp = (a ** 2 + b ** 2)
    return hyp

try:
    assert hyp(3, 4) == 5
except AssertionError:
    logging.warning("Test FAILED !!!")
# WARNING:root:Test FAILED !!!

