from entities.recipe import Recipe


class CalculationsService:
    def __init__(self, recipe: Recipe):
        self._recipe = recipe

    # OG kaava: OG = (MALTAAN MÄÄRÄ + MALTAAN PPG) / ERÄN KOKO
    # Yksiköt: pound ja gallon
    def calculate_original_gravity(self):
        if self._recipe.volume <= 0:
            return 1.000

        gravity_units = 0

        for malt in self._recipe.ingredients["malts"]:
            gravity_units += malt.amount * malt.ppg

        original_gravity = (gravity_units / self._recipe.volume) * \
            self._recipe.mashing_efficiency
        return original_gravity

    # FINAL GRAVITY = OG - (OG - 1) * ATTENUATION
    # ATTENUATION = ATTENUATION - 0.0225 * (X - 67.5)
    def calculate_final_gravity(self):
        if len(self._recipe.ingredients["yeasts"]) == 0:
            return self._recipe.original_gravity

        original_gravity = self._recipe.original_gravity
        average_attenuation = 0

        for yeast in self._recipe.ingredients["yeasts"]:
            average_attenuation += yeast.attenuation

        average_attenuation /= len(self._recipe.ingredients["yeasts"])
        average_attenuation -= 0.0225 * (65 - 67.5)
        final_gravity = original_gravity - (original_gravity - 1) * average_attenuation
        return final_gravity

    #ABV KAAVA = (OG - FG) * 131.25
    def calculate_abv(self):
        original_gravity = self._recipe.original_gravity
        final_gravity = self._recipe.final_gravity
        abv = (original_gravity - final_gravity) * 131.25
        return round(abv / 1000, 2)

    # MCU = (MALTAIDEN MÄÄRÄ * MALTAAN VÄRIASTE) / MÄÄRÄ
    # SRM VÄRI = 1.4922 * (MCU ^ 0.6859)
    def calculate_color(self):
        if self._recipe.volume <= 0:
            return 0.00

        malt_color_units = 0
        color = 0

        for malt in self._recipe.ingredients["malts"]:
            malt_color_units += malt.amount * malt.color

        color = 1.4922 * ((malt_color_units / self._recipe.volume) ** 0.6859)
        return round(color, 2)
