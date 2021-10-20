"""
Композиція - це є спеціалізована форма асоціації.
Композиція - це метод об"єднання простих об"єктів чи типів даних у більш складні.

Асоціація - зв"язок/відносини між двома класами без будь-яких правил.

Створюємо в контейнер-класі Book об"єкт/и іншого незалежного класу Page і,
якщо контейнер знищується, то знищується і сам об"єкт, який був у ньому.

Клас-контейнер НЕ може існувати окремо від контейнера.

Якщо ми знищуємо об"єкт book класу Book, то ми автоматично знищимо два об"єкти (page1, page2) класу Page.

"""

class Book:       # клас-контейнер
    def __init__(self):
        # page1 і page2 - об"єкти класу Page,
        # в класі Page є атрибут об"єкту self.content, і доступ до нього можливий лише через клас-контейнер,
        self.page1 = Page(10)
        self.page2 = Page('This is content for page2')

        # self.pages = [page1, page2]


class Page:
    def __init__(self, content):
        self.content = content
#         page1 = Page(10)


book = Book()
# book - об"єкт класу Book
# print(book.pages[0])
print(book.page1.content)
# 10
print(book.page2.content)
# This is content for page2
book.page1.content = "Новий зміст сторінки page1"
print(book.page1.content)
# Новий зміст сторінки page1


print("^ "*15)
# class Laptop:
#     """
#     Make the class with composition.
#     """
# class Battery:
#     """
#     Make the class with composition.
#     """

class Laptop:  # class-container
    def __init__(self):
        self.battery1 = Battery(50)
        self.battery2 = Battery()


class Battery:
    def __init__(self, charge_level=100):
        self.charge_level = charge_level


laptop = Laptop()
print(laptop.battery1)
# OUTPUT: <__main__.Battery object at 0x7f398edc8d60>
print(laptop.battery1.charge_level)
# 50
print(laptop.battery2.charge_level)
# 100
