from __future__ import annotations
from uuid import uuid4
from abc import ABC, abstractmethod
from random import randint
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, jungle: Jungle):
        raise NotImplementedError


class Predator(Animal):

    def eat(self, jungle: Jungle):
        count_animals = len(jungle.animals.keys())
        force_key = randint(1, count_animals)
        force_animal = jungle.animals[force_key]
        if force_animal.id == self.id:
            self.current_power -= (self.max_power / 100) * 40
        else:
            if self.speed > force_animal.speed and self.current_power > force_animal.current_power:
                self.current_power += (self.max_power / 100) * 40
                jungle.animals.pop(force_key)
                if self.current_power > self.max_power:
                    self.current_power = self.max_power
            else:
                self.current_power -= (self.max_power / 100) * 40
                return self.current_power


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
        self.current_power += (self.max_power / 100) * 40
        if self.current_power > self.max_power:
            self.current_power = self.max_power
        return self.current_power




class Jungle:

    def __init__(self):
        self.animals = dict()

    def add_animal(self, animal):
        self.animals[animal.id] = animal
        return self.animals

    def remove_animal(self, animal):
        self.animals.pop(animal.id)
        return self.animals

    def any_predator_left(self):
        count = 0
        if any(isinstance(animal, Predator) for self.animals in jungle.animals.values()):
            return True
        else:
            False


def animal_generator():
    animals =[Predator, Herbivorous]
    for i in range(10):
        yield animals[randint(0, 1)](randint(20, 100), randint(20, 100))



if __name__ == "__main__":
    nature = animal_generator()
    jungle = Jungle()
    for i in range(10):
        animal = next(nature)
        jungle.add_animal(animal)

    while True:
        if not jungle.any_predator_left():
            break
        for animal in jungle.animals:
            animal.eat(jungle=jungle)
        time.sleep(1)
