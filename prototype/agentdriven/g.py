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


firesword = Skill("firesword", {"close range": 10})
rifle = Skill("rifle", {"close range": 5, "mid range": 5})
