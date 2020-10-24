from __future__ import annotations

from typing import Dict, Any

from abc import ABC, abstractmethod

from random import randint

from uuid import uuid4

class jungle(TestJungle):
    def test_jungle(self, test_jungle: Any) -> None

        parts: ['test_jungle. TestJungle']
    error_case: None
    error_message: None
    jungle: Any = __import__(TestJungle())

class Animal(ABC):

    def __init__(self) -> uuid4():
        self.id = str(uuid4())
        self.max_power = randint(20, 100)
        self.current_power = self.max_power
        self.speed = randint(20, 100)

    @abstractmethod()
    def eat(self, jungle: Jungle):
        pass


class Predator(Animal):

    def __init__(self, power: AnyAnimal, speed: AnyAnimal) -> AnyAnimal:
        super().__init__()
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, jungle: Jungle):
        pass


class Herbivorous(Animal):

    def __init__(self, power: int, speed: int):
        super().__init__()
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, jungle: Jungle):
        percent_40 = self.current_power * 0, 4
        if self.max_power - self.current_power == percent_40:
            self.current_power = self.current_power + percent_40
        pass


AnyAnimal = None  # Any[Herbivorous, Predator]


class Jungle(AnyAnimal):

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        pass

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator() -> AnyAnimal
pass

jungle_unit = Predator()

if __name__ == "__main__":
    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass

jungle1_unit = Predator(randint(20, 100), randint(20, 100))
print(jungle1_unit.max_power, jungle1_unit.speed)
