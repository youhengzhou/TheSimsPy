import random
from dataclasses import dataclass

from termcolor import colored
import jsoneng

from lib.char import *
from lib.locale import *

jdb = jsoneng.JsonDB()
jdb.create({})


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
    journey(Overworld(), 4)


if __name__ == "__main__":
    main()
