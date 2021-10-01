"""
Создайте класс Person, у которого есть:

конструктор __init__, принимающий 3 аргумента: first_name, last_name, age.
метод full_name, который возвращает строку в виде "<Фамилия> <Имя>"
метод is_adult, который возвращает True, если человек достиг 18 лет и False в противном случае;
p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())  # выводит "Hendrix Jimi"
print(p1.is_adult()) # выводит "True"
"""


class Person(object):

    def __init__(self, n, s, a):
        self.first_name, self.last_name, self.age = n, s, a

    def full_name(self):
        return f'{self.last_name} {self.first_name}'

    def is_adult(self):
        return self.age >= 18


p1 = Person('Jimi', 'Hendrix', 55)
print(p1.full_name())   # выводит "Hendrix Jimi"
print(p1.is_adult())   # выводит "True"