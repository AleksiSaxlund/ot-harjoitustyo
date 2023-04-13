
class Malt:
    def __init__(self, name: str, ppg: float, color: int):
        self.amount = 0
        self.name = name
        self.ppg = ppg
        self.color = color


class Hop:
    def __init__(self, name: str, alpha_acids: float):
        self.amount = 0
        self.boiltime = 0
        self.name = name
        self.alpha_acids = alpha_acids


class Yeast:
    def __init__(self, name: str, attenuation: int, temperature_range: str):
        self.name = name
        self.attenuation = attenuation
        self.temperature_range = temperature_range
