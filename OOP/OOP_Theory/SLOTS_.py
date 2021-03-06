"""
SLOTS - це обмеження набору атрибутів; дозволяють наперід визначити набір атрибутів, який будуть мати екземпляри класу,
щоб уникнути динамічного створення атрибутів.
За допомогою слотів можемо екземплярам класу задавати/визначати/встановлювати лише певні/визначені атрибути.
Тобто, задати лише імена тих атрибутів, які нам потрібні і
наші екземпляри будуть містити лише ці певні наперід визначені атрибути і ніякі інші не можна буде записати в об"єкти.

У класу, в якого є SLOTS:
1. операції над об"єктами класу будуть виконуватись швидше, а саме:
   - створення об"єкту (p1 = Point(3, 4))
   - зміна атрибутів (p1.x = 100)
   - звернення до цього атрибуту (p1.x)
   - видалення атрибуту (del p1.y)
2. зберігає місце в пам"яті: при використанні __slots__ наші екземпляри займають менше місця в памяті;
до атрибутів доступаємось швидше, бо вони вже зарезервовані в памяті через __slots__
3. обмеження атрибутів

Але при використанні __slots__ ми не будемо мати доступу до магічної змінної __dict__(в якій зберігаються всі атрибути):
p2 = PointSlots(3, 4)
print(p2.__dict__)  --->  AttributeError: 'PointSlots' object has no attribute '__dict__'

Краще НЕ використовувати слоти:
1. при multiple inheritance
2. не працює для таких класів як int, tuple, bytes
3. якщо хочемо робити динамічне присвоєння атрибутів(геттер/сеттер/проперті)

На рівні класу, коли ми пишемо атрибути класу, написати:
__slots__ = ("x", "y"), де строками в колекції перечисляємо, які атрибути будуть використовуватись в класі

In Inheretance:
__slots__ дочірнього класу розширюють __slots__ батьківського класу.
Якщо ми НЕ хочемо додавати нові атрибути в __slots__ в дочірньому класі (не хочемо розширювати список __slots__),
то в дочірньому класі достатньо лише задати порожню колекцію:
__slots__ = tuple()

"""
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(2, 3)
#  можемо звертатись до атрибутів через крапку:
print(p1.x, p1.y)   # 2 3
# ці атрибути зберігаються в магічний змінній __dict__
print(p1.__dict__)   # {'x': 2, 'y': 3}
# можемо створювати інші атрибути
p1.q = 100
print(p1.q)   # 100
print(p1.__dict__)    # {'x': 2, 'y': 3, 'q': 100}


# за допомогою __slots__ наші екземпляри класу будуть мати лише ті атрибути, які ми вкажемо у магічний змінній __slots__
class PointSlots:

    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p2 = PointSlots(3, 4)
# все ще можемо звертатись до атрибутів через крапку: p2.x
print(p2.x)
# можемо змінювати значення існуючих атрибутів:
p2.x = 222
print("p2.x: ", p2.x)    # p2.x:  222

# але тепер вже немає магічної змінної __dict__
# print(p2.__dict__)   # AttributeError: 'PointSlots' object has no attribute '__dict__'

# також вже НЕ можемо створювати атрибутів
# p2.qq = 200
# print(p2.qq)   # AttributeError: 'PointSlots' object has no attribute 'qq'

"""
при використанні __slots__ наші екземпляри займають менше місця в памяті
"""
s = Point(4, 5)
# всі атрибути цього класу Point зберіг-ся в магічній змінній __dict__, і цей словник атрибутів теж займає місце в памяті
print(s.__sizeof__(), s.__dict__.__sizeof__())   # клас Point зберігає в собі посилання на сам об"єкт,
# отже сам об"єкт займає певне місце,
# і також його словник атрибутів займає певне місце

# а коли ми створюємо __slots__, то всі атрибути цього об"єкту, вже знаходяться всередині об"єкту ss
ss = PointSlots(4, 5)
print(ss.__sizeof__())   # загальний об"єм всього обсягу нашого об"єкта,
# тоді як клас Point зберігає в собі посилання на сам об"єкт, отже сам об"єкт займає певне місце,
# і також його словник атрибутів займає певне місце в памяті,
# тому при використанні слотів ми економимо память


"""
У класу, в якого є SLOTS:
операції над об"єктами класу будуть виконуватись швидше, а саме:
   - створення об"єкту (p1 = Point(3, 4))
   - зміна атрибутів (p1.x = 100)
   - звернення до цього атрибуту (p1.x)
   - видалення атрибуту (del p1.y)
"""
from timeit import timeit

def make_class1():   # w/o slots
    d = Point(5, 6)
    d.x = 100
    d.x
    del d.x

def make_class2():   # with slots
    dd = PointSlots(5, 6)
    dd.x = 100
    dd.x
    del dd.x

print(timeit(make_class1))   # 1.0783700430183671
print(timeit(make_class2))   # 0.8148730669636279
