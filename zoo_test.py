import unittest
from zoo import Zoo

from zoo import Zoo
from animal import Animal


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo(10, 1000)
        self.tiger = Animal('Tiger', 2, 'Gosho', 'Male', 20)
        self.zoo.accommodate(self.tiger)

    def test_accommodate(self):
        self.assertIn(self.tiger, self.zoo.animals)

    def test_calc_daily_incomes(self):
        lion = Animal('Lion', 2, 'Pesho', 'Female', 25)
        self.zoo.accommodate(lion)
        self.assertEqual(self.zoo.calculate_daily_income(), 120)

if __name__ == "__main__":
    unittest.main()
