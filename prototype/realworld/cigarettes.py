import random
from dataclasses import dataclass, asdict
from termcolor import cprint
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


@dataclass
class Char:
    name: str
    role: str
    authenciticy: int
    resolve: int
    inspiration: int
    personality: int


@dataclass
class Event:
    key: str
    desc: str
    action: None


@dataclass
class Place:
    key: str
    name: str
    neighbors: list
    events: list


def testAction():
    print("what's 1 + 1?")
    answer = input("> ")
    if answer == "2":
        print("you win!")
        return
    print("you lose!")


test = Event("test", "you have a test coming up, what do you do?", testAction)

military_sacking = Event()

home = Place("home", "your home", ["school"], [])
school = Place("school", "your school", ["home"], [test])

p_map = {
    "home": home,
    "school": school,
}


def newDay(time, currentPlace):
    cprint(f"a new day, day: {time}, and you are in {currentPlace.name}", "blue")
    cprint("available actions:", "green")
    cprint("0. rest", "red")
    cprint("1. move", "red")
    cprint("2. events", "red")
    action = input("enter action: > ")
    return action


def changeCurrentPlace(time, currentPlace):
    cprint("available neighbors:", "green")
    for i in range(len(currentPlace.neighbors)):
        cprint(f"{i}. {p_map[currentPlace.neighbors[i]].name}.", "red")

    # choose neighbor
    choice = input("enter location: > ")
    if choice.isdigit() and 0 <= int(choice) <= len(currentPlace.neighbors) - 1:
        chosen_neighbor = currentPlace.neighbors[int(choice)]
        cprint(f"Moving to {p_map[chosen_neighbor].name}...", "red")
        currentPlace = p_map[chosen_neighbor]
    else:
        cprint("Invalid neighbor choice.", "red")


def getEvents(time, currentPlace):
    if currentPlace.events:
        # get event
        cprint("you get an event:", "green")
        currentEvent = random.choice(currentPlace.events)
        currentEvent.action()

        # ask player to describe in diary
        cprint("write down what happened please", "red")
        text = input("> ")
        jdb.patch({time: {"prompt": currentEvent.desc, "answer": text}})
        print("")
    else:
        cprint("no available events", "red")


def main(time, currentPlace):
    while True:
        userChoice = newDay(time, currentPlace)

        if userChoice == "exit":
            print("thank you for playing")
            break

        if userChoice == "0":
            print("you rested")

        elif userChoice == "1":
            print("move where?")

            currentPlace = changeCurrentPlace(time, currentPlace)

        elif userChoice == "2":
            getEvents(time, currentPlace)

        else:
            cprint("invalid choice", "red")

        input("time passes...\n")
        time += 1


ideal = ["revenge"]


@dataclass
class Foe:
    name: str
    drives: list
    risks: list
    obstacles: list


@dataclass
class Risk:
    hinders: list
    attention: list
    resources: list
    delay: list


"""
Thing
name
desc
stats
things

name
federation

sanity
perspicacity
tenacity
personality
dexterity

close quarters
open field
foilage
dense foilage
urban

drives
attacks
defenses

hinderance
alarm
supply
delay

attack
defense
shock

sword/axe/mace
greatsword/axe/mace
short sword/dagger/knife
polearm
staff

bow
long bow
crossbow
hand gun
long gun

light shield
tower shield
cloth armor
torso armor
full armor

sanity/perspicacity

militia
recruit
regular
veteran
mastery

bedroom
living room
dining room
kitchen
washroom

office
game rooom
lab
trophy room
library

attic
basement
hallway
doorway
yard

military
church
business
school
country club
gang bar
fence
farm
"""

ideal = ["altruism", "survival", "mayhem"]
raised = ["cultist", "isolate", "raider", "sheltered", "pariah", "settler"]
trademark = [
    "outlandish hair",
    "tire pauldron",
    "glasses",
    "goggle eyepatch",
    "cryo-stasis burns",
    "old-timey voice",
    "mechanical augment",
    "facepaint",
    "tattoos",
    "jaunty hat",
]
goods = [
    "ammo box",
    "armored coat",
    "bedroll",
    "crowbar",
    "flashlight",
    "knife",
    "meds",
    "rifle",
    "rope",
    "pistol",
]

if __name__ == "__main__":
    print("hi")
    # main(0, p_map["home"])
