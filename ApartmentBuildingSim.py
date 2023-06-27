import heapq
import random
import jsoneng
from dotenv import load_dotenv
import os

jdb = jsoneng.JsonDB()
jdb.create({})

import random
import heapq

class Character:
    def __init__(self, name):
        self.name = name
        self.state = "idling"

    def __repr__(self):
        return self.name

class Event:
    def __init__(self, time, action, participants=None):
        self.time = time
        self.action = action
        self.participants = participants if participants is not None else []

    def __lt__(self, other):
        return self.time < other.time

class SimWorld:
    FutureEventList = []
    