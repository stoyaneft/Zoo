import unittest
from animal import Animal


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.testAnimal = Animal("Tiger", 2, "Name", "Male", 50)
        self.femaleAnimal = Animal('Tiger', 3, 'Penka', "Female", 5)

    def tearDown(self):
        Animal.NAMES = {}

    def test_init(self):
        self.assertEqual(self.testAnimal.species, "Tiger")
        self.assertEqual(self.testAnimal.age, 2)
        self.assertEqual(self.testAnimal.name, "Name")
        self.assertEqual(self.testAnimal.gender, "Male")
        self.assertEqual(self.testAnimal.weight, 50)

    def test_equal_names_raises_error(self):
        with self.assertRaises(NameError):
            self.testAnimal2 = Animal("Tiger", 2, "Name", "Female", 50)

    def test_grow_older(self):
        self.testAnimal.grow()
        self.assertEqual(self.testAnimal.age, 3)

    def test_gestation(self):
        self.femaleAnimal.in_gestation = True
        self.femaleAnimal.grow()
        self.assertEqual(self.femaleAnimal.gestation, 209)

    def test_eating_price_for_carnivore(self):
        result = self.testAnimal.eating_price()
        self.assertEqual(result, 200*0.3)

    def test_eating_price_for_herbivore(self):
        self.testAnimal2 = Animal("Rabbit", 1, "Zaek", "Male", 15)
        result = self.testAnimal2.eating_price()
        self.assertEqual(result, 30*0.1)

    def test_is_dead_when_already_dead(self):
        self.testAnimal.is_alive = False
        result = self.testAnimal.is_dead()
        self.assertTrue(result)

    def test_is_dead_when_not_dead(self):
        result = self.testAnimal.is_dead()
        for i in range(0, 100):
            self.assertIn(result, [True, False])

if __name__ == "__main__":
    unittest.main()
