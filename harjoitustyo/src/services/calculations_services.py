from entities.recipe import Recipe
from repositories.malts_repository import MaltsRepository

class CalculationsService:
    
    def __init__(self, recipe: Recipe):
        self._recipe = recipe

    # OG kaava: OG = (MALTAAN MÄÄRÄ + MALTAAN PPG) / ERÄN KOKO
    # Yksiköt: pound ja gallon
    def calculate_original_gravity(self):
        gravity_units = 0

        for malt in self._recipe.malts:
            gravity_units += malt.amount * malt.ppg

        original_gravity = (gravity_units / self._recipe.volume) * self._recipe.mashing_efficiency
        return original_gravity

    def calculate_final_gravity(self):
        pass

    def calculate_abv(self):
        pass

    # MCU = (MALTAIDEN MÄÄRÄ * MALTAAN VÄRIASTE) / MÄÄRÄ
    # SRM VÄRI = 1.4922 * (MCU ^ 0.6859)
    def calculate_color(self):
        malt_color_units = 0
        color = 0

        for malt in self._recipe.malts:
            malt_color_units += malt.amount * malt.color
        
        color = 1.4922 * ((malt_color_units / self._recipe.volume) ** 0.6859)
        return color