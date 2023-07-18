import random
import heapq
import sys
from dataclasses import *
import jsoneng

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
        "mountain",
        "mountain village",
        "cliffs",
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
        "staff dining room",
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


locale(overworld, 4)
