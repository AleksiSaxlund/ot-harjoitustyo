
class MaltsRepository:

    def __init__(self, connection):
        self._connection = connection
        self.malts = self._connection.execute(
            "SELECT name, ppg, color FROM Malts", []
            ).fetchall()

class HopsRepository:
    def __init__(self, connection):
        self._connection = connection
        self.hops = self._connection.execute(
            "SELECT name, aa FROM Hops", []
            ).fetchall()

class YeastsRepository:
    def __init__(self, connection):
        self._connection = connection
        self.yeasts = self._connection.execute(
            "SELECT name, attenuation, temperature_range FROM Yeasts", []
            ).fetchall()
