import random
import heapq
import sys
from dataclasses import *
import jsoneng

biomes = {
    "overworld": [
        "coast",
        "plains",
        "forest",
        "mountains",
        "desert",
        "town",
        "city",
    ],
}

overworld = {
    "coast": [
        "beach",
        "marsh",
        "woods",
        "seaside fair",
        "seaside town",
        "seaside city",
        "port",
        "seaside road",
    ],
    "plains": [
        "grassy field",
        "flower field",
        "crops farm",
        "animal farm",
        "village",
        "village fair",
        "town",
        "city",
        "road",
        "highway",
    ],
    "forest": [
        "woods",
        "dense woods",
        "clearing",
        "hills",
        "caves",
        "campground",
        "river",
        "riverside village",
        "waterfall",
        "forest village",
        "path",
        "road",
        "highway",
    ],
    "mountains": [
        "hills",
        "waterfall",
        "cliffs",
        "caves",
        "mountain",
        "mountain top",
        "mountain village",
        "snowy alpine",
        "alpine village",
        "mountain path",
        "mountain road",
    ],
    "desert": [
        "desert",
        "mesa",
        "dune hills",
        "sand dune",
        "desert mountain",
        "desert town",
        "desert train station",
        "desert city",
        "oasis",
        "oasis town",
        "desert path",
        "desert road",
    ],
}

urban = {
    "entrance": [
        "gates",
        "tavern",
        "stable",
        "metalsmith",
        "road",
    ],
    "res": [
        "slums",
        "apartments",
        "houses",
        "convenience store",
        "fruit stalls",
        "barber shop",
        "tavern",
        "alleyway",
        "road",
    ],
    "slums": [
        "slums",
        "gambling den",
        "drug den",
        "whore house",
        "fence",
        "alleyway",
    ],
    "shops": [
        "grocers",
        "fishmongers",
        "butchers",
        "tavern",
        "textile shoppes",
        "clothing shoppes",
        "metalsmith",
        "alleyway",
        "road",
    ],
    "rich": [
        "police station",
        "apartment",
        "apartment house party",
        "mansion",
        "mansion gala party",
        "castle",
        "castle gala party",
        "restaurants",
        "tavern",
        "hotel",
        "fine grocers",
        "fine clothing shoppes",
        "bank",
        "casino",
        "gunstore",
        "road",
    ],
}

roomsGala = {
    "up": [
        "study",
        "private study",
        "vault",
        "library",
        "hallway",
        "balcony",
        "master bedroom",
        "guest room",
        "grand stairwell",
        "side stairwell",
        "secret stairwell",
    ],
    "party": [
        "reception hall",
        "great hall",
        "dance hall",
        "dining room hall",
        "grand stairwell",
        "side stairwell",
        "toilet",
        "coat check",
        "game room",
        "smoking room",
    ],
    "ground": [
        "hallway",
        "staff dining kroom",
        "kitchen",
        "staff bedroom",
        "guest room",
        "art room",
        "grand stairwell",
        "side stairwell",
        "coal dump",
        "junk room",
    ],
    "yard": [
        "entrance",
        "staff entrance",
        "underground entrance",
        "courtyard",
        "fountain",
    ],
    "low": [
        "firepit",
        "kitchen",
        "celler",
        "winery",
        "butcher table",
        "staff bedroom",
        "prison",
        "stairwell",
        "ladder to yard",
        "secret stairwell",
    ],
}

gardens = {
    "gate": [
        "ornate door",
        "guard post",
    ],
    "entrance": [
        "labyrinth entrance",
        "labyrinth trap",
        "labyrinth passage way",
    ],
    "garden": [
        "garden entrance",
        "central garden",
    ],
    "vault": [
        "guard post",
        "treasure room",
    ],
}

localeInfo = {
    "name": "",
    "population": 0,
    "security": 0,
    "supernatural": 0,
}


def getString(dictionary):
    return random.choice(dictionary[random.choice(list(dictionary.keys()))])


def locale(dictionary, size):
    steps = 0
    locale = []
    while True:
        roomType = input(f"create next locale... locale type: ")

        if roomType == "":
            print(dictionary.keys())
            continue

        steps += 1
        locale.append(random.choice(dictionary[roomType]))
        if len(locale) > size:
            locale.pop(0)

        print(f"steps: {steps}")
        print(f"{locale}")


def series(dictionary, size):
    while True:
        roomType = input(f"create next street... street type: ")

        if roomType == "":
            print(dictionary.keys())
            continue

        locale = []
        for i in range(size):
            locale.append(random.choice(dictionary[roomType]))

        import hero
        import json

        localeInfo["name"] = random.choice(hero.names["place"])
        localeInfo["population"] = random.randint(0, 2)
        localeInfo["security"] = random.randint(0, 2)
        localeInfo["supernatural"] = random.randint(0, 2)

        print(json.dumps(localeInfo, indent=4))
        print(f"{locale}")


locale(overworld, 6)

# series(overworld, 4)
