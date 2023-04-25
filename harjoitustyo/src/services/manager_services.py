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
        if ingredient_type == "malts":
            pass
        elif ingredient_type == "hops":
            pass
        elif ingredient_type == "yeasts":
            self.recipe.ingredients[ingredient_type].append(ingredient)

        results = self.update_calculations()
        return results

    def ingredient_removed(self, index, ingredient_type):
        if len(self.recipe.ingredients[ingredient_type]) > 0:
            if ingredient_type == "malts":
                pass
            elif ingredient_type == "hops":
                pass
            elif ingredient_type == "yeasts":
                self.recipe.ingredients[ingredient_type].pop(index)

        results = self.update_calculations()
        return results

    def ingredient_amount_changed(self):
        pass

    def get_all_malts(self):
        pass

    def get_all_hops(self):
        pass

    def get_all_yeasts(self):
        all_yeasts = self.yeasts.get_all_yeasts()
        return all_yeasts

    def volume_changed(self):
        pass

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
        values.append(f"{self.recipe.color}")
        values.append(f"{self.recipe.ibu}")

        return values
