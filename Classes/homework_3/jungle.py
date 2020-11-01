from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
from random import randint, choice
from uuid import uuid4
import csv


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

    def eat(self, jungle: Jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
        choice_from_jun = choice(list(jungle.animals.values()))
        if self.id == choice_from_jun.id:
            self.current_power = self.current_power
        elif self.speed < choice_from_jun.speed or self.current_power < choice_from_jun.current_power:
            self.current_power -= int(self.max_power * 0.3)
            choice_from_jun.current_power -= int(choice_from_jun.max_power * 0.3)
        else:
            self.current_power += int(self.max_power * 0.4)
            jungle.remove_animal(choice_from_jun)
        if self.current_power >= self.max_power:
            self.current_power = self.max_power


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
        else:
            self.current_power += int(self.current_power + self.max_power * 0.4)
        if self.current_power > self.max_power:
            self.current_power = self.max_power


class Jungle:

    def __init__(self):
        self.animals: Dict[ str, Animal ] = dict()
        self.number = -1

    def __getitem__(self, item):
        length = len(self.animals)
        if self.number >= length - 1:
            self.number = -1
            raise StopIteration
        self.number += 1
        return list(self.animals.values())[ self.number ]

    def add_animal(self, animal: Animal):
        self.animals[ animal.id ] = animal

    def remove_animal(self, animal: Animal):
        self.animals.pop(animal.id)

    def any_predator_left(self):
        if any(isinstance(obj, Predator) for obj in self.animals.values()):
            return True
        return False


def animal_generator():
    for i in range(10):
        if i % 2 == 0:
            i = Predator(power=randint(20, 100), speed=randint(20, 100))
            i.id = uuid4()
            yield i
        else:
            i = Herbivorous(power=randint(20, 100), speed=randint(20, 100))
            i.id = uuid4()
            yield i

def dict_animal_writer(dictionary: dict):
    with open('animal.csv', 'w') as f:
        for key, value in dictionary.items():
            f.write('id: ' + str(key) + '\t' + str(value.__class__) + ' speed: ' + str(value.speed) + ' power: ' + str(value.current_power) +'\n')



if __name__ == "__main__":
    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal

    nature = animal_generator()
    jungle = Jungle()

    for i in range(10):
        animal = next(nature)
        jungle.add_animal(animal)
    print(jungle.animals)

    dict_animal_writer(jungle.animals)

    while True:
        if not jungle.any_predator_left():
            break
        for animal in jungle:
            animal.eat(jungle=jungle)

    # print(jungle.animals)
