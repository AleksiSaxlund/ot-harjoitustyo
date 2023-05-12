from entities.all_ingredients import Malt, Hop, Yeast
import database_connections


class MaltsRepository:
    """Class for handling all malt database interactions.
    """

    def __init__(self):
        """Constructor of the class.
        Connects into the malts database and reads all values into a variable.
        """
        self._connection = database_connections.get_malts_connection()
        self.malts = self._connection.execute(
            "SELECT name, ppg, color FROM Malts", []
        ).fetchall()

    def get_all_malts(self):
        """Converts all of the malts into Malt objects.
        Then returns them as a list.

        Returns:
            list: A list of all malts as Malt objects.
        """
        malts = []

        for malt in self.malts:
            malts.append(Malt(malt[0], float(malt[1]), int(malt[2])))

        return malts


class HopsRepository:
    """Class for handling all hop database interactions.
    """

    def __init__(self):
        """Constructor of the class.
        Connects into the hops database and reads all values into a variable.
        """

        self._connection = database_connections.get_hops_connection()
        self.hops = self._connection.execute(
            "SELECT name, aa FROM Hops", []
        ).fetchall()

    def get_all_hops(self):
        """Converts all of the hops into Hop objects.
        Then returns them as a list.

        Returns:
            list: A list of all hops as Hop objects.
        """
        hops = []

        for hop in self.hops:
            hops.append(Hop(hop[0], float(hop[1])))

        return hops


class YeastsRepository:
    """Class for handling all yeast database interactions.
    """

    def __init__(self):
        """Constructor of the class.
        Connects into the yeasts database and reads all values into a variable.
        """

        self._connection = database_connections.get_yeasts_connection()
        self.yeasts = self._connection.execute(
            "SELECT name, attenuation, temperature_range FROM Yeasts", []
        ).fetchall()

    def get_all_yeasts(self):
        """Converts all of the yeasts into Yeast objects.
        Then returns them as a list.

        Returns:
            list: A list of all yeasts as Yeast objects.
        """
        yeasts = []

        for yeast in self.yeasts:
            yeasts.append(Yeast(yeast[0], float(yeast[1]), yeast[2]))

        return yeasts
