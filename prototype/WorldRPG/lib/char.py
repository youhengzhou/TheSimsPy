import random
from dataclasses import *


@dataclass
class Action:
    name: str
    desc: str
    actionRollTable: dict


# CHARACTERS

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
    "place": [
        "Ashbourne",
        "Bexhill",
        "Cheltenham",
        "Dorking",
        "Epsom",
        "Farnham",
        "Gillingham",
        "Harrogate",
        "Ilfracombe",
        "Jarrow",
        "Kendal",
        "Louth",
        "Matlock",
        "Newark",
        "Ormskirk",
        "Penzance",
        "Queenborough",
        "Rye",
        "Scarborough",
        "Tewkesbury",
    ],
}


@dataclass
class Char:
    name: str
    desc: str
    actions: list[Action]


humanPost = {
    "civilian": ["serf", "servant", "commoner", "wildmen"],
    "civil": ["laborer", "artisan", "shopkeeper", "banker"],
    "military": ["towne militia", "city guard", "soldier", "knight"],
    "dark": ["thief", "gang member", "assassin", "lieutenant"],
    "science": ["intelligentsia", "student", "researcher", "professor"],
    "occult": ["hobbyist", "journalist", "investigator", "occult member"],
}


class Commoner(Char):
    def __init__(self, gender="male"):
        self.name = (
            f"Commoner {random.choice(names[gender])} {random.choice(names['last'])}"
        )

        self.desc = "commoners are the plentiful backbone of society"

        class Live(Action):
            def __init__(self):
                self.name = "Live"
                self.desc = "commoners tend to be lazy, living a life of simple liesure instead of working"
                self.actionRollTable = {
                    "rollType": "speed",
                    "roll": [
                        [4, "live well"],
                        [3, "live okay"],
                    ],
                }

        self.actions = [
            Live(),
        ]
