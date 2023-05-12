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

    def test_get_all_malts(self):
        malts = self.malts.get_all_malts()

        expected_results = [('Abbey Malt', 33.0, 17), ('Acidulated Malt', 27.0, 3), (
            'Agave Nectar', 35.0, 2), ('Ale Malt', 37.4, 3), ('Ale Malt', 37.0, 3)]

        for i in range(len(expected_results)):
            self.assertEqual(
                (malts[i].name, malts[i].ppg, malts[i].color), expected_results[i])

    def test_get_all_hops(self):
        hops = self.hops.get_all_hops()

        expected_results = [('Admiral', 14.3), ('Ahtanum', 5.5),
                            ('Amarillo', 8.6), ('Ariana', 10.9), ('Aurora', 8.4)]

        for i in range(len(expected_results)):
            self.assertEqual(
                (hops[i].name, hops[i].alpha_acids), expected_results[i])

    def test_get_all_yeasts(self):
        yeasts = self.yeasts.get_all_yeasts()

        expected_results = [('Escarpment Labs - Brut Ale', 0.85, '57.0 - 72.0'), ('Omega Yeast Labs - Dried Lutra Kveik - OYL-071DRY', 0.785, '68.0 - 95.0'),
                            ('AEB - Fermo Brew Citrus', 0.75, '0.0 - 0.0'), ('Fermentum Mobile - FM12 Scottish Tartan', 0.77, '64.0 - 72.0'), ('Fermentum Mobile - FM20 White Wellingtons', 0.73, '66.0 - 75.0')]

        for i in range(len(expected_results)):
            self.assertEqual((yeasts[i].name, yeasts[i].attenuation,
                             yeasts[i].temperature_range), expected_results[i])
