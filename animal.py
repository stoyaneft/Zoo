import json
from random import random


@staticmethod
def get_database(db):
    with open(db, "r") as db_file:
        db_data = json.load(db_file)
    return db_data


class Animal:
    DEFAULT_NAME = "Unknown"
    NAMES = []
    DATABASE = get_database("database.json")

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.gender = gender
        self.weight = weight
        self.name = name
        for species_info in Animal.DATABASE:
            if species_info['species'] == self.species:
                self.species_info = Animal.DATABASE[self.species]
        if self.gender == 'Female':
            self.days_till_reproduce = 0
            self.in_gestation = False
            self.gestation = self.species_info['gestation'] * 30
        # else:
        #     raise Exception("NameExists")

    def grow(self):
        self.age += 1
        grow_ratio = self.species_info['weight/age']
        self.weight += grow_ratio / 30
        average_weight = self.species_info['average_weight']
        if self.weight > average_weight:
            self.weight = average_weight
        if self.gender == 'Female':
            self.day_till_reproduce -= 1
            if self.day_till_reproduce < 0:
                self.day_till_reproduce = 0
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
        life_expectancy = self.species_info['life_expectancy']
        chance_of_dying = self.age / life_expectancy
        roll = random()
        return roll <= chance_of_dying
