import unittest
from zoo import Zoo
from animal import Animal
import copy


class TestZoo(unittest.TestCase):

    def setUp(self):
        self.zoo = Zoo(10, 1000)
        self.tiger = Animal('Tiger', 2, 'Gosho', 'Male', 20)
        self.zoo.accommodate(self.tiger)

    def tearDown(self):
        Zoo.animals = []
        Animal.NAMES = {}

    def test_init(self):
        self.assertEqual(self.zoo.capacity, 10)
        self.assertEqual(self.zoo.budget, 1000)
        self.assertEqual(self.zoo.animals, [self.tiger])

    def test_accommodate(self):
        self.assertIn(self.tiger, self.zoo.animals)

    def test_move_to_habitat(self):
        before = self.zoo.animals
        after = copy.deepcopy(self.zoo.animals)
        self.zoo.accommodate(self.tiger)
        self.zoo.move_to_habitat("Tiger", "Gosho")
        after = [x for x in self.zoo.animals if x.name !=
                 "Gosho" and x.species != "Tiger"]
        self.assertEqual(len(before), len(after) + 1)

    def test_interval_in_days(self):
        result = self.zoo.interval_in_days("days")
        self.assertEqual(result, 1)

    def test_interval_in_months(self):
        result = self.zoo.interval_in_days("months")
        self.assertEqual(result, 30)

    def test_interval_in_weeks(self):
        result = self.zoo.interval_in_days("weeks")
        self.assertEqual(result, 7)

    def test_interval_in_years(self):
        result = self.zoo.interval_in_days("years")
        self.assertEqual(result, 365)

    def test_calc_daily_incomes(self):
        rabbit = Animal('Rabbit', 2, 'Pesho', 'Female', 25)
        self.zoo.accommodate(rabbit)
        self.zoo.calculate_daily_income()
        self.assertEqual(self.zoo.budget, 1120)

if __name__ == "__main__":
    unittest.main()
