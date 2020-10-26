with open('animals.json', 'r') as f:
    animals_json = Animal['animals']
    print(animals_json)


class Animal:

    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def __str__(self):
        return f"Animal {self.power} {self.speed}"

    def __repr__(self):
        return f"Animal {self.power} {self.speed}"


cat = Animal(20, 40)


class List(Animal):


    pass

true_animals: List[Animal] = []
true_animals = [Animal(power=i['power'], speed=i['speed']) for i in animals_json]
print(true_animals)
