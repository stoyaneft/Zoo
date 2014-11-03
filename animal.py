import json


@staticmethod
def get_database(db, ):
    with open(db, "r") as db_file:
        db_data = json.load(db_file)
    return db_data


class Animal:
    DEFAULT_NAME = "Unknown"
    NAMES = []
    database = get_database("database.json")

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.gender = gender
        self.weight = weight
        self.name = name
        self.is_dead = False
        # else:
        #     raise Exception("NameExists")

    def grow(self, weight, age):
        life_expectancy = Animal.database[self.species]["life_expectancy"]
        aver_weight = Animal.database[self.species]["average_weight"]
        if self.age + age > life_expectancy:
            self.age = life_expectancy
        if self.weight + weight > aver_weight:
            self.weight = aver_weight

        self.weight += weight
        self.age += age

    def eat(self):
        return "NomNomNom"

    def die(self):
        self.is_dead = True
        return "I died."
