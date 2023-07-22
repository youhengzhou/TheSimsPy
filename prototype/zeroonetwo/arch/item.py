from dataclasses import *
from action import Action


@dataclass
class Item:
    name: str
    desc: str
    actions: list[Action]
