"""
Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент - значение,
с которого начинается подсчет, по умолчанию равно 0.
Также нужно создать метод increment, который увеличивает счетчик на 1.
Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>"
и метод reset,  который обнуляет экземпляр счетчика.

Пример работы с классом Counter:
c1 = Counter()
c1.start_from()
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 1"
c1.increment()
c1.display() # печатает "Текущее значение счетчика = 2"
c1.reset()
c1.display() # печатает "Текущее значение счетчика = 0"

c2 = Counter()
c2.start_from(3)
c2.display() # печатает "Текущее значение счетчика = 3"
c2.increment()
c2.display() # печатает "Текущее значение счетчика = 4"
"""


class Counter:
    def start_from(self, value=0):
        self.counter = value

    def increment(self):
        self.counter += 1

    def display(self):
        print(f"Дане значення лічильника = {self.counter}")

    def reset(self):
        self.counter = 0


c1 = Counter()
c1.start_from()
print(c1.display())
# Дане значення лічильника = 0
c1.increment()
print(c1.display())
# Дане значення лічильника = 1
c1.increment()
print(c1.display())
# Дане значення лічильника = 2
c1.increment()
print(c1.display())
# Дане значення лічильника = 3
c1.reset()
print(c1.display())
# Дане значення лічильника = 0

c2 = Counter()
c2.start_from(3)
print(c2.display())
# Дане значення лічильника = 3
c2.increment()
print(c2.display())
# Дане значення лічильника = 4
c2.increment()
print(c2.display())
# Дане значення лічильника = 5
