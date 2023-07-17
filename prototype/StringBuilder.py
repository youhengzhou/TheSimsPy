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

clothingPostRich = ["top", "tuxedo", "dress shirt", "long shirt", "vest", "jacket"]


def getString(dictionary):
    return random.choice(dictionary[random.choice(list(dictionary.keys()))])


def comb(one, two):
    if type(one) != dict:
        return f"{one} {getString(two)}"
    elif type(two) != dict:
        return f"{getString(one)} {two}"
    else:
        return f"{getString(one)} {getString(two)}"


print(comb(clothingPreCommon, clothingPostCommon))

for i in range(100):
    outfit = comb(clothingPreCommon, clothingPostCommon)
    role = comb(humanPre, random.choice(humanPost["civilian"]))
    print(f"{role}      -wearing-    {outfit}")
