import unittest
from services.calculations_services import CalculationsService
from entities.recipe import Recipe
from entities.all_ingredients import Malt, Hop, Yeast

class TestCalculationsService(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe()
        self.recipe.malts = [Malt("test malt 1", 37.0, 10), Malt("test malt 2", 12.4, 5)]
        self.recipe.volume = 5
        self.recipe.malts[0].amount = 5
        self.recipe.malts[1].amount = 2
        self.calculator = CalculationsService(self.recipe)
    
    def test_original_gravity_calculations(self):
        og = self.calculator.calculate_original_gravity()

        self.assertAlmostEqual(og, 29.372)

    def test_original_gravity_calculations_with_no_malts(self):
        self.recipe.malts = []
        og = self.calculator.calculate_original_gravity()

        self.assertAlmostEqual(og, 0.0)
    
    def test_color_calculations(self):
        srm = self.calculator.calculate_color()

        self.assertAlmostEqual(srm, 8.204222922)
    
    def test_color_calculations_with_no_malts(self):
        self.recipe.malts = []
        og = self.calculator.calculate_color()

        self.assertAlmostEqual(og, 0.0)