import random
from .char import *
from dataclasses import dataclass


@dataclass
class Locale:
    localeName: str
    desc: str
    ruler: str


@dataclass
class Biome:
    biomeName: str
    desc: str
    ruler: str
    locales: list[Locale]


@dataclass
class World:
    worldName: str
    desc: str
    ruler: str
    biomes: list[Biome]


placeNames = [
    "Ashbourne",
    "Bexhill",
    "Cheltenham",
    "Dorking",
    "Epsom",
    "Farnham",
    "Gillingham",
    "Harrogate",
    "Ilfracombe",
    "Jarrow",
    "Kendal",
    "Louth",
    "Matlock",
    "Newark",
    "Ormskirk",
    "Penzance",
    "Queenborough",
    "Rye",
    "Scarborough",
    "Tewkesbury",
]


class Overworld(World):
    def __init__(self):
        self.worldName = "Earth Overworld"
        self.desc = "lush, green, and blue"
        self.ruler = ""

        class Coast(Biome):
            def __init__(self):
                self.biomeName = "coast"
                self.desc = "the coast"
                self.ruler = ""

                class Beach(Locale):
                    def __init__(self):
                        self.localeName = "beach"
                        self.desc = "beach"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Marsh(Locale):
                    def __init__(self):
                        self.localeName = "marsh"
                        self.desc = "marsh"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Cliff(Locale):
                    def __init__(self):
                        self.localeName = "cliff"
                        self.desc = "cliff"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Shore(Locale):
                    def __init__(self):
                        self.localeName = "shore"
                        self.desc = "shore"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                self.locales = [Beach(), Marsh(), Cliff(), Shore()]

            def genName(self):
                return f"Seaside Duchy of {random.choice(placeNames)}"

        class Plains(Biome):
            def __init__(self):
                self.biomeName = "plains"
                self.desc = "plains"
                self.ruler = ""

                class GrassyField(Locale):
                    def __init__(self):
                        self.localeName = "grassy field"
                        self.desc = "grassy field"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class FarmLands(Locale):
                    def __init__(self):
                        self.localeName = "farm lands"
                        self.desc = "farm lands"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                self.locales = [GrassyField(), FarmLands()]

            def genName(self):
                return f"Plains Duchy of {random.choice(placeNames)}"

        class Forest(Biome):
            def __init__(self):
                self.biomeName = "forest"
                self.desc = "forest"
                self.ruler = ""

                class Woods(Locale):
                    def __init__(self):
                        self.localeName = "woods"
                        self.desc = "woods"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class DeepWoods(Locale):
                    def __init__(self):
                        self.localeName = "deep woods"
                        self.desc = "deep woods"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                self.locales = [Woods(), DeepWoods()]

            def genName(self):
                return f"Forest Duchy of {random.choice(placeNames)}"

        class Mountains(Biome):
            def __init__(self):
                self.biomeName = "mountains"
                self.desc = "mountains"
                self.ruler = ""

                class Hills(Locale):
                    def __init__(self):
                        self.localeName = "hills"
                        self.desc = "hills"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Mountains(Locale):
                    def __init__(self):
                        self.localeName = "mountains"
                        self.desc = "mountains"
                        self.ruler = ""

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                self.locales = [Hills(), Mountains()]

            def genName(self):
                return f"Mountain Duchy of {random.choice(placeNames)}"

        self.biomes = [Coast(), Plains(), Forest(), Mountains()]

    def genName(self):
        return f"Kingdom of {random.choice(placeNames)}"

    def genRuler(self):
        return Human("male", "King")

    def genDuke(self):
        return Human("male", "Duke")

    def genCount(self):
        return Human("male", "Count")
