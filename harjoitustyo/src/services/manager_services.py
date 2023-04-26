from repositories.ingredients_repository import MaltsRepository, HopsRepository, YeastsRepository
from services.calculations_services import CalculationsService


class ManagerServices():
    def __init__(self, recipe):
        self.malts = MaltsRepository()
        self.hops = HopsRepository()
        self.yeasts = YeastsRepository()
        self.recipe = recipe
        self.calculator = CalculationsService(self.recipe)

    def ingredient_added(self, ingredient, ingredient_type):
        if ingredient_type in ["malts", "hops", "yeasts"]:
            self.recipe.ingredients[ingredient_type].append(ingredient)

        results = self.update_calculations()
        return results

    def ingredient_removed(self, index, ingredient_type):
        if len(self.recipe.ingredients[ingredient_type]) > 0:
            if ingredient_type in ["malts", "hops", "yeasts"]:
                self.recipe.ingredients[ingredient_type].pop(index)

        results = self.update_calculations()
        return results

    def ingredient_amount_changed(self, amount, index, ingredient_type):
        if len(self.recipe.ingredients[ingredient_type]) > index:
            if ingredient_type in ["malts", "hops"]:
                self.recipe.ingredients[ingredient_type][index].amount = amount

        results = self.update_calculations()
        return results
    
    def volume_changed(self, volume):
        self.recipe.volume = volume
        results = self.update_calculations()
        return results

    def get_all_malts(self):
        all_malts = self.malts.get_all_malts()
        return all_malts

    def get_all_hops(self):
        all_hops = self.hops.get_all_hops()
        return all_hops

    def get_all_yeasts(self):
        all_yeasts = self.yeasts.get_all_yeasts()
        return all_yeasts

    def update_calculations(self):
        original_gravity, final_gravity, abv, color, ibu = self.calculator.get_all_calculations()
        self.recipe.original_gravity = original_gravity
        self.recipe.final_gravity = final_gravity
        self.recipe.abv = abv
        self.recipe.color = color
        self.recipe.ibu = ibu

        results = self.format_calculation_results()
        return results

    def format_calculation_results(self):
        values = []
        values.append(f"{round(self.recipe.original_gravity / 1000 + 1, 3)}")
        values.append(f"{round(self.recipe.final_gravity / 1000 + 1, 3)}")
        values.append(f"{round(self.recipe.abv, 2)}%")
        values.append(f"{int(self.recipe.color)}")
        values.append(f"{int(self.recipe.ibu)}")

        return values
