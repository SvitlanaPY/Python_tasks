"""
Abstract Classes - ті класи, які мають хоча б один абстрактий метод.
Абстрактий метод - це метод, якимй оголошений, але в ньому не міститься реалізації(може містити pass або рейзати ерор):
@abstractmethod
def is_ripe(self):
    raise NotImplementedError("You missed me")

@abstractmethod
    def growth(self):
        pass

Для абстрактних класів не можливо створити екземляр/об"єкт і
абстрактні класи вимагають класів-нащадків, де і будуть реалізовуватись ці абстрактні методи, оголошені в абстрактному класі.

Для визначення абстрактих класів потрібно імпортнути модуль abc і навісити @abstractmethod декоратор на метод:
from abc import ABC, abstractmethod
ABC - забезпечує те, що ми не зможемо створити з нашого класу instance-у.

Абстрактний клас здебільшого робить шаблон якогось інтерфейсу, опис методів, наприклад сторінка логування.
А вже сама реалізація описується в класах-нащадках.
З абстракцією використовується обов"язково наслідування.

Інтерфейс - це будь-які канали взаємодії користувача з вашим продуктом: екран телефона, кнопки телефона, камера тел...
Це один із паттернів проектування.
Інтерфейс - це той самий абстрактний клас, у якого ВСІ методи абстрактні.
Інтерфейс має наслідуватись від класу АВС.
Абстрактний клас - містить хоча б один абстрактний метод, але не мусить наслідуватись від класу АВС.
"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def feed(self):
        pass

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')


class Lion(Animal):
    def eat(self):
        print('Eating meat')

    def feed(self):
        print('Feeding')

    def growth(self):
        print("I am growing")

lion = Lion()
lion.eat()
lion.feed()
lion.growth()

"""
З абстрактного класу ми НЕ можемо створювати об"єкти цього класу.
"""

try:
    animal = Animal()
except TypeError as err:
    print(err)

# an = Animal()
# TypeError: Can't instantiate abstract class Animal with abstract methods feed, growth


class Animal2(ABC):

    @abstractmethod
    def feeding(self, feed_type):
        raise NotImplementedError('You missed me!!!')


class Tiger(Animal2):
    def eating(self):
        print('Eating meat')

    def feeding(self, feed_type, age):
        super().feeding(feed_type)
        print(f'I am eating {feed_type}. I am {age} years old.')


tiger = Tiger()
tiger.eating()
tiger.feeding('meat', 3)
