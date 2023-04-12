import unittest
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt, Hop, Yeast


class TestCalculationsService(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe()
        self.recipe.ingredients["malts"] = [
            Malt("test malt 1", 37.0, 10), Malt("test malt 2", 12.4, 5)]
        self.recipe.ingredients["yeasts"] = [Yeast("test yeast", 0.75, "12-50")]
        self.recipe.volume = 5
        self.recipe.ingredients["malts"][0].amount = 5
        self.recipe.ingredients["malts"][1].amount = 2
        self.calculator = CalculationsService(self.recipe)

    def test_original_gravity_calculations(self):
        og = self.calculator.calculate_original_gravity()

        self.assertAlmostEqual(og, 1.029)

    def test_original_gravity_calculations_with_no_malts(self):
        self.recipe.ingredients["malts"] = []
        og = self.calculator.calculate_original_gravity()

        self.assertAlmostEqual(og, 1.000)

    def test_color_calculations(self):
        srm = self.calculator.calculate_color()

        self.assertAlmostEqual(srm, 8.20)

    def test_color_calculations_with_no_malts(self):
        self.recipe.ingredients["malts"] = []
        srm = self.calculator.calculate_color()

        self.assertAlmostEqual(srm, 0.00)

    def test_final_gravity_calculations(self):
        self.recipe.original_gravity = 1.029
        fg = self.calculator.calculate_final_gravity()

        self.assertAlmostEqual(fg, 1.006)

    def test_final_gravity_calculation_with_no_malts(self):
        self.recipe.original_gravity = 1.000
        fg = self.calculator.calculate_final_gravity()

        self.assertAlmostEqual(fg, 1.000)

    def test_final_gravity_calculation_with_no_yeasts(self):
        self.recipe.original_gravity = 1.0029
        self.recipe.ingredients["yeasts"] = []
        fg = self.calculator.calculate_final_gravity()

        self.assertAlmostEqual(fg, 1.0029)

    def test_abv_calculations(self):
        self.recipe.original_gravity = 29.372
        self.recipe.final_gravity = 6.497075
        abv = self.calculator.calculate_abv()

        self.assertAlmostEqual(round(abv, 2), 3.0)
