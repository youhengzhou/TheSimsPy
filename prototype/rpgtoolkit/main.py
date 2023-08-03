import random
from dataclasses import dataclass, asdict
from termcolor import cprint, colored
import jsoneng

from lib.data import Char, Event, Place

jdb = jsoneng.JsonDB({})


def testAction():
    print("what's 1 + 1?")
    answer = input("> ")
    if answer == "2":
        print("you win!")
        return
    print("you lose!")


test = Event("test", "you have a test coming up, what do you do?", testAction)

home = Place("home", "your home", ["school"], [])
school = Place("school", "your school", ["home"], [test])

p_map = {
    "home": home,
    "school": school,
}


def newDay(time, currentPlace):
    newDayData = f"""day: {colored(time, 'red')}
you are in {currentPlace.name}
available actions:
0. rest
1. move
2. events

enter the action you want below"""
    return view(newDayData, True)


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

    return currentPlace


def getEvents(time, currentPlace):
    if currentPlace.events:
        # get event
        currentEvent = random.choice(currentPlace.events)
        currentEvent.action()

        # ask player to describe in diary
        cprint("write down what happened please", "red")
        text = view("> ", "white", True)
        jdb.patch({time: {"prompt": currentEvent.desc, "answer": text}})
    else:
        cprint("no available events", "red")


def view(info, prompt=False):
    print("")
    print("---view---")
    cprint(info, prompt) if type(prompt) == str else print(info)
    print("---view---")
    print("")
    return input("> ")


def main(time, currentPlace):
    while True:
        userChoice = newDay(time, currentPlace)

        if userChoice == "exit":
            view("thank you for playing")
            break

        if userChoice == "0":
            view("you rested", True)

        elif userChoice == "1":
            view("move where?", "red")

            currentPlace = changeCurrentPlace(time, currentPlace)

        elif userChoice == "2":
            getEvents(time, currentPlace)

        else:
            view("invalid choice")

        view("time passes...", True)
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

ideal = [
    "altruism",
    "survival",
    "mayhem",
]
raised = [
    "cultist",
    "isolate",
    "raider",
    "sheltered",
    "pariah",
    "settler",
]
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
    main(0, p_map["home"])
