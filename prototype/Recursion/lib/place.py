import random
from dataclasses import *
from .char import *

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


@dataclass
class PlaceDesc:
    name: str
    desc: str

    def __init__(self, type, name, desc=""):
        self.name = f"{type} of {name}"
        self.desc = ""


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
class Place:
    desc: PlaceDesc
    ruler: str
    stats: Stats
    subPlaces: list

    def __init__(self):
        self.desc = PlaceDesc()
        self.ruler = Char()
        self.stats = Stats()
        self.subPlaces = []


class Kingdom(Place):
    def __init__(self, size):
        self.desc = PlaceDesc("Kingdom", random.choice(placeNames))
        self.ruler = Ruler("King")
        self.stats = Stats()
        self.subPlaces = []

        class Coast(Place):
            def __init__(self, size=0):
                self.desc = PlaceDesc("Coastal Duchy", random.choice(placeNames))
                self.ruler = Ruler("Duke")
                self.stats = Stats()
                self.subPlaces = []

                class Beach(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Beach County", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                class Cliff(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Cliff County", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                class Shore(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Shore County", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                self.seed = [Beach, Cliff, Shore]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())

        class Plains(Place):
            def __init__(self, size=0):
                self.desc = PlaceDesc("Plains Duchy", random.choice(placeNames))
                self.ruler = Ruler("Duke")
                self.stats = Stats()
                self.subPlaces = []

                class Grassland(Place):
                    def __init__(self):
                        self.desc = PlaceDesc(
                            "Grassland County", random.choice(placeNames)
                        )
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                class Farmland(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Farmland", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                self.seed = [Grassland, Farmland]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())

        class Forest(Place):
            def __init__(self, size=0):
                self.desc = PlaceDesc("Forest Duchy", random.choice(placeNames))
                self.ruler = Ruler("Duke")
                self.stats = Stats()
                self.subPlaces = []

                class Woods(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Woods County", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                class DeepWoods(Place):
                    def __init__(self):
                        self.desc = PlaceDesc(
                            "Deep Woods County", random.choice(placeNames)
                        )
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                self.seed = [Woods, DeepWoods]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())

        class Mountains(Place):
            def __init__(self, size=0):
                self.desc = PlaceDesc("Mountain Duchy", random.choice(placeNames))
                self.ruler = Ruler("Duke")
                self.stats = Stats()
                self.subPlaces = []

                class Hills(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Hills County", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                class Mountains(Place):
                    def __init__(self):
                        self.desc = PlaceDesc(
                            "Mountains County", random.choice(placeNames)
                        )
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                self.seed = [Hills, Mountains]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())

        self.seed = [Coast, Plains, Forest, Mountains]

        for _ in range(size):
            self.subPlaces.append(random.choice(self.seed)(random.randint(1,4)))
