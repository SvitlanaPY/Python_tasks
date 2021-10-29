from __future__ import annotations
from random import randint
from abc import abstractmethod
from typing import Dict, Union
import uuid


class Animal:

    def __init__(self, power: int, speed: int):
        self.id = str(uuid.uuid4())
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predator(Animal):
    def __init__(self):
        Animal.__init__(self, power=randint(25, 100), speed=randint(25, 100))

    def eat(self, forest: Forest):
        pass


class Herbivore(Animal):
    def __init__(self):
        Animal.__init__(self, randint(25, 100), randint(25, 100))
        
    def eat(self, forest: Forest):
        pass


AnyAnimal: Union[Herbivore, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator(n):
    while n != 0:
        yield Predator()
        n -= 1
        yield Herbivore()
        n -= 1


if __name__ == "__main__":
    forest = Forest()
    for i in animal_generator(10):
        animal = i
        print(animal)
        forest.add_animal(animal)

    # Create forest
    # Create few animals
    # Add animals to forest

    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
pass

# pred = Predators()
# herb = Herbivorous()
# print()

