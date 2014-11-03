class Zoo:

    INCOME_PER_ANIMAL = 60

    def __init__(self, capacity, budget):
        self.animals = []
        self.capacity = capacity
        self.budget = budget

    def accommodate(self, animal):
        self.animals.append(animal)

    def calculate_daily_income(self):
        return len(self.animals) * Zoo.INCOME_PER_ANIMAL

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
