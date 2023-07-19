from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

# ESCAPE FROM IRELANDIA


# ITEMS


@dataclass
class Action:
    name: str
    desc: str
    actionRollTable: dict


@dataclass
class Item:
    name: str
    desc: str
    actions: list[Action]


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


# CHARACTERS


@dataclass
class Char:
    name: str
    desc: str
    listOfItems: list[Item]
    actions: list[Action]


class Jailor(Char):
    def __init__(self):
        self.name = "Jailor"
        self.desc = "a typical jailor, they might not want to be there, just there for a paycheck, but they still do their jobs"
        self.listOfItems = [Gun()]

        class Patrol(Action):
            def __init__(self):
                self.name = "Patrol"
                self.desc = "the jailor patrols the area, they check for you"
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        ["4", "found you"],
                        ["3", "miss you"],
                    ],
                }

        class CallBackup(Action):
            def __init__(self):
                self.name = "Call Backup"
                self.desc = "calls for backup, get some extra weapons or help"
                self.actionRollTable = {
                    "rollType": "sanity",
                    "roll": [
                        ["6", "they receive extra weapons and help"],
                        ["4", "they only receive extra weapons"],
                        ["3", "nobody comes to help"],
                    ],
                }

        self.actions = [Patrol(), CallBackup()]


# GOOD EVENTS


@dataclass
class GoodEvent:
    name: str
    desc: str
    eventRollTable: dict
    listOfItems: list[Item]
    listOfChars: list[Char]


# BAD EVENTS


@dataclass
class BadEvent:
    name: str
    desc: str
    eventRollTable: dict
    listOfItems: list[Item]
    listOfChars: list[Char]


class Patrol(BadEvent):
    def __init__(self):
        self.name = "Patrol"
        self.desc = "a patrol of some guards came over, roll to see the guards you get"

        self.eventRollTable = {
            "rollType": "speed",
            "roll": [
                ["6", "no guard found you"],
                ["4", "one guard found you"],
                ["3", "lots of guards found you (d4)"],
            ],
        }

        self.listOfItems = []
        self.listOfChars = [Jailor()]


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
    localeName: str
    desc: str
    listOfItems: list[Item]
    listOfChars: list[Char]
    listOfGoodEvents: list[GoodEvent]
    listOfBadEvents: list[BadEvent]


@dataclass
class Biome:
    biomeName: str
    desc: str
    locales: list[Locale]


@dataclass
class Overworld:
    overworldName: str
    desc: str
    biomes: list[Biome]


class Prison(Overworld):
    def __init__(self):
        self.overworldName = "Imperial Irelandia Prison"
        self.desc = "none shall leave here without penance"

        class Armories(Biome):
            def __init__(self):
                self.biomeName = "Armory Section"
                self.desc = "the armory section, guns and lots of guards patrolling"

                class WeaponCache(Locale):
                    def __init__(self):
                        self.localeName = "Weapon Cache"
                        self.desc = "lots of weapons here"

                        self.listOfItems = [Gun()]
                        self.listOfChars = [Jailor()]
                        self.listOfGoodEvents = []
                        self.listOfBadEvents = [Patrol()]

                class ArmoryEntrance(Locale):
                    def __init__(self):
                        self.localeName = "Armory Entrance"
                        self.desc = "lots of guards patrolling the entrance"

                        self.listOfItems = []
                        self.listOfChars = [Jailor()]
                        self.listOfGoodEvents = []
                        self.listOfBadEvents = [Patrol()]

                self.locales = [WeaponCache(), ArmoryEntrance()]

        self.biomes = [Armories()]


p = Prison()

jdb.patch(asdict(p))
