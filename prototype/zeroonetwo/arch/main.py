from dataclasses import dataclass
from action import *
from item import *
from char import *
import locale


class Overworld(locale.World):
    def __init__(self):
        self.worldName = "Earth Overworld"
        self.desc = "lush, green, and blue"
