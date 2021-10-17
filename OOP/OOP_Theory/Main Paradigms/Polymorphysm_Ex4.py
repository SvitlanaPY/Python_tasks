class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a cat and my name is {self.name} and I am {self.age} years old')

    def make_sound(self, sound):
        print(sound)
        print('Meow')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f'I am a dog and my name is {self.name} and I am {self.age} years old')

    def make_sound(self, sound=''):
        print(sound)
        print('Guffff')

catt = Cat('Tom', 3)
dogg = Dog('Rex', 5)


"""
У нас два різні об"єкти: catt та dogg; 
у них різні типи: тип Cat та тип Dog (різні незалежні один від одного класи)
Але вони виконують одну і ту саму ф-ість/інтерфейс (методи з однаковою назвою): make_sound(), але яка працює по-різному.
"""
c_d = (catt, dogg)

for animal in (catt, dogg):   # = for animal in c_d:
    animal.make_sound('grrr')
    animal.info()
    animal.make_sound('')

# Meow
# I am a cat and my name is Tom and I am 3 years old
# Meow
# Guffff
# I am a dog and my name is Rex and I am 5 years old
# Guffff
