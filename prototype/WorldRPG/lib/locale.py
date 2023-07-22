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

                class Cliff(Locale):
                    def __init__(self):
                        self.localeName = "cliff"
                        self.desc = "cliff"

                class Shore(Locale):
                    def __init__(self):
                        self.localeName = "shore"
                        self.desc = "shore"

                self.locales = [Beach(), Marsh(), Cliff(), Shore()]

        class Plains(Biome):
            def __init__(self):
                self.biomeName = "plains"
                self.desc = "plains"

                class GrassyField(Locale):
                    def __init__(self):
                        self.localeName = "grassy field"
                        self.desc = "grassy field"

                class FarmLands(Locale):
                    def __init__(self):
                        self.localeName = "farm lands"
                        self.desc = "farm lands"

                self.locales = [GrassyField(), FarmLands()]

        class Forest(Biome):
            def __init__(self):
                self.biomeName = "forest"
                self.desc = "forest"

                class Woods(Locale):
                    def __init__(self):
                        self.localeName = "woods"
                        self.desc = "woods"

                class DeepWoods(Locale):
                    def __init__(self):
                        self.localeName = "deep woods"
                        self.desc = "deep woods"

                self.locales = [Woods(), DeepWoods()]

        class Mountains(Biome):
            def __init__(self):
                self.biomeName = "mountains"
                self.desc = "mountains"

                class Hills(Locale):
                    def __init__(self):
                        self.localeName = "hills"
                        self.desc = "hills"

                class Mountains(Locale):
                    def __init__(self):
                        self.localeName = "mountains"
                        self.desc = "mountains"

                self.locales = [Hills(), Mountains()]

        self.biomes = [Coast(), Plains(), Forest(), Mountains()]
