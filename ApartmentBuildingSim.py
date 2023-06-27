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
        self.state = "idle"
        self.location = None

    def __repr__(self):
        return f"{self.name} is {self.state} at {self.location}"

class Event:
    def __init__(self, time, participants=None):
        self.time = time
        self.name = None
        self.participants = participants if participants is not None else []
    
    def __repr__(self):
        return f"{self.time} {self.name}"

    def __lt__(self, other):
        return self.time < other.time
    
class InitCharacters(Event):
    def __init__(self, time, participants):
        super(InitCharacters, self).__init__(time, participants)
        self.name = 'init chars'

    def handleEvent(self):
        for c in self.participants:
            c.location = 'lobby'
    
class DrinkWater(Event):
    def __init__(self, time, participants):
        super(DrinkWater, self).__init__(time, participants)
        self.name = 'drink water'

    def handleEvent(self):
        self.name = 'drink water'
        for c in self.participants:
            c.state = 'drinking'

class SimState:
    def __init__(self):
        self.characters = []

class SimWorld:
    def __init__(self, endSimTime):
        self.simTime = 0
        self.endSimTime = endSimTime
        self.futureEventList = []
        self.simState = SimState()
        
    def run(self):
        while self.simTime < self.endSimTime:
            currEvent = heapq.heappop(self.futureEventList)

            currEvent.handleEvent()

            for c in self.simState.characters:
                c.createEvents(self.futureEventList)


harry = Character('harry')
alice = Character('alice')
d = InitCharacters(10,[harry,alice])
d1 = DrinkWater(1,[harry,alice])
d2 = DrinkWater(2,[harry,alice])
d3 = DrinkWater(3,[harry,alice])

fel = []

heapq.heappush(fel, d3)
heapq.heappush(fel, d2)
heapq.heappush(fel, d1)

print(f"fel {fel}")

print(d)

print(harry)
print(alice)


