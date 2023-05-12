import unittest
from services.manager_services import ManagerServices
from entities.recipe import Recipe
from entities.all_ingredients import Malt, Hop, Yeast


class TestCalculationsService(unittest.TestCase):
    def setUp(self):
        self.recipe = Recipe()
        self.manager = ManagerServices(self.recipe)

    def test_yeast_added_to_recipe(self):
        yeast = Yeast("test yeast", 15.2, "12-45")

        self.manager.ingredient_added(yeast, "yeasts", 0)

        self.assertEqual(self.recipe.ingredients["yeasts"][0], yeast)
