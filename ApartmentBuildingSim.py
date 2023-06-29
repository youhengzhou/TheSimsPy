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
        self.pissCounter = 0

    def __repr__(self):
        return f"CHAR: name:{self.name} state:{self.state} location:{self.location}"
        # return f"{colored('CHAR:','red')} name:{self.name} state:{self.state} location:{self.location}"

class WaterDrinker(Char):
    def createEvents(self, simTime, futureEventList, chars):
        if not any(self in evt.chars for evt in futureEventList):
            if self.state == 'idle':
                heapq.heappush(futureEventList, DrinkWater0(simTime + random.randint(1,2), [self]))
            
            if self.state == 'need to piss':
                heapq.heappush(futureEventList, PissWater0(simTime + random.randint(1,2), [self]))
                self.pissCounter += 1

class Event:
    def __init__(self, time, chars, name):
        self.time = time
        self.name = name
        self.chars = chars

    def __repr__(self):
        return f"EVENT: time:{self.time} chars:{self.chars[0].name} name:{self.name}"

    def __lt__(self, other):
        return self.time < other.time
    
    def setCharacters(self, state=None, location=None):
      for c in self.chars:
         if state:
            c.state = state
         if location:
            c.location = location
    
    def handleEvent(self, futureEventList):
      raise NotImplementedError()
    
class InitCharsEvent(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'init chars')

    def handleEvent(self, futureEventList):
        self.setCharacters('idle', 'lobby')
    
class DrinkWater0(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 0: start drinking water')

    def handleEvent(self, futureEventList):
        self.setCharacters('stage 0: drink water')
        heapq.heappush(futureEventList, DrinkWater1(self.time + random.randint(1,50), self.chars))

class DrinkWater1(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 1: finish drinking water')

    def handleEvent(self, futureEventList):
        self.setCharacters('need to piss')

class PissWater0(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 0: start pissing')

    def handleEvent(self, futureEventList):
        self.setCharacters('stage 0: pissing')
        heapq.heappush(futureEventList, PissWater1(self.time + random.randint(1,50), self.chars))

class PissWater1(Event):
    def __init__(self, time, chars):
        super().__init__(time, chars, 'stage 1: finish pissing')

    def handleEvent(self, futureEventList):
        self.setCharacters('idle')

chars = []
harry = WaterDrinker('Harry')
alice = WaterDrinker('Alice')
sally = WaterDrinker('Sally')
david = WaterDrinker('David')
chars.append(harry)
chars.append(alice)
chars.append(sally)
chars.append(david)

fel = []
initCharsEvent = InitCharsEvent(0, chars)
fel.append(initCharsEvent)

simTime = 0
while simTime < 1000:
    currEvent = heapq.heappop(fel)
    simTime = currEvent.time

    currEvent.handleEvent(fel)

    random.shuffle(chars)
    for c in chars:
        c.createEvents(simTime, fel, chars)
    
    print(f"time:{simTime} currEvent:{currEvent} chars:{chars}")

    jdb.i({
        'time': str(simTime),
        'currEvent': str(currEvent.name),
        'chars': str(currEvent.chars[0].name),
    })

print(fel)

print(f"harry {harry.pissCounter}")
print(f"alice {alice.pissCounter}")
print(f"sally {sally.pissCounter}")
print(f"david {david.pissCounter}")
