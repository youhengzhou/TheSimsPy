import random
from dataclasses import *

names = {
    "male": [
        "Alfred",
        "Arthur",
        "Benjamin",
        "Charles",
        "Edgar",
        "Edmund",
        "Ernest",
        "Frederick",
        "George",
        "Harold",
        "Herbert",
        "Leonard",
        "Lionel",
        "Percy",
        "Reginald",
        "Sidney",
        "Stanley",
        "Thomas",
        "Walter",
        "Wilfred",
    ],
    "female": [
        "Ada",
        "Agnes",
        "Alice",
        "Amelia",
        "Beatrice",
        "Catherine",
        "Charlotte",
        "Clara",
        "Edith",
        "Eleanor",
        "Elizabeth",
        "Emma",
        "Florence",
        "Frances",
        "Grace",
        "Harriet",
        "Isabella",
        "Jane",
        "Louisa",
        "Mary",
    ],
    "last": [
        "Smith",
        "Johnson",
        "Williams",
        "Brown",
        "Jones",
        "Miller",
        "Davis",
        "Wilson",
        "Taylor",
        "Clark",
        "Hall",
        "Lee",
        "Allen",
        "Young",
        "Walker",
        "Wright",
        "Morris",
        "King",
        "Carter",
        "Baker",
    ],
}

humanPost = {
    "civilian": ["serf", "servant", "commoner", "wildmen"],
    "civil": ["laborer", "artisan", "shopkeeper", "banker"],
    "military": ["towne militia", "city guard", "soldier", "knight"],
    "dark": ["thief", "gang member", "assassin", "lieutenant"],
    "science": ["intelligentsia", "student", "researcher", "professor"],
    "occult": ["hobbyist", "journalist", "investigator", "occult member"],
}


@dataclass
class CharDesc:
    name: str
    desc: str

    def __init__(self, type, name, desc=""):
        self.name = f"{type} {name}"
        self.desc = ""


@dataclass
class Char:
    desc: CharDesc


@dataclass
class Ruler:
    def __init__(self, type):
        self.desc = CharDesc(
            type, f"{random.choice(names['male'])} {random.choice(names['last'])}"
        )
