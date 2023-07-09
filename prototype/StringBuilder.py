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


def getString(dictionary):
    return random.choice(dictionary[random.choice(list(dictionary.keys()))])


def clothing():
    return f"{getString(ClothingPreCommon)} {getString(ClothingPostCommon)}"


print(clothing())


@dataclass
class Person:
    name: str

    def __init__(self, name):
        self.name = name

    def __lt__(self, other):
        return self.name < other.name


@dataclass
class Floor:
    name: str
    inhabitants: list

    def __init__(self, name):
        self.name = name
        self.inhabitants = []
        heapq.heapify(self.inhabitants)


spaceElevator = Floor("space elevator")
pentHouse = Floor("penthouse")
apartments = Floor("apartments")

tower = [spaceElevator, pentHouse, apartments]

for floor in tower:
    jdb.i(str(floor))

tom = Person("tom")
dan = Person("dan")

registry = [tom, dan]

heapq.heappush(pentHouse.inhabitants, tom)
heapq.heappush(pentHouse.inhabitants, dan)

for i in range(len(tower)):
    if tower[i].inhabitants:
        print(tower[i])

        if tower[i] > 0 and tower[i] < len(tower) - 1:
            for p in range(len(tower)):
                print(tower[i])

                person = heapq.heappop(tower[i].inhabitants)

                # heapq.heappush(tower[random.randint(-1, 1) + i], person)

# print(tower)
