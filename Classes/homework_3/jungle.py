from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any
import uuid
import random


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = str(uuid.uuid4())
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, jungle: Jungle):
        pass

    def set_power(self, power: int):
        if power > self.max_power:
            self.current_power = self.max_power
        else:
            self.current_power = power


class Predator(Animal):

    def eat(self, jungle: Jungle):
        victim_key = self.choose_victim(jungle)
        if self.id == victim_key:
            return print('Bad day')
        victim: Any[Predator, Herbivorous] = jungle.animals[victim_key]
        if self.speed <= victim.speed or self.current_power <= victim.current_power:
            self.set_power(int(self.max_power * 0.7))
            victim.set_power(int(victim.max_power * 0.7))
            return print('You`re so weak and lost 30% of your power!')

        victim.set_power(0)  # Self is stronger and faster than his victim... kill him!
        self.set_power(int(self.max_power * 1.3))

    @staticmethod
    def choose_victim(jungle: Jungle):
        keys = jungle.animals.keys()
        return random.choice(list(keys))

    # count_animals = len(keys)


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        self.set_power(int(self.max_power * 1.4))


# AnyAnimal = Any[Herbivorous, Predator]


class Jungle:


    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal: AnyAnimal):
        del self.animals[animal.id]

    def any_predator_left(self):
        for animal in self.animals.values():
            if animal.__class__.__name__ == 'Predator' and animal.current_power > 0:
                return True
        return False

    def __iter__(self):
        return self.animals.__iter__()

def animal_generator(max_animals: int):
    animals = [Predator, Herbivorous]
    for i in range(0, max_animals):
        power, speed = random.randint(20, 101), random.randint(20, 101)
        yield animals[random.randint(0, 1)](power, speed)


if __name__ == "__main__":
    jungle = Jungle()
    print('List of animals:')
    for animal in animal_generator(5):
        jungle.add_animal(animal)
        print(animal.__class__.__name__, animal.id, animal.current_power, animal.speed)
    print('Starting eat!')
    while jungle.animals:

        if not jungle.any_predator_left():
            print('The end')
            break

        for animal in jungle.animals.values():
            if animal.current_power != 0:
                animal.eat(jungle)

        animal.eat(jungle)
        print(animal.__class__.__name__, animal.id, animal.current_power, animal.speed)
        # print(animal.id, animal.current_power)

    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal
