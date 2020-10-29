from __future__ import annotations
from abc import ABC, abstractmethod
import time
from typing import Dict, Any
import uuid
import random
import csv


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

    filename = 'csv_jungle.csv'
    # convert my jungle to csv file (Dict format)
    try:
        with open(filename, 'w', newline='') as csv_files:
            fieldnames = ['name', 'id', 'power', 'speed']
            writer = csv.DictWriter(csv_files, fieldnames=fieldnames)
            writer.writeheader()
            for item in animal_generator(10):
                writer.writerow({'name': item.__class__.__name__, 'id': item.id, 'power': item.current_power,
                                 'speed': item.speed})
    except BaseException as e:
        print('BaseException:', filename)
    else:
        print('Data has been loaded successfully !')

    #Load my jungle(animals) from csv file and print
    print('List of animals:')
    with open('csv_jungle.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for item in reader:
            if item['name'] == 'Predator':
                animal = Predator(0, 0)
            else:
                animal = Herbivorous(0, 0)
            animal.id = item['id']
            animal.speed = int(item['speed'])
            animal.max_power = int(item['power'])
            animal.current_power = int(item['power'])
            jungle.add_animal(animal)

    while jungle.animals:
        # if there is no predator or only one predator left in jungle then finish game
        if not jungle.any_predator_left() or (
                len(jungle.animals) == 1 and list(jungle.animals.values())[0].__class__.__name__ == "Predator"):
            print('The end')
            break

        #Game start
        print('Start eating!')
        for animal in jungle.animals.values():
            if animal.current_power > 0:
                animal.eat(jungle)
        jungle.clear_dead_animals()

        time.sleep(0.5)
        print('---------------------------')
        for animal in jungle.animals.values():
            print(animal.__class__.__name__, animal.id, animal.current_power, animal.speed)
