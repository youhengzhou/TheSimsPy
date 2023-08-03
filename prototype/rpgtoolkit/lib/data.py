import random
from dataclasses import dataclass, asdict


@dataclass
class Char:
    name: str
    role: str
    authenciticy: int
    resolve: int
    inspiration: int
    personality: int


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
