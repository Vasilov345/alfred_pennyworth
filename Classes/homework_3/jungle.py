from __future__ import annotations
import csv
import time
import uuid
import random
from abc import ABC, abstractmethod
from pprint import pprint
from typing import Dict, Any, List


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = str(uuid.uuid4())
        self.max_power = power
        self._current_power = power
        self.speed = speed

    @property
    def current_power(self):
        return self._current_power

    @current_power.setter
    def current_power(self, power):
        if power > self.max_power:
            self._current_power = self.max_power
        else:
            self._current_power = power

    @abstractmethod
    def eat(self, jungle: Jungle):
        raise NotImplementedError


class Predator(Animal):

    def eat(self, jungle: Jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
            return self._current_power

        rand_animal = random.choice(list(jungle.animals.values()))
        if self.id == rand_animal.id:
            print("Predator catch himself")
            self.current_power *= 0.7
            self.current_power = int(self.current_power)
        else:
            if self.speed > rand_animal.speed and self.current_power > rand_animal.current_power:
                jungle.remove_animal(rand_animal)
                print(f"Predator ate {rand_animal.__class__}")
                self.current_power *= 1.4  # Here i use + 40 %
                self._current_power = int(self._current_power)
            else:
                self.current_power *= 0.7
                self._current_power = int(self._current_power)
                print("Predator did`nt catch anyone")
                rand_animal.current_power *= 0.7
                rand_animal.current_power = int(rand_animal.current_power)
        return self._current_power


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if self.current_power <= 0:
            jungle.remove_animal(self)
        else:
            self.current_power *= 1.4
            print("Herbivorous eat")
            self._current_power = int(self._current_power)
        return self._current_power


# AnyAnimal = Any[Herbivorous, Predator]  # Have no idea what to do with it


class Jungle:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    index = 0
    copy_of_dict = {}

    def __next__(self):
        if self.copy_of_dict == {}:
            self.copy_of_dict = self.animals.copy()

        self.index = len(self.copy_of_dict.values())
        while self.copy_of_dict.values():  # if jungle.animals != 0
            for ident, obj in self.copy_of_dict.items():
                if self.index > 0:
                    self.copy_of_dict.pop(ident)
                    self.index -= 1
                    return obj
        raise StopIteration

        # Shows first elem from animal n-times
        # while self.index < len(self.animals.values()):
        #     for obj in list(self.animals.values()):
        #         self.index += 1
        #         return obj
        # raise StopIteration

    def __iter__(self):
        return self

    def add_animal(self, animal: AnyAnimal):
        self.animals[animal.id] = animal
        return self.animals

    def remove_animal(self, animal: AnyAnimal):
        self.animals.pop(animal.id)
        return self.animals

    def check_if_all_predators_die(self):
        for obj in self.animals.values():
            if isinstance(obj, Predator):
                return False
        return True


def obj_info():
    lst = []
    for id, obj in jungle.animals.items():
        list_animals = [f"{obj.__class__.__name__}", f"{obj.max_power}", f"{obj.speed}", f"{obj.id}"]
        lst.append(list_animals)
    pprint(lst)
    return lst


def convert_to_csv():
    print("Wrote info about animal in separate file")
    with open("animal_in.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(['class', 'power', 'speed', 'id'])
        writer.writerows(obj_info())


def animal_generator(list_of_animals: List[AnyAnimal]):  # Not sure it works properly
    for an in list_of_animals:
        yield an


if __name__ == "__main__":
    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal

    jungle = Jungle()

    # Creating our instances of animals
    animal_list = []
    for i in range(4):
        rand_int = random.randint(0, 1)
        if rand_int == 0:
            animal_list.append(Predator(random.randint(20, 100), random.randint(20, 100)))
        else:
            animal_list.append(Herbivorous(random.randint(20, 100), random.randint(20, 100)))

    AnyAnimal = any(animal_list)

    # Creating animal generator
    animal_gen = animal_generator(animal_list)
        # Add animals to jungle
    for i in animal_gen:
        jungle.add_animal(i)


    for id, obj in jungle.animals.items():
        print(f"{obj.__class__} power: '{obj.max_power}', Animal speed: '{obj.speed}', id: {id}")
    convert_to_csv()

    # while True:
    for animal in jungle:
        if jungle.check_if_all_predators_die():
            print("All Predators died")
            print("Game Over")
            break
        animal.eat(jungle=jungle)
        time.sleep(0.5)
