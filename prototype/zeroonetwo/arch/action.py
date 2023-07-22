from dataclasses import *


@dataclass
class Action:
    name: str
    desc: str
    actionRollTable: dict
