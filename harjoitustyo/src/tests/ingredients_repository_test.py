import unittest
from repositories.ingredients_repository import MaltsRepository, HopsRepository, YeastsRepository
from database_connections import get_malts_connection, get_hops_connection, get_yeasts_connection
from entities.all_ingredients import Malt, Hop, Yeast


class TestCalculationsService(unittest.TestCase):
    def setUp(self):
        self.malts = MaltsRepository()
        self.hops = HopsRepository()
        self.yeasts = YeastsRepository()

    def test_connections(self):
        malts = get_malts_connection()
        hops = get_hops_connection()
        yeasts = get_yeasts_connection()

        self.assertEqual((malts, hops, yeasts),
                         (self.malts._connection, self.hops._connection, self.yeasts._connection))

    def test_get_all_yeasts(self):
        yeasts = []
        for yeast in self.yeasts._yeasts:
            yeasts.append(Yeast(yeast[0], float(yeast[1]), yeast[2]))

        test_yeasts = self.yeasts.get_all_yeasts()

        for i in range(len(yeasts)):
            self.assertEqual((test_yeasts[i].name, test_yeasts[i].attenuation, test_yeasts[i].temperature_range),
                             (yeasts[i].name, yeasts[i].attenuation, yeasts[i].temperature_range))
