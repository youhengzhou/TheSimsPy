import random
from .char import *
from dataclasses import dataclass


@dataclass
class Stats:
    pop: int
    dip: int
    mil: int
    prd: int

    def __init__(self, pop=0, dip=0, mil=0, prd=0):
        self.pop = pop
        self.dip = dip
        self.mil = mil
        self.prd = prd


@dataclass
class Locale:
    localeName: str
    desc: str
    ruler: str
    stats: Stats

    def __init__(self, localeName, desc, ruler):
        self.localeName = localeName
        self.desc = desc
        self.ruler = ruler
        self.stats = Stats()


@dataclass
class Biome:
    biomeName: str
    desc: str
    ruler: str
    stats: Stats
    locales: list[Locale]

    def __init__(self, biomeName, desc, ruler):
        self.biomeName = biomeName
        self.desc = desc
        self.ruler = ruler
        self.stats = Stats()
        self.locales = []


@dataclass
class World:
    worldName: str
    desc: str
    ruler: str
    stats: Stats
    biomes: list[Biome]

    def __init__(self, worldName, desc, ruler):
        self.worldName = worldName
        self.desc = desc
        self.ruler = ruler
        self.stats = Stats()
        self.biomes = []


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
        self.stats = Stats()

        class Coast(Biome):
            def __init__(self):
                self.biomeName = "coast"
                self.desc = "the coast"
                self.ruler = ""
                self.stats = Stats()

                class Beach(Locale):
                    def __init__(self):
                        self.localeName = "beach"
                        self.desc = "beach"
                        self.ruler = ""
                        self.stats = Stats()

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Marsh(Locale):
                    def __init__(self):
                        self.localeName = "marsh"
                        self.desc = "marsh"
                        self.ruler = ""
                        self.stats = Stats()

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Cliff(Locale):
                    def __init__(self):
                        self.localeName = "cliff"
                        self.desc = "cliff"
                        self.ruler = ""
                        self.stats = Stats()

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Shore(Locale):
                    def __init__(self):
                        self.localeName = "shore"
                        self.desc = "shore"
                        self.ruler = ""
                        self.stats = Stats()

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
                self.stats = Stats()

                class GrassyField(Locale):
                    def __init__(self):
                        self.localeName = "grassy field"
                        self.desc = "grassy field"
                        self.ruler = ""
                        self.stats = Stats()

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class FarmLands(Locale):
                    def __init__(self):
                        self.localeName = "farm lands"
                        self.desc = "farm lands"
                        self.ruler = ""
                        self.stats = Stats()

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
                self.stats = Stats()

                class Woods(Locale):
                    def __init__(self):
                        self.localeName = "woods"
                        self.desc = "woods"
                        self.ruler = ""
                        self.stats = Stats()

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class DeepWoods(Locale):
                    def __init__(self):
                        self.localeName = "deep woods"
                        self.desc = "deep woods"
                        self.ruler = ""
                        self.stats = Stats()

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
                self.stats = Stats()

                class Hills(Locale):
                    def __init__(self):
                        self.localeName = "hills"
                        self.desc = "hills"
                        self.ruler = ""
                        self.stats = Stats()

                    def genName(self):
                        return f"County of {random.choice(placeNames)}"

                class Mountains(Locale):
                    def __init__(self):
                        self.localeName = "mountains"
                        self.desc = "mountains"
                        self.ruler = ""
                        self.stats = Stats()

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

    def genCountyStats(self):
        return Stats(
            random.randint(1, 5),
            random.randint(1, 5),
            random.randint(1, 5),
            random.randint(1, 5),
        )

    def genDuchyStats(self, duchy):
        pop = 0
        dip = 0
        mil = 0
        prd = 0

        for county in duchy.locales:
            pop += county.stats.pop
            dip += county.stats.dip
            mil += county.stats.mil
            prd += county.stats.prd

        return Stats(
            pop,
            dip,
            mil,
            prd,
        )

    def genKingdomStats(self, kingdom):
        pop = 0
        dip = 0
        mil = 0
        prd = 0

        for biome in kingdom.biomes:
            pop += biome.stats.pop
            dip += biome.stats.dip
            mil += biome.stats.mil
            prd += biome.stats.prd

        return Stats(
            pop,
            dip,
            mil,
            prd,
        )
