from random import randint
from typing import Any
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        self.id = id
        power = randint(20, 100)
        self.speed = randint(20, 100)
        self.current_power = power
        self.max_power = power

    @abstractmethod
    def eat(self, jungle):
        raise NotImplementedError


class Predator(Animal):

    def eat(self, jungle):
        count_animals = len(jungle.animals.keys())
        force_key = randint(1, count_animals)
        force_animal: Any[Predator, Herbivorous] = jungle.animals[force_key]
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

    def eat(self, jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
        self.current_power += (self.max_power / 100) * 40
        if self.current_power > self.max_power:
            self.current_power = self.max_power
        return self.current_power


class Jungle:
    def __init__(self):
        self.animals = dict()  # Створили словник з

    def add_animal(self, animals_from_gen):
        # створюємо для кожної тварини число як ключ
        key = len(self.animals.keys()) + 1
        self.animals[key] = animals_from_gen

    def remove_animal(self, jungle):
        animal_list_values = [a for a in self.animals.values()]
        animal_list_keys = [k for k in self.animals.keys()]
        index_of_animal = animal_list_values.index(animal)
        key = animal_list_keys[index_of_animal]
        del self.animals[key]


def animal_generator():
    animals_from_gen = [Predator, Herbivorous]
    for i in range(1, 5):
        yield animals_from_gen[randint(0, 1)]()


jungle = Jungle()
for animal in animal_generator():
    jungle.add_animal(animal)

    while jungle.animals:
        is_predator = bool([animal for animal in jungle.animals.values() if animal.__class__.__name__ == 'Predator'])

        if is_predator == False:
            print('The end')
            print(animal, animal.current_power)
            break

        count_animals = len(jungle.animals.keys())
        animal = jungle.animals[randint(1, count_animals)]

        animal.eat(jungle)