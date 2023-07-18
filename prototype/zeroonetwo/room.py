import random
import heapq
import sys
from dataclasses import *
import jsoneng


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


def rooms():
    rooms = []
    while True:
        roomType = input(f"create next room... room type:")
        if roomType == "":
            print(roomsGala.keys())
            continue
        rooms.append(random.choice(roomsGala[roomType]))
        if len(rooms) > 6:
            rooms.pop(0)
        print(rooms)


rooms()
