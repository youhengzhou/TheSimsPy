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

street = Place("street", "Street", ["h_door", "s_door"])

s_door = Place("s_door", "School Door", ["street", "s_hallway"])
s_hallway = Place("s_hallway", "School Hallway", ["s_door"])

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
    "street": [street, []],
    "s_door": [s_door, []],
    "s_hallway": [s_hallway, []],
}


def travel():
    currentPlace = h_livingroom
    while True:
        for i in range(len(currentPlace.neighbors)):
            cprint(f"{i}. {p_map[currentPlace.neighbors[i]][0].name}.", "red")

        choice = input("enter place: > ")

        if choice == "exit":
            break

        if choice.isdigit() and 0 <= int(choice) <= len(currentPlace.neighbors) - 1:
            chosen_neighbor = currentPlace.neighbors[int(choice)]
            print(f"Moving to {p_map[chosen_neighbor][0].name}...\n")
            currentPlace = p_map[chosen_neighbor][0]
        else:
            print("Invalid neighbor choice.\n")


def resolveCombat(p1, p2, place, event):
    pass


travel()
