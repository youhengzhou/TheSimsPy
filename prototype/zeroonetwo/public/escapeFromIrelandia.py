from dataclasses import *

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


@dataclass
class Locale:
    name: str


class Prison(Locale):
    def __init__(self):
        self.name = "Irelandia"
        self.prison = {
            "armory": [
                "weapon cache",
                "armory entrance",
            ],
            "yard": [
                "main yard",
                "yard gates",
            ],
        }


# ITEMS


@dataclass
class Item:
    name: str


# GOOD EVENTS


@dataclass
class GoodEvent:
    name: str


# BAD EVENTS


@dataclass
class BadEvent:
    name: str


print(Jailor())
