import unittest
from animal import Animal


class TestAnimal(unittest.TestCase):
    def setUp(self):
        self.testAnimal = Animal("Species", 2, "Name", "Male", 50)

    def test_init(self):
        self.assertEqual(self.testAnimal.species, "Species")
        self.assertEqual(self.testAnimal.age, 2)
        self.assertEqual(self.testAnimal.name, "Name")
        self.assertEqual(self.testAnimal.gender, "Male")
        self.assertEqual(self.testAnimal.weight, 50)

    # def test_equal_names(self):
    #     print (Animal.NAMES)
    #     with self.assertRaises((Exception("NameExists"))):
    #         self.testAnimal2 = Animal("Species", 3, "Name", "Male", 50)

    def test_grow(self):
        self.testAnimal.grow(10, 1)
        self.assertEqual(self.testAnimal.weight, 60)
        self.assertEqual(self.testAnimal.age, 3)

    def test_eat(self):
        result = self.testAnimal.eat()
        self.assertEqual(result, "NomNomNom")

    def test_die(self):
        result = self.testAnimal.die()
        self.assertEqual(result, "I died.")

if __name__ == "__main__":
    unittest.main()
