from __future__ import annotations

import csv
from abc import ABC, abstractmethod
from random import randint, choice
from typing import Dict, Any, List
from uuid import uuid4
import json


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = str(uuid4())
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def __str__(self):
        return f"Animal {self.id},{self.__class__} power={self.current_power}, speed={self.speed}"

    def loss_power(self):
        # print("current power", self.current_power)
        self.current_power = self.current_power - int(self.max_power * 0.3)
        if self.current_power < 0:
            print("Im done, current power <0")

    def restore_power(self):
        self.current_power = min(self.max_power, self.current_power + int(self.max_power * 0.4))

    @abstractmethod
    def eat(self, jungle: Jungle):
        pass

    def if_animal_can_search_food(self):
        return self.current_power > 0

    def catch(self, prey: Animal):
        return prey.speed < self.speed

    def kill(self, prey: Animal):
        return prey.current_power < self.current_power


class Predator(Animal):

    def eat(self, jungle: Jungle):
        if not self.if_animal_can_search_food():
            jungle.remove_animal(self)
            return
        prey = jungle.get_random_animal()
        print(f'I`m predator and im gonna eating,{prey.id}')
        if prey.id == self.id:
            print("oops,shit happens")
            self.loss_power()
            return
        if self.catch(prey):
            if self.kill(prey):
                jungle.remove_animal(prey)
            else:
                self.loss_power()
                prey.loss_power()
        else:
            self.loss_power()
            prey.loss_power()


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        print(f"I`m herbivorous and  im gonna eating , my ID {self.id}")
        if self.if_animal_can_search_food():

            self.restore_power()
        else:
            jungle.remove_animal(self)


# AnyAnimal = Any[Herbivorous, Predator]


class Jungle:

    def __init__(self):
        self.animals: Dict[str, Animal] = dict()
        self.number = 0

    def __getitem__(self, item):
        length = len(self.animals)
        if self.number >= length:
            self.number = 0
            raise StopIteration
        self.number += 1
        return list(self.animals.values())[self.number]

    def get_random_animal(self):
        return choice(list(self.animals.values()))

    def add_animal(self, animal: Animal):
        self.animals[animal.id] = animal
        # with open("animals_from_jungle.json", "a") as file:
        #     json.dump(str(animal), file)
        with open('animals_from_jungle.csv', 'a', newline='') as file:
            writer = csv.writer(file, delimiter=" ")
            writer.writerow(str(animal))

    def remove_animal(self, animal: Animal):
        self.animals.pop(animal.id)

    def any_predator_left(self):
        if any(isinstance(animal, Predator) for self.animals in jungle.animals.values()):
            return True
        return False


def animal_generator():
    while True:
        if randint(1, 2) == 1:
            yield Herbivorous(power=randint(20, 100), speed=randint(20, 100))
        else:
            yield Predator(power=randint(20, 100), speed=randint(20, 100))


if __name__ == "__main__":
    gen = animal_generator()
    jungle = Jungle()
    for i in range(11):
        jungle.add_animal(next(gen))

    for animal in jungle:
        print(f"Animal id - {animal.id} - Animal  power {animal.current_power} - Animal speed {animal.speed}")

    # while True:
    #     if not jungle.any_predator_left():
    #         print("game over")
    #         break
    #     for animal in jungle:
    #         animal.eat(jungle=jungle)

    while True:
        if any(isinstance(animal, Predator) for animal in jungle.animals.values()):
            try:
                for animal in jungle.animals.values():
                    animal.eat(jungle=jungle)
            except RuntimeError:
                continue
            else:
                print("game over")
                break

