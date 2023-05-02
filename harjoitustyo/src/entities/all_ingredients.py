
# All amounts are in pounds or ounces.

class Malt:
    """This is a class which represents a single malt for the recipe.
    """

    def __init__(self, name: str, ppg: float, color: int):
        """Contructor of the class.

        Args:
            name (str): Name of the malt.
            ppg (float): Points per Pound per Gallon of the malt.
            color (int): The color value of the malt.
        """

        self.amount = 0
        self.name = name
        self.ppg = ppg
        self.color = color


class Hop:
    """This is a class which represents a single hop for the recipe.
    """

    def __init__(self, name: str, alpha_acids: float):
        """Constructor of the class.

        Args:
            name (str): Name of the hop.
            alpha_acids (float): The alpha acid amount of the hop.
        """

        self.amount = 0
        self.boiltime = 0
        self.name = name
        self.alpha_acids = alpha_acids


class Yeast:
    """This is a class which represents a single yeast for the recipe.
    """

    def __init__(self, name: str, attenuation: float, temperature_range: str):
        """Contructor of the class.

        Args:
            name (str): Name of the yeast.
            attenuation (float): Attenuation percentage of the yeast. Format: 0.85 = 85%.
            temperature_range (str): Temperature range of the yeast.
        """

        self.name = name
        self.attenuation = attenuation
        self.temperature_range = temperature_range
