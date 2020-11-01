from __future__ import annotations
from uuid import uuid4
from abc import ABC, abstractmethod
from random import randint, choice
import csv


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = str(uuid4())
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, jungle: Jungle):
        raise NotImplementedError

    def animal_can_search_food(self):
        return self.current_power > 0

    def loss_power(self):
        self.current_power = self.current_power - int(self.max_power*0.3)

    def restore_power(self):
        self.current_power = min(self.max_power, self.current_power + int(self.max_power*0.4))
        if self.current_power > self.max_power:
            self.current_power = self.max_power



class Predator(Animal):


    def eat(self, jungle):

        if not self.animal_can_search_food():
            jungle.remove_animal(self)
            return

        prey_animal = jungle.get_rand_animal()

        if prey_animal.id == self.id:
            prey_animal.loss_power()

        if self.catch(prey_animal):

            if self.kill(prey_animal):
                self.restore_power()
                jungle.remove_animal(prey_animal)
            else:
                self.loss_power()
                prey_animal.loss_power()
                if not self.animal_can_search_food():
                    jungle.remove_animal(self)
                    return

        else:
            self.loss_power()
            prey_animal.loss_power()
            if not self.animal_can_search_food():
                jungle.remove_animal(self)
                return


    def catch(self, prey_animal):
        return prey_animal.speed < self.speed

    def kill(self, prey_animal):
        return prey_animal.current_power < self.current_power


class Herbivorous(Animal):

    def eat(self, jungle: Jungle):
        if not self.animal_can_search_food():
            jungle.remove_animal(self)
            return
        else:
            self.restore_power()


class Jungle:

    def __init__(self):
        self.animals = dict()
        self.number = -1

    def __getitem__(self, item):
        leng = len(self.animals)
        if self.number >= leng -1:
            self.number = -1
            raise StopIteration
        self.number += 1
        return list(self.animals.values())[self.number]

    def any_predator_left(self):
        if any(isinstance(animal, Predator) for animal in jungle.animals.values()):
            return True

    def add_animal(self, animal: Animal):
        self.animals[animal.id] = animal

    def remove_animal(self, animal: Animal):
        self.animals.pop(animal.id)

    def get_rand_animal(self):
        return choice(list(jungle.animals.values()))


def animal_generator():
    animals = [Predator, Herbivorous]
    for i_animals in range(10):
        yield animals[randint(0, 1)](power=randint(20, 100), speed=randint(20, 100))

def creator_CSV(jungle):
    lst =[]
    for k, v in jungle.animals.items():
        list_animals = [f"{v.__class__.__name__}", f"{v.max_power}", f"{v.speed}", f"{v.id}"]
        lst.append(list_animals)
    with open("animals.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(['class', 'power', 'speed', 'id'])
        writer.writerows(lst)


if __name__ == "__main__":
    nature = animal_generator()

    jungle = Jungle()
    for i in range(10):
        animal = next(nature)
        jungle.add_animal(animal)
    creator_CSV(jungle)
    while True:
        if not jungle.any_predator_left():
            print(f"list of Herbivorous left {jungle.animals}")
            break
        for animal in jungle:
            animal.eat(jungle=jungle)

