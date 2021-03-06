"""
Генератор - це ітератор, елементи якого можна обійти в циклі лише ОДИН раз.
Елементи генератора не зберігаються в пам"яті всі разом, а формуються на льоту.
При кожному новому зверненні до генератора всередині циклу чи за допомогою ф-ії next(), ми отримуємо наступний елемент,
і всі ці елементи НЕ зберігаються в пам"яті.
Сам цикл for викликає ф-ію next() і вона буде брати кожен наступний елемент колекції, але не буде їх зберігати в памяті.

Ітератор - об"єкт, який підтримує ф-ію next().
і при виклику цієї функції він(ітератор) бере наступний елемент колекції.
Ф-ія next() запам"ятовує, який елемент буде братись наступним.
Ітератор завжди зберігає інформацію, який елемент буде братись наступним.

Ітератор представляє собою колекцію, елементи якої можна по-черзі обійти лише ОДИН раз,
а обхід елементів цієї колекції відбувається шляхом виклику ф-ії next(),

Ітерабельними є об"єкти, які:
1. дають можливість обходити свої елементи по черзі в циклі, і
2. можуть бути перетворені до ітератора за допомогою ф-ії iter().
Списки є ітерабельними об"єктами.
Самі по собі списки не підримують ф-ію next(), бо вони не є ітератором, але
списки можна перетворити в ітератор, застосувавши ф-ію iter():
a = [1, 2, 3, 4, 5]
b = iter(a)
print(b)   # <list_iterator object at 0x7f1ad0f7b2e0>
Тепер ми можемо викликати ф-ію next() до нашого ітератора b:
next(b)
При першому виклику, ми отримаємо перший елемент колекції(списку а),
при другому виклику - другий...і так до кінця,
і коли дійдемо до кінця, то отримаємо помилку StopIteration.

Отже, ітерабельні об"жкти НЕ є ітераторами, но з них можна зробити ітератор за допомогою ф-ії iter().

ГЕНЕРАТОР є ітератором. Отже ми можемо до генератора застосовувати ф-ію next()
с = (i ** 2 for i in range(1,6))
next(с) - отримаємо перший елемент колекції.

Генератори можна:
1. перетворювати в списки: list(c)
2. До генераторів не можна застосувати ф-ію len():  # TypeError: object of type 'generator' has no len()
3. До генераторів не можна застосовувати індекс: cc[1] ===>  # TypeError: 'generator' object is not subscriptable

"""

c = (i ** 2 for i in range(1, 6))
print(next(c))    # 1
print(next(c))    # 4
print(next(c))    # 9
print(next(c))    # 16
print(next(c))    # 25
# print(next(с))    # StopIteration


k = (i ** 2 for i in range(10, 16))
print('first')
for i in k:
    print(i, end=' ')
    # 100 121 144 169 196 225 second
print('second')
for i in k:
    print(i, end=' ')

"""
Генератори можна перетворювати в списки:
"""
cc = (i ** 2 for i in range(1, 6))
print(list(cc))   # [1, 4, 9, 16, 25]

"""
до генераторів не можна застосувати ф-ію len():  len(cc)  ===> TypeError: object of type 'generator' has no len()
"""
# print(len(cc))   # TypeError: object of type 'generator' has no len()

"""
До генераторів не можна застосовувати індекс: cc[1] ===>  # TypeError: 'generator' object is not subscriptable
"""
# print(cc[1])   # TypeError: 'generator' object is not subscriptable
