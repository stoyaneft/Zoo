from animal import Animal


class Zoo:

    def __init__(self, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    def produce_animals(self, gestation, species):
        toReproduce = {"Male": [], "Female": []}
        for animal in self.animals:
            if animal.species == species:
                toReproduce[animal.gender].append(animal)
        for item in toReproduce:
            if len(toReproduce[item]) == 0:
                return False
            else:
                return True

    def is_dead(self, species, name):
        for animal in self. animals:
            if (animal.species == species and
                    animal.name == name and
                    animal.is_dead is True):
                return True
        return False







# accomodate
# calculate incomes
# calculate outcomes
# is dead
