import random
from dataclasses import dataclass

from termcolor import colored
import jsoneng

from lib.char import *
from lib.place import *

jdb = jsoneng.JsonDB()
jdb.create({})


def journey(world, size):
    selectedPlace = world
    displayPlaces = world.subPlaces
    while True:
        choice = input(f"locale to visit: ")

        if choice == "":
            print(
                f"{colored(selectedPlace.desc.name, 'red')}, ruled by {colored(selectedPlace.ruler.desc.name, 'blue')}"
            )
            print(
                f"{colored([locale.desc.name for locale in displayPlaces], 'yellow')}"
            )
            print(f"{colored(selectedPlace.stats, 'green')}")
            continue

        if choice == "quit":
            break

        if choice == "leave":
            selectedPlace = world
            displayPlaces = world.subPlaces
            jdb.p(
                "hero",
                {
                    "location": None,
                },
            )
            continue

        if selectedPlace.subPlaces:
            selectedPlace = selectedPlace.subPlaces[int(choice)]
            displayPlaces = selectedPlace.subPlaces
            jdb.p(
                "hero",
                {
                    "location": int(choice),
                },
            )


def main():
    hero = {
        "location": None,
    }
    jdb.p("hero", hero)

    k = Kingdom(4)
    jdb.p("kingdom", asdict(k))

    journey(k, 4)


if __name__ == "__main__":
    main()
