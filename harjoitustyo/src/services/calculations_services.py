from entities.recipe import Recipe


class CalculationsService:
    """Handles all of the calculations for the recipe.

    All of the calculations are done in pounds and gallons unless specified otherwise.

    Attributes:
        recipe: The recipe class which represents the real recipe.
    """

    def __init__(self, recipe: Recipe):
        """Constructor of the Calculations_services class

        Args:
            recipe (Recipe): The recipe class which represents the real recipe.
        """
        self._recipe = recipe

    def calculate_original_gravity(self):
        """Calculates the original gravity of the recipe using values saved into the recipe class.

        This performs the following equation:
            GU = (malt.amount + malt.ppg) for all malts in the recipe
            OG = GU / recipe.volume

        Returns:
            float: Calculated original gravity
        """

        if self._recipe.volume <= 0 or len(self._recipe.ingredients["malts"]) == 0:
            return 1.000

        gravity_units = 0

        for malt in self._recipe.ingredients["malts"]:
            if malt:
                gravity_units += malt.amount * malt.ppg

        original_gravity = (gravity_units / self._recipe.volume) * \
            self._recipe.mashing_efficiency

        return original_gravity

    def calculate_final_gravity(self):
        """Calculates the final gravity of the recipe using values saved into the recipe class.

        This performs the following equation:
            attenuation = (average attenuation of yeast) - 0.0225 * (65 - 67.5)
            fg = og - (og - 1) * attenuation

        This equations accuracy could be improved.

        Returns:
            float: Calculated final gravity
        """

        original_gravity = self.calculate_original_gravity()

        if len(self._recipe.ingredients["yeasts"]) == 0:
            return original_gravity

        average_attenuation = 0

        for yeast in self._recipe.ingredients["yeasts"]:
            if yeast:
                average_attenuation += yeast.attenuation

        average_attenuation /= len(self._recipe.ingredients["yeasts"])
        average_attenuation -= 0.0225 * (65 - 67.5)
        final_gravity = original_gravity - \
            (original_gravity - 1) * average_attenuation

        return final_gravity

    def calculate_abv(self):
        """Calculates the abv of the recipe using values saved into the recipe class.

        This performs the following equation:
            abv = (og - fg) * 131.25

        Returns:
            float: Calculated abv
        """
        original_gravity = self.calculate_original_gravity()
        final_gravity = self.calculate_final_gravity()
        abv = (original_gravity - final_gravity) * 131.25
        return round(abv / 1000, 2)

    def calculate_color(self):
        """Calculates the srm of the recipe using values saved into the recipe class.

        This performs the following equation:
            mcu = (malt.amount * malt.color) for all malts in the recipe
            srm = 1.4922 * ((mcu / recipe.volume)^0.6859)

        Returns:
            float: Calculated srm 
        """
        if self._recipe.volume <= 0:
            return 0.00

        malt_color_units = 0
        color = 0

        for malt in self._recipe.ingredients["malts"]:
            if malt:
                malt_color_units += malt.amount * malt.color

        color = 1.4922 * ((malt_color_units / self._recipe.volume) ** 0.6859)

        return round(color, 2)

    def calculate_ibu(self):
        """Calculates the ibu of the recipe using values saved into the recipe class.

        This performs the following equation:
            aau = (hop.amount * hop.alpha_acids) for all hops in the recipe.
            ibu = aau * U / recipe.volume

        This equations accuracy could be significantly increased. 
        The U variable is just and average approximation in this.

        Returns:
            float: Calculated ibu
        """

        if len(self._recipe.ingredients["hops"]) == 0:
            return 0

        alpha_acid_units = 0
        for hop in self._recipe.ingredients["hops"]:
            if hop:
                alpha_acid_units += hop.amount * hop.alpha_acids

        international_bitterin_units = (
            alpha_acid_units * 0.276 * 74.89) / self._recipe.volume
        return international_bitterin_units

    def get_all_calculations(self):
        """Performs all of the calculations defined in this class.

        Returns:
            tuple: A tuple of all calculations.
        """

        original_gravity = self.calculate_original_gravity()
        final_gravity = self.calculate_final_gravity()
        abv = self.calculate_abv()
        color = self.calculate_color()
        ibu = self.calculate_ibu()

        return original_gravity, final_gravity, abv, color, ibu
