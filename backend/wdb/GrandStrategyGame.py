import random
import json
from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

# class Char:
#     def __init__(self, charData):
#         self.charData = charData

#     def __repr__(self):
#         return f"Char:{json.dumps(self.charData, indent=2)})"


@dataclass
class Skills:
    martial: int
    larceny: int
    etiquette: int
    education: int
    journey: int
    craft: int
    silver_tongue: int


@dataclass
class Stats:
    fame: int
    body: int
    reputation: int
    wealth: int
    friends: int
    mental: int
    grit: int


@dataclass
class Char:
    name: str
    background: str
    age: int
    skills: Skills
    stats: Stats


def createChar(name, background, age=15):
    skills = Skills(0, 0, 0, 0, 0, 0, 0)
    stats = Stats(0, 0, 0, 0, 0, 0, 0)

    return Char(name, background, age, skills, stats)


@dataclass
class Role:
    type: str
    archetype: list
    history: list
    events: dict
    benefits: list
    quitting: list
    char: Char

    def genArchetype(self):
        return random.choice(self.archetype)

    def genHistory(self):
        out = {}
        years = random.randint(1, 7)
        for year in range(years):
            out["year " + str(self.char.age + year + 1) + " desc"] = self.history[year][
                "desc"
            ]
            if "stats" in self.history[year]:
                for stat in self.history[year]["stats"]:
                    # setattr(
                    #     self.char.skills,
                    #     stat[0],
                    #     getattr(self.char.skills, stat[0]) + stat[1],
                    # ) if stat[0] in [
                    #     field.name for field in fields(Skills)
                    # ] else setattr(
                    #     self.char.stats,
                    #     stat[0],
                    #     getattr(self.char.stats, stat[0]) + stat[1],
                    # )
                    if stat[0] in [field.name for field in fields(Skills)]:
                        setattr(
                            self.char.skills,
                            stat[0],
                            getattr(self.char.skills, stat[0]) + stat[1],
                        )
                    elif stat[0] in [field.name for field in fields(Stats)]:
                        setattr(
                            self.char.stats,
                            stat[0],
                            getattr(self.char.stats, stat[0]) + stat[1],
                        )
            out["year " + str(self.char.age + year + 1) + " event"] = self.genEvent()
        self.char.age += years
        return out

    def genEvent(self):
        out = {}
        ranEvent = random.choice(self.events)
        out["title"] = ranEvent["title"]
        out["desc"] = ranEvent["desc"]
        out["choice"] = random.choice(ranEvent["choices"])["desc"]
        return out

    def genAll(self, char):
        self.char = char
        out = {}
        out["type"] = self.type
        out["archetype"] = self.genArchetype()
        out["history"] = self.genHistory()
        return out


