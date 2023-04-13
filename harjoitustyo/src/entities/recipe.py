
class Recipe:
    def __init__(self):
        self.ingredients = {"malts": [], "hops": [], "yeasts": []}
        self.original_gravity = 1.000
        self.final_gravity = 1.000
        self.abv = 0
        self.ibu = 0
        self.volume = 5
        self.mashing_efficiency = 0.70
        self.boiltime = 0
