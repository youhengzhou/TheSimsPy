from dataclasses import dataclass, asdict
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


@dataclass
class Char:
    name: str
    role: str
    desc: str
    skills: list


@dataclass
class Skill:
    name: str
    rolltable: dict


@dataclass
class Place:
    name: str
    rolltable: dict
    neighbors: list


firesword = Skill("firesword", {"close range": 10})
rifle = Skill("rifle", {"close range": 5, "mid range": 5})


waterfountain = Place("water fountain", {"close range": 10, "mid range": 10}, [])
square = Place("square", {"close range": 10, "mid range": 10}, [])

park = [waterfountain, square]

# for place in park:
#     for otherPlace in park:
#         if place != otherPlace:
#             place.neighbors.append(otherPlace)

# jdb.p(asdict(square))
