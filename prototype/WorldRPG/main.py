import random
from dataclasses import dataclass

from termcolor import colored
import jsoneng

from lib.char import *
from lib.locale import *

jdb = jsoneng.JsonDB()
jdb.create({})


def civGen(seed, size):
    kingdom = World(seed.genName(), "kingdom", seed.genRuler(), [])

    for _ in range(size):
        biomeSeed = random.choice(seed.biomes)
        biome = Biome(biomeSeed.genName(), biomeSeed.desc, seed.genDuke(), [])

        localesSize = random.randint(1, 4)
        for _ in range(localesSize):
            locale = random.choice(biomeSeed.locales)
            locale.ruler = seed.genCount()

            biome.locales.append(locale)

        kingdom.biomes.append(biome)

    return kingdom


def journey(overworld, size):
    day = 0
    locales = []
    stay = True
    while stay:
        biomeType = input(f"create next locale... locale type: ")

        if biomeType == "":
            print(f"{colored([biome.biomeName for biome in overworld.biomes], 'red')}")
            continue

        if biomeType == "escape":
            stay = False
            continue

        day += 1

        for biome in overworld.biomes:
            if biomeType == biome.biomeName:
                selectedLocale = random.choice(biome.locales)
                locales.append(selectedLocale.localeName)
                # selectedLocale.localeAffect()

        if len(locales) > size:
            locales.pop(0)

        print(f"day: {colored(day, 'red')}")
        print(f"{locales}")


def main():
    hero = {}
    jdb.p("hero", hero)
    seed = Overworld()
    world = civGen(seed, 4)
    jdb.p("kingdom", asdict(world))
    journey(world, 4)


if __name__ == "__main__":
    main()
