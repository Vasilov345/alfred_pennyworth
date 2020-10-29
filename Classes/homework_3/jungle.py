from __future__ import annotations
from abc import ABC, abstractmethod
from uuid import uuid4
from random import randint, choice
from typing import Dict, Any


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, jungle: Jungle):
        raise NotImplementedError


class Predator(Animal):

    def eat(self, other):
        other = choice(list(other.values()))
        print(self.current_power)
        print(other.current_power)
        if self.id == other.id:
            self.current_power = self.current_power
        elif self.speed < other.speed or self.current_power < other.current_power:
            self.current_power -= (self.max_power * 30) / 100
            other.current_power -= (other.max_power * 30) / 100
            if self.current_power <= 0:
                self.current_power = 0
                print(self.id)
                obj_Jung.remove_animal(self)
                print(self.id)
            if other.current_power <= 0:
                other.current_power = 0
                obj_Jung.remove_animal(other)
        else:
            self.current_power += (self.max_power * 40) / 100
            if self.current_power >= self.max_power:
                self.current_power = self.max_power

        print(self.current_power)
        print(other.current_power)


class Herbivorous(Animal):

    def eat(self):
        self.current_power += (self.max_power * 40) / 100
        if self.current_power >= self.max_power:
            self.current_power = self.max_power


#
# AnyAnimal = Any[ Herbivorous, Predator ]


class Jungle:

    def __init__(self):
        self.animals: Dict[ str, AnyAnimal ] = dict()
        self.animals_2 = self.animals

    def add_animal(self, animal: AnyAnimal):
        self.animals[ animal.id ] = animal

    def remove_animal(self, animal: AnyAnimal):
        self.animals.pop(animal.id)


obj_Jung = Jungle()


def animal_generator():
    for i in range(10):
        if i % 2 == 0:
            i = Predator(randint(20, 101), randint(20, 101))
            i.id = uuid4()
            yield i
        elif i % 2 == 1:
            i = Herbivorous(randint(20, 101), randint(20, 101))
            i.id = uuid4()
            yield i


for i in animal_generator():
    obj_Jung.add_animal(i)
print(obj_Jung.animals)


if __name__ == "__main__":
    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass
