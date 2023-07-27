import random
from dataclasses import dataclass

from termcolor import colored
import jsoneng

from lib.char import *
from lib.locale import *

jdb = jsoneng.JsonDB()
jdb.create({})


def civGen(seed, size):
    kingdom = World(seed.genName(), "kingdom", seed.genRuler())

    for _ in range(size):
        biomeSeed = random.choice(seed.biomes)
        biome = Biome(biomeSeed.genName(), biomeSeed.desc, seed.genDuke())

        localesSize = random.randint(1, 4)
        for _ in range(localesSize):
            locale = random.choice(biomeSeed.locales)
            locale.ruler = seed.genCount()
            locale.stats = seed.genCountyStats()

            biome.locales.append(locale)

        biome.stats = seed.genDuchyStats(biome)
        kingdom.biomes.append(biome)

    kingdom.stats = seed.genKingdomStats(kingdom)
    return kingdom


def journey(overworld, size):
    day = 0
    locales = []
    stay = True
    while stay:
        choice = input(f"locale to visit: ")

        if choice == "":
            if jdb.r("hero")["location"] == None:
                print(
                    f"{colored(overworld.worldName, 'red')}, ruled by {colored(overworld.ruler.name, 'blue')}"
                )
                print(
                    f"{colored([biome.biomeName for biome in overworld.biomes], 'yellow')}"
                )
                print(f"{colored(overworld.stats, 'green')}")
            else:
                print(
                    f"{colored(selectedBiome.biomeName, 'red')}, ruled by {colored(selectedBiome.ruler.name, 'blue')}"
                )
                print(f"{colored([locale.localeName for locale in locales], 'yellow')}")
                print(f"{colored(selectedBiome.stats, 'green')}")
            continue

        if choice == "leave":
            jdb.p(
                "hero",
                {
                    "location": None,
                },
            )
            continue

        # day += 1

        selectedBiome = overworld.biomes[int(choice)]

        locales = selectedBiome.locales

        jdb.p(
            "hero",
            {
                "location": int(choice),
            },
        )

        # for biome in overworld.biomes:
        #     if biomeType == biome.biomeName:
        #         selectedLocale = random.choice(biome.locales)
        #         locales.append(selectedLocale.localeName)
        #         # selectedLocale.localeAffect()

        # if len(locales) > size:
        #     locales.pop(0)

        # print(f"day: {colored(day, 'red')}")
        # print(
        #     f"{colored(selectedBiome.biomeName, 'red')}, ruled by {colored(selectedBiome.ruler.name, 'blue')}"
        # )
        # print(f"{colored([locale.localeName for locale in locales], 'yellow')}")


def main():
    hero = {
        "location": None,
    }
    jdb.p("hero", hero)
    seed = Overworld()
    world = civGen(seed, 4)
    jdb.p("kingdom", asdict(world))
    journey(world, 4)


# if __name__ == "__main__":
#     main()
