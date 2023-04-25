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
                found.append(Malt(malt[0], float(malt[1]), int(malt[2])))

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
                found.append(Hop(hop[0], float(hop[1])))

        return list(enumerate(found))


class YeastsRepository:
    def __init__(self):
        self._connection = database_connections.get_yeasts_connection()
        self._yeasts = self._connection.execute(
            "SELECT name, attenuation, temperature_range FROM Yeasts", []
        ).fetchall()

    def search(self, search):
        found = []

        for yeast in self._yeasts:
            if search.lower() in yeast[0].lower():
                found.append(Yeast(yeast[0], float(yeast[1]), yeast[2]))

        return list(enumerate(found))

    def get_all_yeasts(self):
        yeasts = []

        for yeast in self._yeasts:
            yeasts.append(Yeast(yeast[0], float(yeast[1]), yeast[2]))

        return yeasts
