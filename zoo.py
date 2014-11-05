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

    def accommodate(self, animal):
        self.animals.append(animal)
        print('Animal accommodated successfully')

    def calculate_daily_income(self):
        self.budget += len(self.animals) * Zoo.INCOME_PER_ANIMAL

    def check_for_pregnancy(self):
        species = defaultdict(list)
        for animal in self.animals:
            species[animal.species].append(animal)
        for s in species:
            males = filter(lambda x: x.gender == 'Male', species[s])
            reproducable_females = list(filter(
                lambda x: x.gender == 'Female' and x.days_till_reproduce == 0,
                species[s]))
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
                newborn_weight = female.species_info['Newborn']
                newborn = Animal(
                    female.species, 0, name, gender, newborn_weight)
                self.animals.append(newborn)
                female.gestation = female.species_info['gestation'] * 30
                female.in_gestation = False
                return newborn
        return None

    def see_animals(self):
        for animal in self.animals:
            print ("{} : {}, {}, {}".format(animal.name, animal.species,
                                            animal.age, animal.weight))

    def move_to_habitat(self, species, name):
        for animal in self.animals:
            if (animal.species == species and
                    animal.name == name and
                    animal.is_alive):
                self.animals.remove(animal)

    @staticmethod
    def interval_in_days(interval):
        if interval == 'days':
            days_in_interval = 1
        elif interval == 'weeks':
            days_in_interval = 7
        elif interval == 'months':
            days_in_interval = 30
        else:
            days_in_interval = 365
        return days_in_interval

    def simulate_day(self, changes):
        self.calculate_daily_income()
        for animal in self.animals:
            animal.grow()
            animal.is_dead()
            if not animal.is_alive:
                changes['dead'].append(animal)
                self.animals.remove(animal)
            newborn = self.is_animal_born()
            if newborn is not None:
                changes['newborn'].append(newborn)
            changes['expenses'] += animal.eating_price()

    def simulate(self, interval, period):
        for i in range(period):
            self.see_animals()
            changes = {'dead': [], 'newborn': [], 'expenses': 0}
            for day in range(Zoo.interval_in_days(interval)):
                self.simulate_day(changes)
            for dead_animal in changes['dead']:
                print('{} {} has died.'.format(
                    dead_animal.species, dead_animal.name))
            if changes['expenses'] > self.budget:
                print ('Not enough budget to feed all animals.')
            for newborn in changes['newborn']:
                print('{} {} was born.'.format(newborn.species, newborn.name))
