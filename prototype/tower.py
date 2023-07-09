import random
from dataclasses import *
import heapq
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


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

tom = Person("tom")
dan = Person("dan")

registry = [tom, dan]

heapq.heappush(pentHouse.inhabitants, tom)
heapq.heappush(pentHouse.inhabitants, dan)

for i in range(len(tower)):
    if tower[i].inhabitants:
        print(tower[i])

        if i > 0 and i < len(tower) - 1:
            numHab = len(tower[i].inhabitants)
            for p in range(numHab):
                person = heapq.heappop(tower[i].inhabitants)
                heapq.heappush(tower[random.randint(-1, 1) + i].inhabitants, person)

for floor in tower:
    jdb.i(str(floor))
