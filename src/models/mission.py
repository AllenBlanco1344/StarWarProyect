class Mission:
    def __init__(self, name, planet, starship, weapons, members):
        self.name = name
        self.planet = planet
        self.starship = starship
        self.weapons = weapons
        self.members = members

    def __str__(self):
        return f"Mission: {self.name}, Planet: {self.planet}, Starship: {self.starship}"
