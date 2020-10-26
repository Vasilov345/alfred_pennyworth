import json

with open('animals.json', 'r') as f:
    animals_json = json.load(f)
    animals_json = animals_json['animals']
    print(animals_json)


class Animal:

    def __init__(self, speed, power):
        self.speed = speed
        self.power = power

    def __str__(self):
        return f"Animal {self.power} {self.speed}"

    def __repr__(self):
        return f"Animal {self.power} {self.speed}"


dog = Animal(20, 50)
# class List(Animal):
# pass

true_animals: List[Animal] = []
true_animals = [Animal(power=, speed=) for i in animals_json
print(true_animals)

with open("animals.json", 'r') as f:
    result = f.readlines()
print(f'List of animals in animals.json {type(result)}: {result}')

main_path = "dir_with_files"
path = os.path.join(main_path, "animals.json")
