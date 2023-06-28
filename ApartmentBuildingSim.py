import heapq
import random
import os
import jsoneng
from dotenv import load_dotenv
from termcolor import *

jdb = jsoneng.JsonDB()
jdb.create({})










class Char:
    def __init__(self, name):
        self.name = name
        self.state = None
        self.location = None

    def __repr__(self):
        return f"{colored('CHAR:','red')} name:{self.name} state:{self.state} location:{self.location}"

class WaterDrinker(Char):
    def createEvents(self, simTime, futureEventList, chars):
        if self.state == 'idle':
            heapq.heappush(futureEventList, DrinkWater0(simTime + random.randint(1,4)))










class Event:
    def __init__(self, time, chars, ):
        self.time = time
        self.name = name
        self.futureEventList = futureEventList
        self.chars = chars

    def __repr__(self):
        return f"{colored('EVENT:','red')} time:{self.time} name:{self.name}"

    def __lt__(self, other):
        return self.time < other.time
    
class InitCharsEvent(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'init chars')

    def handleEvent(self, futureEventList):
        for c in self.chars:
            c.state = 'idle'
            c.location = 'lobby'
    
class DrinkWater0(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 0: start drinking water')

    def handleEvent(self, futureEventList):
        for c in self.chars:
            c.state = 'stage 0: drink water'
        heapq.heappush(self.futureEventList, DrinkWater1(self.time, self.chars))

class DrinkWater1(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 1: finish drinking water')

    def handleEvent(self, futureEventList):
        for c in self.chars:
            c.state = 'idle'












chars = []
harry = WaterDrinker('Harry')
alice = WaterDrinker('Alice')
chars.append(harry)
chars.append(alice)

fel = []
initCharsEvent = InitCharsEvent(0, chars)
fel.append(initCharsEvent)

simTime = 0
while simTime < 100:
    currEvent = heapq.heappop(fel)
    simTime += currEvent.time

    currEvent.handleEvent(fel)

    for c in chars:
        c.createEvents(simTime, fel, chars)
    
    print(f"time:{simTime} currEvent:{currEvent} chars:{chars}")
