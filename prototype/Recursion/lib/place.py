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


def quickStats(self):
    pop = 0
    dip = 0
    mil = 0
    prd = 0

    for sp in self.subPlaces:
        pop += sp.stats.pop
        dip += sp.stats.dip
        mil += sp.stats.mil
        prd += sp.stats.prd

    self.stats = Stats(pop, dip, mil, prd)


@dataclass
class Place:
    desc: PlaceDesc
    ruler: str
    stats: Stats
    subPlaces: list

    def __init__(self, desc=None, ruler=None, stats=None):
        self.desc = PlaceDesc(desc, random.choice(placeNames))
        self.ruler = ruler
        self.stats = stats
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

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)
                        quickStats(self)

                class Cliff(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Cliff County", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)
                        quickStats(self)

                class Shore(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Shore County", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)
                        quickStats(self)

                self.seed = [Beach, Cliff, Shore]

                structures = [
                    Place(
                        "Seaside Castle",
                        Ruler("Baron"),
                        Stats(
                            random.randint(1, 2),
                            random.randint(1, 2),
                            random.randint(3, 4),
                            random.randint(1, 2),
                        ),
                    ),
                    Place(
                        "Seaside Town",
                        Ruler("Baron"),
                        Stats(
                            random.randint(2, 3),
                            random.randint(1, 2),
                            random.randint(1, 2),
                            random.randint(1, 2),
                        ),
                    ),
                ]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())
                quickStats(self)

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

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)

                class Farmland(Place):
                    def __init__(self):
                        self.desc = PlaceDesc("Farmland", random.choice(placeNames))
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)

                self.seed = [Grassland, Farmland]

                structures = [
                    Place(
                        "Plains Castle",
                        Ruler("Baron"),
                        Stats(
                            random.randint(6, 10),
                            random.randint(4, 6),
                            random.randint(6, 10),
                            random.randint(6, 8),
                        ),
                    ),
                    Place(
                        "Plains City",
                        Ruler("Baron"),
                        Stats(
                            random.randint(8, 12),
                            random.randint(4, 6),
                            random.randint(4, 6),
                            random.randint(6, 10),
                        ),
                    ),
                ]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())
                quickStats(self)

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

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)

                class DeepWoods(Place):
                    def __init__(self):
                        self.desc = PlaceDesc(
                            "Deep Woods County", random.choice(placeNames)
                        )
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)

                self.seed = [Woods, DeepWoods]

                structures = [
                    Place(
                        "Forest Castle",
                        Ruler("Baron"),
                        Stats(
                            random.randint(5, 8),
                            random.randint(1, 2),
                            random.randint(3, 4),
                            random.randint(3, 6),
                        ),
                    ),
                    Place(
                        "Forest City",
                        Ruler("Baron"),
                        Stats(
                            random.randint(5, 10),
                            random.randint(1, 2),
                            random.randint(2, 3),
                            random.randint(3, 6),
                        ),
                    ),
                ]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())
                quickStats(self)

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

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)

                class Mountains(Place):
                    def __init__(self):
                        self.desc = PlaceDesc(
                            "Mountains County", random.choice(placeNames)
                        )
                        self.ruler = Ruler("Count")
                        self.stats = Stats()
                        self.subPlaces = []

                        self.subPlaces.append(random.choice(structures))
                        quickStats(self)

                self.seed = [Hills, Mountains]

                structures = [
                    Place(
                        "Mountain Castle",
                        Ruler("Baron"),
                        Stats(
                            random.randint(1, 2),
                            random.randint(1, 2),
                            random.randint(4, 6),
                            random.randint(2, 3),
                        ),
                    ),
                    Place(
                        "Mountain Village",
                        Ruler("Baron"),
                        Stats(
                            random.randint(2, 3),
                            random.randint(1, 2),
                            random.randint(2, 3),
                            random.randint(2, 3),
                        ),
                    ),
                ]

                for _ in range(size):
                    self.subPlaces.append(random.choice(self.seed)())
                quickStats(self)

        self.seed = [Coast, Plains, Forest, Mountains]

        for _ in range(size):
            self.subPlaces.append(random.choice(self.seed)(random.randint(1, 4)))
        quickStats(self)
