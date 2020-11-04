from __future__ import annotations
import uuid
import random
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, power, speed):
        self.id = str(uuid.uuid4())
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, jungle: Jungle):
        pass


class Predator(Animal):

    def eat(self, jungle: Jungle):
        any_animal = random.choice([x for x in jungle.animals.values()])
        if self.current_power <= 0:
            jungle.remove_animal(self)
        elif any_animal.id == self.id:
            self.current_power -= 0.3 * self.max_power
        else:
            if self.speed > any_animal.speed and self.current_power > any_animal.current_power:
                self.current_power += 40
                if self.current_power > self.max_power:
                    self.current_power = self.max_power
            else:
                self.current_power -= 0.3 * self.max_power
                any_animal.current_power -= 0.3 * any_animal.max_power


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
        else:
            self.current_power += 40
            if self.current_power > self.max_power:
                self.current_power = self.max_power


class Jungle:

    def __init__(self):
        self.animals = dict()

    number: int = - 1

    def __getitem__(self, item):
        length = len(self.animals)
        if self.number >= length - 1:
            self.number = -1
            raise StopIteration
        self.number += 1
        return list(self.animals.values())[self.number]

    def add_animal(self, animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal):
        self.animals.pop(animal.id)
        return self.animals


def animal_generator():
    for random_animal in range(10):
        if random.randint(1, 2) == 1:
            yield Predator(power=random.randint(20, 100), speed=random.randint(20, 100))
        else:
            yield Herbivorous(power=random.randint(20, 100), speed=random.randint(20, 100))


if __name__ == "__main__":
    # jungle = Jungle()
    # nature = animal_generator()
    #
    # while True:
    #     try:
    #         jungle.add_animal(next(nature))
    #     except StopIteration:
    #         break
    #
    # while True:
    #     if any(isinstance(animal, Predator) for animal in jungle.animals.values()):
    #         try:
    #             for animal in jungle.animals.values():
    #                 animal.eat(jungle=jungle)
    #         except RuntimeError:
    #             continue
    #     else:
    #         break
    pass
