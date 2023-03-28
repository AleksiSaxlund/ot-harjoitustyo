from entities.recipe import Recipe
from entities.hop import Hop
from entities.malt import Malt
from entities.yeast import Yeast

class CalculationsService:
    
    def __init__(self, recipe: Recipe):
        self._recipe = recipe

    def calculate_original_gravity(self):
        pass

    def calculate_final_gravity(self):
        pass

    def calculate_abv(self):
        pass

    def calculate_color(self):
        pass