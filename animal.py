import json
from random import random


def get_database(db):
    with open(db, "r") as db_file:
        db_data = json.load(db_file)
    return db_data


class Animal:
    DEFAULT_NAME = "Unknown"
    NAMES = {}
    DATABASE = get_database("database.json")

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        if species not in Animal.NAMES:
            Animal.NAMES[species] = []
        self.age = age
        self.gender = gender
        self.weight = weight
        self.is_alive = True

        if name not in Animal.NAMES[self.species]:
            Animal.NAMES[self.species].append(name)
            self.name = name
        else:
            Animal.NAMES[self.species].append(Animal.DEFAULT_NAME)
            self.name = Animal.DEFAULT_NAME

        for species_info in Animal.DATABASE:
            if species_info['Species'] == self.species:
                self.species_info = species_info

        if self.gender == 'Female':
            self.days_till_reproduce = 0
            self.in_gestation = False
            self.gestation = self.species_info['gestation'] * 30

    def grow(self):
        self.age += 1
        grow_ratio = self.species_info['weight/age']
        self.weight += grow_ratio / 30
        average_weight = self.species_info['average_weight']
        if self.weight > average_weight:
            self.weight = average_weight
        if self.gender == 'Female':
            self.days_till_reproduce -= 1
            if self.days_till_reproduce < 0:
                self.days_till_reproduce = 0
            if self.in_gestation:
                self.gestation -= 1

    def eating_price(self):
        if self.species_info['food_type'] == 'carnivore':
            money_per_kilo = 4
        else:
            money_per_kilo = 2
        food_weight_ratio = self.species_info['food/weight']
        kilos_eaten = food_weight_ratio * self.weight
        return money_per_kilo * kilos_eaten

    def is_dead(self):
        if not self.is_alive:
            return True
        life_expectancy = self.species_info['life_expectancy']
        chance_of_dying = self.age / life_expectancy
        roll = random()
        result = roll <= chance_of_dying
        if result is True:
            self.is_alive = False
        return result