class Soldier(Role):
    def __init__(self):
        self.type = "soldier"
        self.archetype = ["infantry", "skirmisher", "cavalry", "frontier guard"]
        self.history = [
            {
                "desc": "you're still learning the trade",
                "stats": [
                    ["martial", 1],
                ],
            },
            {"desc": "you've seen a lot on the frontline"},
            {
                "desc": "you are a seasoned soldier who has fought on many battlefields across the country",
            },
            {
                "desc": "by now, you're a jaded veteran",
                "stats": [
                    ["martial", 1],
                    ["body", -1],
                ],
            },
            {
                "desc": "your name is quite known among soldiers",
                "stats": [
                    ["body", -1],
                ],
            },
            {
                "desc": "sieges, sabotage, hopeless battles, desperate charges, you've done it all",
                "stats": [
                    ["martial", 1],
                ],
            },
            {
                "desc": "war legend",
                "stats": [
                    ["martial", 1],
                    ["body", -1],
                ],
            },
        ]
        self.events = [
            {
                "title": "sacking",
                "desc": "when the city fell, after a long siege, came the time of savagery. What did you do on this cruel night?",
                "choices": [
                    {
                        "desc": "you took part in the rapes and looting",
                        "stats": [["grit", 1], ["reputation", 1]],
                    },
                    {
                        "desc": "you refused to give in to your vile instincts",
                        "stats": [["reputation", 1], ["mental", -1]],
                    },
                ],
            },
            {
                "title": "smuggling",
                "desc": "you discovered that some of your officers were engaged in illegal smuggling, so you...",
                "choices": [
                    {
                        "desc": "...denounced them to your superiors",
                        "stats": [["reputation", 1], ["grit", -1]],
                    },
                    {
                        "desc": "...kept your tongue, on a condition",
                        "stats": [["wealth", 1]],
                    },
                ],
            },
            {
                "title": "outnumbered",
                "desc": "that was some hell of a battle, you danced with dance that day, how did you survive?",
                "choices": [
                    {
                        "desc": "quick thinking and a lot of tactical insight",
                        "stats": [["martial", 1]],
                    },
                    {
                        "desc": "unshakable will and a last stand with your brothers",
                        "stats": [["fame 1", 1]],
                    },
                ],
            },
            {
                "title": "left for dead",
                "desc": "a blade flashed before your eyes and then the silence, when you woke up, the battle was over, and your brothers gone",
                "choices": [
                    {
                        "desc": "you remained dead to the world and took a new name",
                        "stats": [["QUIT", 1], ["fame", 0]],
                    },
                    {
                        "desc": "you were alive?",
                        "stats": [["fame", 1], ["body", -1]],
                    },
                ],
            },
            {
                "title": "distant lands",
                "desc": "you were sent in an exotic land, far behind the borders of damad, you had many tales to tell after that",
                "choices": [
                    {
                        "desc": "tales of harsh deserts and lethal jungles",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "tales of harsh deserts and lethal jungles",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "mentor",
                "desc": "an old soldier took you under his wing upon noticing your talent for surviving on the battlefield",
                "choices": [
                    {
                        "desc": "despite his age, he was still an amazing swordsman",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "he taught you many things about the places he visited",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "quarrel",
                "desc": "an argument with one of your brothers in arms degenerated into a fight, both of you were whipped",
                "choices": [
                    {
                        "desc": "strangely, this experience made you close friends",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "after that, your rivalry turned into bitter hostility",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "heroism",
                "desc": "you displayed incredible heroism in battle, whether martially or strategically",
                "choices": [
                    {
                        "desc": "that didn't go unoticed",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "your deeds went unnoticed by your superiors",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "wet work",
                "desc": "you took part in a high risk covert operation, far behind enemy lines",
                "choices": [
                    {
                        "desc": "it went smoothly",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "you got captured and tortured",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "winter",
                "desc": "the campaign didn't go well, your regiment got stuck for weeks in teh dead of winter",
                "choices": [
                    {
                        "desc": "you resorted to cannabalism to survive",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "you prayed, again and again",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["brothers-in-arms", "survival", "weapon proficiency"]
        self.quitting = ["promotion", "moving on", "infamy", "captured"]


class Mercenary(Role):
    def __init__(self):
        self.type = "mercenary"
        self.archetype = [
            "the white company",
            "the desert hounds",
            "the blades of the weeping maiden",
            "the black boars",
        ]
        self.history = [
            {
                "desc": "you're making your way through your first battles with the company",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {"desc": "you know everyone in the company"},
            {
                "desc": "you've now travelled far and wide with your battle borthers",
            },
            {
                "desc": "you're a very respected fighter in the company",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "you're a very respected fighter in the company",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "after consultation, you were elected by your brothers as the new captain",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "you've led your brothers through hell, and came back alive",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "camaraderie",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "changing side",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "minor campaign",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "betrayal",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "new recruit",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]


class Officer(Role):
    def __init__(self):
        self.type = "officer"
        self.archetype = [
            "careful",
            "hothead",
            "unorthodox",
            "traditional",
        ]
        self.history = [
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "deserters",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "the child",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "suicide mission",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "dispute",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "long siege",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "war hero",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "civilians",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "tough battle",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "nickname",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "parade",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]


class General(Role):
    def __init__(self):
        self.type = "general"
        self.archetype = [
            "attack",
            "defend",
            "trap",
            "diplomacy",
        ]
        self.history = [
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "invitation",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "speech",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "miracle",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "majesty",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "the prince",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "duel",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "disaster",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "plague",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "unexpected",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "dilemma",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]


class Pilgrim(Role):
    def __init__(self):
        self.type = "pilgrim"
        self.archetype = [
            "east",
            "west",
            "north",
            "south",
        ]
        self.history = [
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "dark place",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "campfire",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "companion",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "despair",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "splendid",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "harsh terrain",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "divine contact",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "horrors",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "misery",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "this is it",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]


class Monk(Role):
    def __init__(self):
        self.type = "monk"
        self.archetype = [
            "redemptiion",
            "spirituality",
            "misanthropy",
            "knowledge",
        ]
        self.history = [
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "mentor",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "teachings",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "occult",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "exorcism",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "journey",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "duty",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "ordeal",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "the child",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "peace",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "brothers",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]


class Priest(Role):
    def __init__(self):
        self.type = "priest"
        self.archetype = [
            "typical",
            "primalist",
            "pantheist",
            "heterodoxy",
        ]
        self.history = [
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "plague",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "temptress",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "disturbing",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "townsfolk",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "vision",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "confession",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "chapel",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "preacher",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "learning",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "orphan",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]


class Inquisitor(Role):
    def __init__(self):
        self.type = "inquisitor"
        self.archetype = [
            "investigator",
            "holy blade",
            "torturer",
            "theologian",
        ]
        self.history = [
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "witch",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "suspect",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "study",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "succubus",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "trial",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "the count",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "accusation",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "ambush",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "torture",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "rival",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]


class ROLE(Role):
    def __init__(self):
        self.type = "ROLE"
        self.archetype = [
            "ARCHETYPE",
            "ARCHETYPE",
            "ARCHETYPE",
            "ARCHETYPE",
        ]
        self.history = [
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
            {
                "desc": "DESC",
                "stats": [
                    ["STAT", 1],
                ],
            },
        ]
        self.events = [
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
            {
                "title": "TITLE",
                "desc": "DESC",
                "choices": [
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                    {
                        "desc": "DESC",
                        "stats": [["STAT", 1], ["STAT", 1]],
                    },
                ],
            },
        ]
        self.benefits = ["TITLE", "TITLE", "TITLE"]
        self.quitting = ["TITLE", "TITLE", "TITLE", "TITLE"]

def gen():
    for i in range(5):
        tom = createChar("char" + str(i), "COMMON", random.randint(16, 26))
        folderName = "test" + str(i)
        jdb.create({}, folderName)

        soldier = Soldier()
        mercenary = Mercenary()
        officer = Officer()
        general = General()
        pilgrim = Pilgrim()
        monk = Monk()
        priest = Priest()
        inquisitor = Inquisitor()

        roleList = [soldier, mercenary, officer, general, pilgrim, monk, priest, inquisitor]
        for j in range(random.randint(1, 5)):
            jdb.i(random.choice(roleList).genAll(tom), folderName)

        jdb.patch(asdict(tom), folderName)

gen()

# sampleOut = {
#     0: {
#         "type": "soldier",
#         "archetype": "infantry",
#         "year1": "you are still learning the trade, martial + 1",
#     }
# }

# class RoleTemplate(Role):
#     roleData = {
#         'type': '',
#         'archetype':
#         ['','','',''],
#         'events':
#         {'': ['',''],
#         '': ['','']},
#         'rewards': ['','','']
#     }
