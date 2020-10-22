import unittest

from jungle import Animal, Herbivorous, Predator, Jungle


class TestBaseAnimal(unittest.TestCase):

    def test_animal_should_be_abstract(self):
        self.assertRaises(TypeError, Animal)


class TestHerbivorous(unittest.TestCase):

    def setUp(self):
        self.jungle = Jungle()

    def tearDown(self) -> None:
        self.jungle.animals.clear()

    def test__should_implement_all_abstract_methods(self):
        error_was_raised = False
        try:
            Herbivorous(100, 100)
        except TypeError:
            error_was_raised = True
        self.assertFalse(error_was_raised)

    def test_herbivorous_should_restore_power_after_eat(self):
        elephant = Herbivorous(100, 70)
        self.jungle.add_animal(elephant)
        elephant.current_power = 50
        elephant.eat(self.jungle)
        self.assertEqual(elephant.current_power, 90)

    def test_current_power_should_not_be_over_max(self):
        elephant = Herbivorous(power=100, speed=70)
        self.jungle.add_animal(elephant)
        elephant.eat(self.jungle)
        self.assertEqual(elephant.current_power, elephant.max_power)

    def test_animal_should_die_if_power_equal_0(self):
        elephant = Herbivorous(power=100, speed=70)
        self.jungle.add_animal(elephant)
        self.assertTrue(self.jungle.animals)
        elephant.current_power = 0
        elephant.eat(self.jungle)
        self.assertFalse(self.jungle.animals)


class TestPredator(unittest.TestCase):

    def setUp(self):
        self.jungle = Jungle()

    def tearDown(self) -> None:
        self.jungle.animals.clear()

    def test__should_implement_all_abstract_methods(self):
        error_was_raised = False
        try:
            Predator(100, 100)
        except TypeError:
            error_was_raised = True
        self.assertFalse(error_was_raised)

    def test_animal_should_die_if_power_equal_0(self):
        tiger = Predator(power=100, speed=70)
        self.jungle.add_animal(tiger)
        self.assertTrue(self.jungle.animals)
        tiger.current_power = 0
        tiger.eat(self.jungle)
        self.assertFalse(self.jungle.animals)

    def test_predator_catch_himself(self):
        tiger = Predator(power=100, speed=70)
        self.jungle.add_animal(tiger)

        tiger.eat(self.jungle)
        self.assertEqual(tiger.current_power, 70)

    def test_predator_try_to_hunt_someone_quicker(self):
        tiger = Predator(power=100, speed=70)
        horse = Herbivorous(power=100, speed=100)
        self.jungle.add_animal(horse)

        tiger.eat(self.jungle)
        self.assertEqual(tiger.current_power, 70)
        self.assertEqual(horse.current_power, 70)

    def test_predator_try_to_hunt_someone_stronger(self):
        dog = Predator(power=10, speed=70)
        elephant = Herbivorous(power=100, speed=40)
        self.jungle.add_animal(elephant)

        dog.eat(self.jungle)
        self.assertEqual(dog.current_power, 7)
        self.assertEqual(elephant.current_power, 70)


class TestJungle(unittest.TestCase):

    def test_add_animal(self):
        jungle = Jungle()
        dog = Predator(power=10, speed=70)

        jungle.add_animal(dog)
        self.assertDictEqual(jungle.animals, {dog.id: dog})

    def test_remove_animal(self):
        jungle = Jungle()
        dog = Predator(power=10, speed=70)

        jungle.add_animal(dog)
        self.assertDictEqual(jungle.animals, {dog.id: dog})

        jungle.remove_animal(dog)
        self.assertDictEqual(jungle.animals, {})

    def test_jungle_is_iterable(self):
        jungle = Jungle()
        animals = [Predator(power=10, speed=70), Predator(power=5, speed=40)]
        for animal in animals:
            jungle.add_animal(animal)

        try:
            animals_from_jungle = [a for a in jungle]
            self.assertEqual(animals, animals_from_jungle)
        except TypeError:
            self.assertTrue(False, "Jungle is not iterable")
