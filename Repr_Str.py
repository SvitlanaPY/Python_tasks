print('hello world')   # hello world



# repr - для серіалізації та відладки, є виводом, який є читабельним для інтерпретатора Python,
# __repr__ дає строку, оціночне строкове представлення обієкта
# >>> x = 'foo'
# >>> x.__repr__()
# "'foo'"
# >>> repr(x)
# "'foo'"

# str - використовується для створення виводу, який має бути читабельним для кінцевого користувача


# >>> str('hello world')
# 'hello world'
# >>> repr('hello world')
# "'hello world'"

# eval(repr('hello world'))
# 'hello world'
# eval(str('hello world'))
# SyntaxError: unexpected EOF while parsing


import datetime
today = datetime.datetime.now()
print(str(today))    # 2021-08-30 18:49:00.352057
print(repr(today))   # datetime.datetime(2021, 8, 30, 18, 49, 0, 352057) - официальное представление обєкта дати

