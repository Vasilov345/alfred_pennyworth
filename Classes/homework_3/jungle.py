from future import annotations

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

    def eat(self, jungle: Jungle)