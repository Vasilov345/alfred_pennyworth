from __future__ import annotations

from typing import Dict, Any


class Animal:

    def __init__(self, power: int, speed: int):
        self.id = None
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, jungle: Jungle):
        pass


class Predator:

    def eat(self, jungle: Jungle):
        pass


class Herbivorous:

    def eat(self, jungle: Jungle):
        pass


AnyAnimal = Any[Herbivorous, Predator]


class Jungle:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        pass

    def remove_animal(self, animal: AnyAnimal):
        pass


def animal_generator():
    pass


if __name__ == "__main__":
    # Create jungle
    # Create few animals
    # Add animals to jungle
    # Iterate throw jungle and force animals to eat until no predators left
    # animal_generator to create a random animal
    pass
