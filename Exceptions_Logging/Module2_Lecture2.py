"""
Виключення в Пайтоні діляться на два типи:
1. Синтаксичні помилки - коли ми в коді допустили синтаксичну помилку і інтерпретатор не може розібрати код
Помилки до виконання самого коду, програма навіть НЕ запускається.
2. Помилки в процесі виконання програми (ри виконанні коду).
Кожна помилка в Пайтоні є об"єктом і має три обов"язкові речі:
1. Тип
2. Додаткове повідомлення, яке несе додаткову інформацію про те, що пішло не так
3. Стан стеку викликів на той момент, коли в нас відбулась помилка.
"""
# EXCEPTIONS - code is executed partly (untill error happens)
print("This line is executed")

class EventLengthMixin:
    def even_length(self):
        return len(self) % 2 == 0

class MyList(list, EventLengthMixin):
    pass


ml = MyList([1, "aaa", 3, 4])
ml.sort()
print(ml)

#OUTPUT:
# This line is executed
# ml.sort()
# TypeError: '<' not supported between instances of 'str' and 'int'