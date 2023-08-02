import random
from dataclasses import dataclass, asdict
from termcolor import cprint
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


@dataclass
class Event:
    key: str
    desc: str


@dataclass
class Place:
    key: str
    name: str
    neighbors: list


h_livingroom = Place("h_livingroom", "Living Room", ["h_hallway"])
h_hallway = Place("h_hallway", "Hallway", ["h_livingroom", "h_door"])
h_door = Place("h_door", "House Front Door", ["h_hallway", "street"])

h_events = [
    Event("h_hunger", "You are hungry. What do you do?"),
    Event("h_thirst", "You are thirsty. What do you do?"),
    Event("h_tired", "You are tired. What do you do?"),
    Event("h_happy", "You are happy. What do you do?"),
    Event("h_sad", "You are sad. What do you do?"),
]

p_map = {
    "h_livingroom": [h_livingroom, h_events],
    "h_hallway": [h_hallway, h_events],
    "h_door": [h_door, h_events],
}


def travel():
    currentPlace = h_livingroom
    while True:
        for i in range(len(currentPlace.neighbors)):
            cprint(f"{i}. {p_map[currentPlace.neighbors[i]][0].name}.", "red")

        userInput = input("enter place: > ")

        if userInput == "exit":
            break

        # if userInput in p_map:
        #     current_place = p_map[userInput][0]
        #     cprint(f"You are in {current_place.name}.", "red")


def resolveCombat(p1, p2, place, event):
    pass


travel()
