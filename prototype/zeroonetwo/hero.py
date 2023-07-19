import random
import heapq
from dataclasses import *
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})

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

humanPre = {
    # "type": ["lyonian", "falconian", "borderlander", "draconian", "tigian"],
    # "name": ["common", "archaic", "uncommon", "noble"],
    "look": ["plain faced", "soft", "attractive", "stern"],
    "build": ["normal build", "small", "fit", "lean"],
    "style": ["incognito", "simple", "stylish", "extravagant"],
}

humanPost = {
    "civilian": ["serf", "servant", "commoner", "wildmen"],
    "civil": ["laborer", "artisan", "shopkeeper", "banker"],
    "military": ["towne militia", "city guard", "soldier", "knight"],
    "dark": ["thief", "gang member", "assassin", "lieutenant"],
    "science": ["intelligentsia", "student", "researcher", "professor"],
    "occult": ["hobbyist", "journalist", "investigator", "occult member"],
}

clothingPreCommon = {
    "pattern": ["sport", "huntsman", "urban", "fine"],
    "adjective": [
        "ironed",
        "clean",
        "dirty",
        "old fashioned",
        "expensive",
        "cheap",
        "old",
        "comfortable",
        "normal",
    ],
}


clothingPostCommon = {
    "male": [
        "vest and shirt",
        "dress shirt",
        "long shirt",
        "shirt and sweater",
        "coat and vest",
        "jacket and vest",
        "jacket and shirt",
        "long jacket",
        "short jacket",
        "robe",
        "tuxedo",
    ],
    "female": [
        "sundress",
        "long dress",
        "vest and shirt",
        "elegant coat",
        "long coat",
        "evening dress",
        "cocktail dress",
        "formal dress",
        "short dress",
    ],
}

clothingPostRich = {"top": ["tuxedo", "dress shirt", "long shirt", "vest", "jacket"]}


@dataclass
class Hero:
    gender: str
    name: str
    home: str
    role: str
    clothing: str
    grit: int
    speed: int
    knowledge: int
    sanity: int
    items: list

    def __init__(self):
        self.grit = 0
        self.speed = 0
        self.knowledge = 0
        self.sanity = 0
        self.items = []

        if random.randint(0, 1) == 0:
            self.gender = "Mr"
            name = random.choice(names["male"])
            self.grit += random.randint(2, 4)
            self.knowledge += random.randint(0, 2)
        else:
            self.gender = "Miss"
            name = random.choice(names["female"])
            self.speed += random.randint(0, 2)
            self.sanity += random.randint(2, 4)

        lastname = random.choice(names["last"])
        self.name = f"{name} {lastname}"

        home = random.choice(names["place"])
        self.home = home

        archetype = random.choice(list(humanPost.keys()))

        if archetype == "military":
            self.grit += random.randint(2, 4)

        if archetype == "dark":
            self.speed += random.randint(2, 4)

        if archetype == "science":
            self.knowledge += random.randint(2, 4)

        if archetype == "occult":
            self.sanity += random.randint(2, 4)

        role = comb(humanPre, random.choice(humanPost[archetype]))
        self.role = role

        if self.gender == "Mr":
            clothing = comb(
                clothingPreCommon, random.choice(clothingPostCommon["male"])
            )
        else:
            clothing = comb(
                clothingPreCommon, random.choice(clothingPostCommon["male"])
            )

        self.clothing = clothing

        self.grit += random.randint(1, 2)
        self.speed += random.randint(1, 2)
        self.knowledge += random.randint(1, 2)
        self.sanity += random.randint(1, 2)

        # from lib import items

        # self.items.append(random.choice(random.choice(items.items)))


def getString(dictionary):
    return random.choice(dictionary[random.choice(list(dictionary.keys()))])


def comb(one, two):
    if type(one) != dict:
        return f"{one} {getString(two)}"
    elif type(two) != dict:
        return f"{getString(one)} {two}"
    else:
        return f"{getString(one)} {getString(two)}"


jdb.create({})
for i in range(4):
    h = Hero()
    jdb.i(dict(asdict(h)))
