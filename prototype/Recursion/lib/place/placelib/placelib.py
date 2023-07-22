import random
from dataclasses import *

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
