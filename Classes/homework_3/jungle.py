from __future__ import annotations
from abc import ABC, abstractmethod
import time
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
            print(self.id, 'Bad day')
            return
        victim: Any[Predator, Herbivorous] = jungle.animals[victim_key]
        if self.speed <= victim.speed or self.current_power <= victim.current_power:
            self.set_power(int(self.current_power * 0.7))
            victim.set_power(int(victim.current_power * 0.7))
            print(self.id, 'You`re so weak and lost 30% of your power!')
            return

        victim.set_power(0)  # Self is stronger and faster than his victim... kill him!
        self.set_power(int(self.current_power * 1.3))

    @staticmethod
    def choose_victim(jungle: Jungle):
        keys = jungle.animals.keys()
        return random.choice(list(keys))


class Herbivorous(Animal):
    def eat(self, jungle: Jungle):
        self.set_power(int(self.current_power * 1.4))


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

    def clear_dead_animals(self):
        res = [animal for animal in self.animals.values() if animal.current_power > 0]
        if res == self.animals.values():
            return
        self.animals.clear()
        for animal in res:
            jungle.add_animal(animal)

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

    while jungle.animals:
        # if there is no predator or only one predator left in jungle then finish game
        if not jungle.any_predator_left() or (
                len(jungle.animals) == 1 and jungle.animals.values()[0].__class__.__name__ == "Predator"):
            print('The end')
            break

        print('Start eating!')
        for animal in jungle.animals.values():
            if animal.current_power > 0:
                animal.eat(jungle)
        jungle.clear_dead_animals()

        time.sleep(1)
        print('---------------------------')
        for animal in jungle.animals.values():
            print(animal.__class__.__name__, animal.id, animal.current_power, animal.speed)
