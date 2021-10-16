"""
З наслідуванням використовуються два вбудовані методи:
isinstance() - перевіряє, чи наш об"єкт відноситься до якогось конкретного класу
та
issubclass() - дозволяє перевірити саме наслідування, чи один клас наслідується від іншого класу
"""
import pprint
"""
В пайтоні ВСЕ є об"єктом
print(isinstance((3, 4), object))
print(isinstance(555, object))
Кожен вудований тип є класом і підкласом самого об"єкту
print(issubclass(int, object))
print(issubclass(dict, object))
Кожен клас в пайтоні наслідується від класу object:
class Person(object):
    pass
print(issubclass(Person, object))
A отже кожен об"єкт, створений до нашого якогось класу буде належати класові object
a = Person()
print(isinstance(a, Person))
print(isinstance(a, object))
"""
# 1.
print(isinstance((3, 4), object))   # True
print(isinstance(555, object))   # True

# 2.
print(issubclass(int, object))   # True
print(issubclass(dict, object))   # True

# 3.
class Person:
    pass
print(issubclass(Person, object))   # True

a = Person()
print(isinstance(a, Person))   # True
print(isinstance(a, object))   # True

# ЯКІ АТРИБУТИ/ФУНКЦІЄ МАЄ ОБ"ЄКТ КЛАСУ
pprint.pprint(dir(a))
pprint.pprint(dir(Person))
# pprint.pprint(dir(a))  =  pprint.pprint(dir(Person))

"""
Коли ми створюємо будь-який клас, то він автоматично наслідується від класу object, 
а, отже, наш створений клас вже буде мати певну поведінку, яка унаслідується від класу object, які можна глянути за допомогою ф-ії:
dir(Person)
['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__' 
 .............
  '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__']
"""
print()


class MyList(list):
    pass

l = MyList()
pprint.pprint(dir(l))   # будуть доступні ВСІ методи списків

"""
клас MyList буде наслідуватись від класу list,
pprint.pprint(issubclass(MyList, list))   # True
також об"єкт l класу MyList буде нажети класу MyList, а також і його батьківському класу list
pprint.pprint(isinstance(l, MyList))
pprint.pprint(isinstance(l, list)) 
"""
pprint.pprint(issubclass(MyList, list))   # True
pprint.pprint(isinstance(MyList, object))   # True

pprint.pprint(isinstance(l, MyList))   # True
pprint.pprint(isinstance(l, list))     # True
pprint.pprint(isinstance(l, object))   # True
