from dataclasses import dataclass
from action import Action
from item import Item
from char import Char


@dataclass
class Locale:
    localeName: str
    desc: str
    listOfChars: list[Char]


@dataclass
class Biome:
    biomeName: str
    desc: str
    locales: list[Locale]


@dataclass
class World:
    worldName: str
    desc: str
    biomes: list[Biome]


class Overworld(World):
    def __init__(self):
        self.worldName = "Earth Overworld"
        self.desc = "lush, green, and blue"

        class Coast(Biome):
            def __init__(self):
                self.biomeName = "the coast"
                self.desc = "the coast"

                class Beach(Locale):
                    def __init__(self):
                        self.localeName = "beach"
                        self.desc = "beach"

                class Marsh(Locale):
                    def __init__(self):
                        self.localeName = "marsh"
                        self.desc = "marsh"

                self.locales = [Beach(), Marsh()]

        self.biomes = [Coast()]
