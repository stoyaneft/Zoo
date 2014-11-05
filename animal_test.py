import unittest
from animal import Animal


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.testAnimal = Animal("Tiger", 2, "Name", "Male", 50)

    def test_init(self):
        self.assertEqual(self.testAnimal.species, "Tiger")
        self.assertEqual(self.testAnimal.age, 2)
        self.assertEqual(self.testAnimal.name, "Name")
        self.assertEqual(self.testAnimal.gender, "Male")
        self.assertEqual(self.testAnimal.weight, 50)

    def test_equal_names(self):
        self.testAnimal2 = Animal("Tiger", 2, "Name", "Female", 50)
        self.assertEqual(self.testAnimal.name, "Name")
        self.assertEqual(self.testAnimal2.name, "Unknown")

    def test_grow(self):
        self.testAnimal.grow()
        self.assertEqual(self.testAnimal.weight, 60)
        self.assertEqual(self.testAnimal.age, 3)

    def test_eating_price_for_carnivore(self):
        result = self.testAnimal.eating_price()
        self.assertEqual(result, 200*0.3)

    def test_eating_price_for_herbivore(self):
        self.testAnimal2 = ("Rabbit", 1, "Zaek", "Male", 15)
        result = self.eating_price()
        self.assertEqual(result, 30*0.1)

    def test_is_dead_when_already_dead(self):
        self.testAnimal.is_alive = False
        result = self.testAnimal.is_dead()
        self.assertTrue(result)

    def test_is_dead_when_not_dead(self):
        result = self.testAnimal.is_dead()
        for i in range(0, 100):
            self.asertIn(result, [True, False])

if __name__ == "__main__":
    unittest.main()
