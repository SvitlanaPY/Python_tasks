"""
magic methods = dunder methods (Double UNDERscore) -
це спеціальні методи, які починаються і закінчуються на два нижніх підкреслення.
Ці методи мають певний функціонал і викликаються всередині класу у певний момент.
"""

"""
8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
otherwise return message: "Your city is too small".
"""

class City:
     def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            print("Your city is too small")

     def __init__(self, name, population):
         self.name = name
         self.population = population


w = City('City1', 1000)
print(w)
# OUTPUT: Your city is too small; None (no new object returned)
W = City('City2', 10000)
print(W)
# OUTPUT: <__main__.City object at 0x7f4dfb86a760>
