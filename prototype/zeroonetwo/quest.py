import random
import heapq
import sys
from dataclasses import *
import jsoneng


events = {
    "guard": ["change of guard", "encounter guard"],
    "social": ["drink", "party"],
    "omen": ["item in mirror", "vampire", "werewolf"],
}


def getString(dictionary):
    return random.choice(dictionary[random.choice(list(dictionary.keys()))])


print(getString(events))
