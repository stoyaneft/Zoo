from random import choice
from collections import defaultdict

from animal import Animal


class Zoo:

    INCOME_PER_ANIMAL = 60
    NEWBORNS = 0

    def __init__(self, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget
        self.database = self.get_database("database.json")

    def accommodate(self, animal):
        self.animals.append(animal)

    def calculate_daily_income(self):
        self.budget += len(self.animals) * Zoo.INCOME_PER_ANIMAL

    def check_for_pregnancy(self):
        species = defaultdict(int)
        for animal in self.animals:
            species[animal.species].append(animal)
        for s in species:
            males = filter(lambda x: x.gender == 'Male', species[s])
            reproducable_females = filter(
                lambda x: x.gender == 'Female' and x.days_till_reproduce == 0,
                species[s])
            if males and reproducable_females:
                reproducable_females[0].in_gestation = True

    def is_animal_born(self):
        self.check_for_pregnancy()
        females = filter(lambda x: x.gender == 'Female', self.animals)
        for female in females:
            if female.gestation == 0:
                name = 'newborn' + str(Zoo.NEWBORNS)
                gender = choice('MF')
                if gender == 'M':
                    gender = 'Male'
                else:
                    gender = 'Female'
                newborn_weight = female.species_info['newborn']
                newborn = Animal(
                    female.species, 0, name, gender, newborn_weight)
                self.animals.append(newborn)
                female.gestation = female.species_info['gestation'] * 30
                female.in_gestation = False
                return True
        return False

    def is_dead(self, species, name):
        for animal in self. animals:
            if (animal.species == species and
                    animal.name == name and
                    animal.is_dead is True):
                return True
        return False

    def see_animals(self):
        for animal in self.animals:
            print "{} : {}, {}, {}".format(animal.name, animal.species,
                                           animal.age, animal.weight)

    def move_to_habitat(self, species, name):
        for animal in self.animals:
            if (animal.species == species and
                    animal.name == name and
                    animal.is_dead is False):
                self.animals.remove(animal)

    def simulate(self, days, period):
        for i in period:
            self.see_animals()
            self.calculate_daily_income()
            needed_money = 0
            for animal in self.animals:
                animal.grow()
                if animal.is_dead():
                    print (
                        "{} {} has died".format(animal.species, animal.name))
                if self.is_animal_born():
                    print('New animal has been born')
                needed_money += animal.eating_price()
            if needed_money > self.budget:
                print('Not enough budget to feed all animals')
