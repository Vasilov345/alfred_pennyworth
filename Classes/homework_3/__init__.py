from __future__ import annotations

from typing import Dict, Any

from abc import ABC, abstractmethod

from random import randint

from uuid import uuid4

class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = str(uuid4())
        self.max_power = randint(20, 100)
        self.current_power = self.max_power
        self.speed = randint(20, 100)

    @abstractmethod()
    def eat(self, jungle: Jungle):
        pass


class Predator(Animal):

    def __init__(self, power: int, speed: int):
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, jungle: Jungle):
        pass


class Herbivorous(Animal):

    def __init__(self, power: int, speed: int):
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, jungle: Jungle):
        percent_40 = self.current_power * 0, 4
        if self.max_power - self.current_power == percent_40:
            self.current_power = self.current_power + percent_40
        pass


AnyAnimal = None


# Any[Herbivorous, Predator]


class Jungle:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        pass

    def remove_animal(self, animal: AnyAnimal):
        pass

    def __iter__(self):
        pass


animal_lst = []


def animal_generator():
    for i in range(10):
        if i <= 4:
            i = Predator(randint(20, 100), randint(20, 100))
            animal_lst.append((i))
        else:
            i = Herbivorous(randint(20, 100), randint(20, 100))
            animal_lst.append(i)
    return animal_lst


animal_generator()

for step_animal in animal_lst:
    unique_id = str(uuid4())
    step_animal.id = str(uuid4())
    print((f" Animal power: {animal_lst[i].max_power} Animal speed: {animal_lst[i].speed} ID: {unique_id}"))

print("test")

jungle1_unit = Predator(randint(20, 100), randint(20, 100))
print(jungle1_unit.max_power, jungle1_unit.speed)

# Create jungle
# Create few animals
# Add animals to jungle
# Iterate throw jungle and force animals to eat until no predators left
# animal_generator to create a random animal
