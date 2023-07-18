import random
import heapq
from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

humanPre = {
    # "type": ["lyonian", "falconian", "borderlander", "draconian", "tigian"],
    # "name": ["common", "archaic", "uncommon", "noble"],
    "look": ["plain", "soft", "attractive", "stern"],
    "build": ["normal", "small", "muscular", "lean"],
    "style": ["incognito", "simple", "stylish", "armored"],
}

humanPost = {
    "civilian": ["slave", "serf", "commoner", "nomad"],
    "military": ["watch", "guard", "soldier", "knight"],
    "religious": ["monk", "priest", "bishop", "cardinal"],
    "civil": ["scribe", "artisan", "shopkeeper", "banker"],
}

clothingPreCommon = {
    "colors": ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"],
    "adjective": [
        "ironed",
        "clean",
        "dirty",
        "old fashioned",
        "expensive",
        "cheap",
        "old",
        "comfortable",
        "normal",
    ],
}


clothingPostCommon = {
    "top": [
        "t-shirt",
        "dress shirt",
        "long shirt",
        "vest",
        "jacket",
        "robe",
        "hoodie",
        "graphic tee",
        "rain coat",
        "suit",
    ]
}

clothingPostRich = {"top": ["tuxedo", "dress shirt", "long shirt", "vest", "jacket"]}

roomsGala = {
    "upper floor": ["study", "vault", "hallway", "master bedroom", "guest room"],
    "ground floor": [
        "reception hall",
        "hallway",
        "dining room",
        "dance hall",
        "kitchen",
        "staff bedroom",
        "guest room",
        "art room",
        "lounge",
        "gaming lounge",
        "smoke room",
    ],
    "basement": [
        "firepit",
        "kitchen",
        "celler",
        "winery",
        "butcher table",
        "staff bedroom",
        "prison",
    ],
}


def comb(one, two):
    def getString(dictionary):
        return random.choice(dictionary[random.choice(list(dictionary.keys()))])

    if type(one) != dict:
        return f"{one} {getString(two)}"
    elif type(two) != dict:
        return f"{getString(one)} {two}"
    else:
        return f"{getString(one)} {getString(two)}"
