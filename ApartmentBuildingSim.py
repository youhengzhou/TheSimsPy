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
        return f"CHAR: name:{self.name} state:{self.state} location:{self.location}"
        # return f"{colored('CHAR:','red')} name:{self.name} state:{self.state} location:{self.location}"

class WaterDrinker(Char):
    def createEvents(self, simTime, futureEventList, chars):
        if not any(self in evt.chars for evt in futureEventList):
            if self.state == 'idle':
                heapq.heappush(futureEventList, DrinkWater0(simTime + random.randint(3,5), [self]))
            
            if self.state == 'need to piss':
                heapq.heappush(futureEventList, PissWater0(simTime + random.randint(3,5), [self]))










class Event:
    def __init__(self, time, chars, name):
        self.time = time
        self.name = name
        self.chars = chars

    def __repr__(self):
        return f"EVENT: time:{self.time} chars:{self.chars[0].name} name:{self.name}"

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
        heapq.heappush(futureEventList, DrinkWater1(self.time + random.randint(4,8), self.chars))

class DrinkWater1(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 1: finish drinking water')

    def handleEvent(self, futureEventList):
        for c in self.chars:
            c.state = 'need to piss'

class PissWater0(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 0: start pissing')

    def handleEvent(self, futureEventList):
        for c in self.chars:
            c.state = 'stage 0: pissing'
        heapq.heappush(futureEventList, PissWater1(self.time + random.randint(4,8), self.chars))

class PissWater1(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 1: finish pissing')

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
while simTime < 20:
    currEvent = heapq.heappop(fel)
    simTime = currEvent.time

    currEvent.handleEvent(fel)

    for c in chars:
        c.createEvents(simTime, fel, chars)
    
    print(f"time:{simTime} currEvent:{currEvent} chars:{chars}")

    jdb.i({
        'time': str(simTime),
        'currEvent': str(currEvent),
        'chars': str(chars),
    })

print(fel)
