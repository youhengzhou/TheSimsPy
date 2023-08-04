import random
from dataclasses import dataclass
import os
from termcolor import cprint

import jsoneng

jdb = jsoneng.JsonDB()


@dataclass
class Char:
    name: str
    role: str
    hth: int
    str: int
    dex: int
    int: int
    cha: int


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


def view(info, color=False):
    os.system("cls" if os.name == "nt" else "clear")
    print("")
    print("---view---")
    cprint(info, color) if type(color) == str else print(info)
    print("---view---")
    print("")
    return input("> ")


def testAction():
    answer = view("what's 1 + 1?")
    if answer == "2":
        view("you win!")
        return
    view("you lose!")


def TYOV():
    output = ""

    def randomRoll(dictionary):
        def rollDice():
            return random.randint(1, 10) - random.randint(1, 6)

        def updateRoll(roll, increment=0):
            return rollDice() + roll + increment

        def assignPart(countsOfRoll, roll):
            currentCount = countsOfRoll.get(roll, 0) + 1
            countsOfRoll[roll] = currentCount
            return f"{roll}{chr(ord('a')+currentCount-1)}"

        out = []
        countsOfRoll = {}

        roll = 0
        while roll <= 80:
            roll = updateRoll(roll, 2)
            part = assignPart(countsOfRoll, roll)

            # This code snippet checks if the variable part is a key in the dictionary.
            # If it is, it assigns the corresponding value to the out dictionary with the same key.
            if part in dictionary:
                out.append(dictionary[part])

        return out
    
    jdb.p('tyov count', int(jdb.r('tyov count')) + 1)

    view(output)


test = Event("test", "you have a test coming up, what do you do?", testAction)

home = Place("home", "your home", ["school"], [])
school = Place("school", "your school", ["home"], [test])

p_map = {
    "home": home,
    "school": school,
}


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
