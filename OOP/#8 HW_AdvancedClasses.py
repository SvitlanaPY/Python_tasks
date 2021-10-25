from __future__ import annotations
from random import randint
from abc import ABC, abstractmethod
from typing import Dict, Any, Union


class Animal:

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predators(Animal):
    def __init__(self):
        Animal.__init__(self, power=randint(25, 100), speed=randint(25, 100))

    def eat(self, forest: Forest):
        pass


class Herbivorous(Animal):
    def __init__(self):
        Animal.__init__(self, randint(25, 100), randint(25, 100))
        
    def eat(self, forest: Forest):
        pass


AnyAnimal: Union[Herbivorous, Predators]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        pass

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator():
    pass


if __name__ == "__main__":
    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass


pred = Predators()
herb = Herbivorous()
print()
