class Animal:
    DEFAULT_NAME = "Unknown"
    NAMES = []

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
        self.weight += weight
        self.age += age

    def eat(self):
        return "NomNomNom"

    def die(self):
        self.is_dead = True
        return "I died."
