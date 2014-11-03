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
