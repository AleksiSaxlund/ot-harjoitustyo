from entities.all_ingredients import Malt, Hop, Yeast
import database_connections


class MaltsRepository:

    def __init__(self):
        self._connection = database_connections.get_malts_connection()
        self.malts = self._connection.execute(
            "SELECT name, ppg, color FROM Malts", []
        ).fetchall()

    def search(self, search):
        found = []

        for malt in self.malts:
            if search.lower() in malt[0].lower():
                found.append(Malt(malt[0], malt[1], malt[2]))

        return list(enumerate(found))


class HopsRepository:
    def __init__(self):
        self._connection = database_connections.get_hops_connection()
        self.hops = self._connection.execute(
            "SELECT name, aa FROM Hops", []
        ).fetchall()

    def search(self, search):
        found = []

        for hop in self.hops:
            if search.lower() in hop[0].lower():
                found.append(Hop(hop[0], hop[1]))

        return list(enumerate(found))


class YeastsRepository:
    def __init__(self):
        self._connection = database_connections.get_yeasts_connection()
        self.yeasts = self._connection.execute(
            "SELECT name, attenuation, temperature_range FROM Yeasts", []
        ).fetchall()

    def search(self, search):
        found = []

        for yeast in self.yeasts:
            if search.lower() in self.yeast[0].lower():
                found.append(Yeast(yeast[0], yeast[1], yeast[2]))

        return list(enumerate(found))
