from dataclasses import dataclass


@dataclass
class Locale:
    localeName: str
    desc: str


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
                self.biomeName = "coast"
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

        class Plains(Biome):
            def __init__(self):
                self.biomeName = "plains"
                self.desc = "the plains"

                class GrassyField(Locale):
                    def __init__(self):
                        self.localeName = "grassy field"
                        self.desc = "grassy field"

                self.locales = [GrassyField()]

        self.biomes = [Coast(), Plains()]
