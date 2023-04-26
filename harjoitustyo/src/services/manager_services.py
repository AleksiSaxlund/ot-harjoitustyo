from repositories.ingredients_repository import MaltsRepository, HopsRepository, YeastsRepository
from services.calculations_services import CalculationsService


class ManagerServices():
    """Class which is responsible for software logic and communicating between ui and other parts.

    Attributes:
        recipe: The recipe class which represents the real recipe.
        malts: MaltsRepository class which communicates with a database.
        hops: HopsRepository class which communicates with the database.
        yeasts: YeastsRepository class which communicates with the database.
        calculator: Calculations_services class which handles all of the calculations.
    """

    def __init__(self, recipe):
        """Constructor of the class which creates the manager for the app.

        Args:
            recipe: The recipe class which represents the real recipe.
        """

        self.malts = MaltsRepository()
        self.hops = HopsRepository()
        self.yeasts = YeastsRepository()
        self.recipe = recipe
        self.calculator = CalculationsService(self.recipe)

    def ingredient_added(self, ingredient, ingredient_type):
        """Handles the adding of new ingredients to the recipe.

        Args:
            Ingredient (Malt, Hop, Yeast): Corresponding class object to the ingredient type.
            Ingredient_type (str): Is one of the following: "malts", "hops", "yeasts".
                                Acts as a dictionary key for the recipe.

        Returns:
            list: A list of all updated and formatted calculations for the ui.
        """

        if ingredient_type in ["malts", "hops", "yeasts"]:
            self.recipe.ingredients[ingredient_type].append(ingredient)

        results = self.update_calculations()
        return results

    def ingredient_removed(self, index, ingredient_type):
        """Handles the removels of ingredients from the recipe.

        Args:
            index (int): Index of the ingredient which will be removed.
            ingredient_type (str): Is one of the following: "malts", "hops", "yeasts".
                                Acts as a dictionary key for the recipe.

        Returns:
            list: A list of all updated and formatted calculations for the ui.
        """

        if len(self.recipe.ingredients[ingredient_type]) > 0:
            if ingredient_type in ["malts", "hops", "yeasts"]:
                self.recipe.ingredients[ingredient_type].pop(index)

        results = self.update_calculations()
        return results

    def ingredient_amount_changed(self, amount, index, ingredient_type):
        """Handles the changes in ingredient amounts.

        Args:
            amount (float): New amount of the ingredient
            index (itn): Index of the ingredient which will be affected.
            ingredient_type (str): Is one of the following: "malts", "hops", "yeasts".
                                Acts as a dictionary key for the recipe.

        Returns:
            list: A list of all updated and formatted calculations for the ui.
        """

        if len(self.recipe.ingredients[ingredient_type]) > index:
            if ingredient_type in ["malts", "hops"]:
                self.recipe.ingredients[ingredient_type][index].amount = amount

        results = self.update_calculations()
        return results

    def volume_changed(self, volume):
        """Handles the changes in the recipe volume.

        Args:
            volume (float): New volume of the recipe.

        Returns:
            list: A list of all updated and formatted calculations for the ui.
        """

        self.recipe.volume = volume
        results = self.update_calculations()
        return results

    def get_all_malts(self):
        """Gets all of the malts from the repository.

        Returns:
            list: A list of all malts
        """

        all_malts = self.malts.get_all_malts()
        return all_malts

    def get_all_hops(self):
        """Gets all of the hops from the repository.

        Returns:
            list: A list of all hops
        """

        all_hops = self.hops.get_all_hops()
        return all_hops

    def get_all_yeasts(self):
        """Gets all of the yeasts from the repository.

        Returns:
            list: A list of all yeasts
        """

        all_yeasts = self.yeasts.get_all_yeasts()
        return all_yeasts

    def update_calculations(self):
        """Gets all of the calculations from calculations_services
            and saves the results into the recipe.

        This method is called by several other in this class methods.

        Returns:
            list: A list of all updated and formatted calculations for the ui.
        """

        original_gravity, final_gravity, abv, color, ibu = self.calculator.get_all_calculations()
        self.recipe.original_gravity = original_gravity
        self.recipe.final_gravity = final_gravity
        self.recipe.abv = abv
        self.recipe.color = color
        self.recipe.ibu = ibu

        results = self.format_calculation_results()
        return results

    def format_calculation_results(self):
        """Formats all of the calculations from the recipe for the ui.

        This method is called by update_calculations method.

        Returns:
            list: A list of all updated and formatted calculations for the ui.
        """
        values = []
        values.append(f"{round(self.recipe.original_gravity / 1000 + 1, 3)}")
        values.append(f"{round(self.recipe.final_gravity / 1000 + 1, 3)}")
        values.append(f"{round(self.recipe.abv, 2)}%")
        values.append(f"{int(self.recipe.color)}")
        values.append(f"{int(self.recipe.ibu)}")

        return values
