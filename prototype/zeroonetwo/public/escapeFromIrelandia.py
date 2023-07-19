from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

# ESCAPE FROM IRELANDIA

# CHARACTERS


@dataclass
class Char:
    name: str


class Jailor(Char):
    def __init__(self):
        self.name = "jailor"


# NAMED CHARACTERS


# LOCALES

prison = {
    "armory": [
        "weapon cache",
        "armory entrance",
    ],
    "yard": [
        "main yard",
        "yard gates",
    ],
}


@dataclass
class Locale:
    name: str
    listOfItems: list
    listOfGoodEvents: list
    listOfBadEvents: list


class WeaponCache(Locale):
    def __init__(self):
        self.name = "Weapon Cache"
        self.listOfItems = []
        self.listOfGoodEvents = []
        self.listOfBadEvents = []


class WeaponCache(Locale):
    def __init__(self):
        self.name = "Weapon Cache"
        self.listOfItems = []
        self.listOfGoodEvents = []
        self.listOfBadEvents = []


# ITEMS


@dataclass
class Item:
    name: str
    desc: str
    actions: list


@dataclass
class Action:
    name: str
    desc: str
    actionRollTable: dict


class Gun(Item):
    def __init__(self):
        self.name = "Gun"
        self.desc = "This revolver contains six bullets, but it tends to jam"

        class ShootFullClip(Action):
            def __init__(self):
                self.name = "Shoot (Full Clip)"
                self.desc = "you take aim with your finesess and shoot, you can use this once per turn"
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        ["4", "incapicate target"],
                        ["3", "miss"],
                    ],
                }

        class ShootHalfClip(Action):
            def __init__(self):
                self.name = "Shoot (Half Clip)"
                self.desc = "you take aim with your finesess and shoot, you can use this once per turn"
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        ["8", "incapicate target"],
                        ["7", "miss"],
                    ],
                }

        class Reload(Action):
            def __init__(self):
                self.name = "Reload"
                self.desc = "you reload your gun, remove bullets from your inventory"
                self.actionRollTable = {
                    "rollType": "knowledge",
                    "roll": [
                        ["2", "reload succeed"],
                        ["1", "reload failed, try again"],
                    ],
                }

        class Aim(Action):
            def __init__(self):
                self.name = "Aim"
                self.desc = "you aim your gun, allowing an easier time to fire"
                self.actionRollTable = {
                    "rollType": "sanity",
                    "roll": [
                        ["8", "increase speed +2 to your next shoot"],
                        ["4", "increase speed +1 to your next shoot"],
                    ],
                }

        self.actions = [ShootFullClip(), ShootHalfClip(), Reload(), Aim()]


gun = Gun()

# choice = input(f"> {[a.name for a in gun.actions]} ")

# GOOD EVENTS


@dataclass
class GoodEvent:
    name: str


# BAD EVENTS


@dataclass
class BadEvent:
    name: str
