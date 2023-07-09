import random
import heapq
from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


ClothingPreCommon = {
    "colors": ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white"],
    "adjective": ["ironed", "clean", "dirty"],
}


ClothingPostCommon = {
    "top": ["t-shirt", "dress shirt", "long shirt", "vest", "jacket", "robe"]
}

ClothingPostRich = ["top", "tuxedo", "dress shirt", "long shirt", "vest", "jacket"]


def getString(dictionary):
    return random.choice(dictionary[random.choice(list(dictionary.keys()))])


def clothing():
    return f"{getString(ClothingPreCommon)} {getString(ClothingPostCommon)}"


print(clothing())
