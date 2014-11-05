import unittest
from zoo import Zoo
from animal import Animal
import copy


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo(10, 1000)
        self.tiger = Animal('Tiger', 2, 'Gosho', 'Male', 20)
        self.zoo.accommodate(self.tiger)

    def test_init(self):
        self.assertEqual(self.zoo.capacity, 10)
        self.assertEqual(self.zoo.budget, 1000)
        self.assertEqual(self.zoo.animals, [self.tiger])

    def test_accommodate(self):
        self.assertIn(self.tiger, self.zoo.animals)

    def test_calculate_daily_income(self):
        self.zoo.accommodate(self.tiger)
        self.assertEqual(self.zoo.budget, 60)

    def test_move_to_habitat(self):
        before = self.zoo.animals
        after = copy.deepcopy(self.zoo.animals)
        self.zoo.accommodate(self.tiger)
        self.zoo.move_to_habitat("Tiger", "Gosho")
        after = [x for x in self.zoo.animals if x.name !=
                 "Gosho" and x.species != "Tiger"]
        self.assertEqual(len(before), len(after) + 1)

    def test_simulate(self):
        pass

    def test_calc_daily_incomes(self):
        lion = Animal('Lion', 2, 'Pesho', 'Female', 25)
        self.zoo.accommodate(lion)
        self.assertEqual(self.zoo.calculate_daily_income(), 120)

if __name__ == "__main__":
    unittest.main()
