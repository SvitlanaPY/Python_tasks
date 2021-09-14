import pprint
# ф-ія import додає в простір імен назву модуля, який ми імпортуємо
# 'pprint': <module 'pprint' from '/usr/lib/python3.8/pprint.py'>,
import calendar
# 'calendar': <module 'calendar' from '/usr/lib/python3.8/calendar.py'>,

import math
#  'math': <module 'math' (built-in)>,



def say_hello(name):
    print(f"Hello, {name}")

def summa(*args):
    return sum(args)

def factorial(n):
    pr = 1
    for i in range(1, n + 1):
        pr *= i
    return pr


my_str = "YOU'RE BREATHTAKING"
my_num1 = 2
my_num2 = 3


# print(locals())
pprint.pprint(locals())

c = calendar.TextCalendar()
print(c.formatyear(2021))
# formatyear(theyear, w=2, l=1, c=6, m=3)
# Return a m-column calendar for an entire year as a multi-line string.
# Optional parameters w, l, and c are for date column width,
# lines per week, and number of spaces between month columns, respectively.



pprint.pprint(dir(math))   # виводимо простір імен модуля math
pprint.pprint(math.e)      # звертаємось до змінної е в модулі math
# 2.718281828459045
pprint.pprint(math.pi)     # звертаємось до змінної рі в модулі math
# 3.141592653589793
pprint.pprint(math.factorial(10))    # звертаємось до ф-ії factorial модуля math і передаємо їй число 10:
# 'factorial': <function factorial at 0x7f775e184d30>,
# 3628800


# імпортуємо модуль, задаючи йому псевдонім;
# import math as m
#  'm': <module 'math' (built-in)>,
# при такому імпорті звернення до ф-ій/змінних модуля відбуватиметься вже через цей псевдонім
# pprint.pprint(m.sqrt(81))



# Якщо НЕ потрібно імпортувати ВЕСЬ функціонал модуля, а лише його певні ф-ії/змінні, то
# використовується інструкція: from <module name> import <list of functions/variables>
# і при такому імпорті ці імена модуля будуть підключатись в наш простір імен НАПРЯМУ

from string import ascii_uppercase, ascii_lowercase
pprint.pprint(locals())
# 'ascii_uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
#  'ascii_lowercase': 'abcdefghijklmnopqrstuvwxyz',

