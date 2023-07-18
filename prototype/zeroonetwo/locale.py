import random
import heapq
import sys
from dataclasses import *
import jsoneng

overworld = {
    "coast": ["beach", "forest", "seaside town", "seaside city", "port", "road"],
    "forest": ["woods", "forest village", "road"],
    "plain": ["grassy field", "village", "town", "city", "road", "highway"],
    "urban": [
        "gala",
        "castle",
        "shopping district",
        "inn",
        "prison",
        "bank",
        "gambling den",
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
    locale = []
    while True:
        roomType = input(f"create next locale... locale type: ")
        if roomType == "":
            print(dictionary.keys())
            continue
        locale.append(random.choice(dictionary[roomType]))
        if len(locale) > size:
            locale.pop(0)
        print(locale)


locale(overworld, 4)
