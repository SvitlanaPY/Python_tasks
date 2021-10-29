"""
Exceptions/виключення - повідомлення про помилку, воно містить:
номер рядка, в якому виникла виключення,
тоді сам код, який став причиної виключення,
і тип виключення з текстом.
Тобто кожна помилка/виключення має свій тип.

Виключення виникає в момент виконання.
Весь код до місця виникнення помилки виконається, а все що після помилки - вже не виконається.
Але ми можемо обробляти виключення таким чином, що навіть після їх виникнення код буде виконуватись до кінця.

Виключення в Пайтони бувають:
1. при виконанні - тобто вони виявляються в момент виконання програми.
2. до виконання програми (виключення компіляції) - програма навіть не запуститься (IndentationError)
3. логічні помилки/помилки в логіці програми - програма видає невірну відповідь, але запускається і відпрацьовує.

Як обробляти виключення:
try:
    int('hello')
except ValueError:
    print("помилка перетворення")

Всі типи виключень є класами, які перебувають у строгій ієрархії!!!
В основі усіх класів знаходиться BaseException(базове виключення), від нього наслідуються всі виключення:
Exception, SystemExit, GeneratorExit, KeyboardInterrupt
Системні виключення (їх краще не обробляти): SystemExit, GeneratorExit, KeyboardInterrupt
Всі решта - звичайні виключення.
Exception - є виключенням, від якого наслідуються всі основні виключення, з якими ми зустрічаємось в програмуванні.
Щоб відловити виключення певного типу, то можна звертатись не конкретно до цього типу виключення, а до його батьківського типу.
Наприклад, щоб відловити IndexError ми можемо звертатись до LookupError(батьківський клас для IndexError)
"""
t = IndexError()
print(isinstance(t, IndexError))   # True - means that "t" is object of class IndexError
print(isinstance(t, LookupError))  # True - means that "t" is object of class LookupError
print(isinstance(t, TypeError))  # False - means that "t" is NOT an object of class TypeError
print(isinstance(t, Exception))   # True - means that "t" is object of base class Exception

# print('Hello1')
# print('Hello2')
# print('Hello3')
# try:
#     {}[5]
# except LookupError:   # LookupError is parent class of KeyError and that's why we can catch KeyError
#     print('KeyError exception occured')
# print('Hello4')
# print('Hello5')


"""
Ми самі теж можемо викликати виключення - за допомогою ключового слова raise
"""
# print('Hello1')
# print('Hello2')
# raise ValueError('Incorrect meaning')   # ValueError: Incorrect meaning
# print('Hello3')
# print('Hello4')
#

try:
    a = int(input(ford))
except:   # if no type of exception mentioned then all types are taken into account
    raise ValueError("ПЕРЕДАВАЙТЕ ЧИСЛО...")   # raise ValueError("ПЕРЕДАВАЙТЕ ЧИСЛО...")   ValueError: ПЕРЕДАВАЙТЕ ЧИСЛО...
