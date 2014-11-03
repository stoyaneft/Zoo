class Animal:
    DEFAULT_NAME = "Unknown"
    NAMES = []

    def __init__(self, species, age, name, gender, weight):
        self.species = species
        self.age = age
        self.gender = gender
        self.weight = weight
        self.name = name
        # else:
        #     raise Exception("NameExists")

    def grow(self, weight, age):
        self.weight += weight
        self.age += age

    def eat(self):
        return "NomNomNom"

    def die(self):
        return "I died."
