# 1D grand strategy simulator game

# eras, mythical, bronze, iron, steel, gunpowder
    # each era can have random amount of time (historical events)

# great figures 1-5 (characters)

# civs (cultures)

# important places (cities, battlefields, monuments)

import heapq

class GlobalData:
    def __init__(self, globalData: dict):
        self.globalData = globalData

sampleGlobalData = GlobalData({'worldTension':0})

class Character:
    def __init__(self, name, charData, charState):
        self.name = name
        self.charData = charData
        self.charState = charState

sampleCharacter = Character('tom',{'combat':10,'speech':10,'craft':10},'IDLE')

class CharsData:
    def __init__(self, charsData: list):
        self.charsData = charsData

class Event:
    def __init__(self, time: int, eventName: str, stateChanges: list):
        self.time = time
        self.eventName = eventName
        self.stateChanges = stateChanges
    
    def __repr__(self):
        return f"Event.time:{self.time} Event.name:{self.eventName}"

    def __lt__(self, other):
        return self.time < other.time

class EventCreator:
    def __init__(self, fel: list, globalData: GlobalData, charData: CharsData):
        self.fel = []
        self.globalData = globalData
        self.charData = charData

    def create_event(self, time: int, eventName: str):
        event = Event(time, eventName)
        heapq.heappush(self.fel, (event.time, event))  # Add event to the FEL

class EventResolver:
    def __init__(self, globalData: GlobalData, charData: CharsData):
        self.globalData = globalData
        self.charData = charData

    def handle_event(self, event: Event):
        # Handle the event by handling the respective state changes to the character and global states
        stateChangess = event.stateChanges
        for attribute, change_value in stateChangess.items():
            self.update_state(attribute, change_value)

    def update_state(self, attribute, change_value):
        # Update the state based on the attribute and change value
        pass

class Simulation:
    def __init__(self, sim_time, fel, global_data, char_data):
        self.sim_time = sim_time
        self.fel = heapq.heapify(fel)
        self.globalData = GlobalData(global_data)
        self.charData = CharsData(char_data)
        self.event_creator = EventCreator(self.fel, self.globalData, self.charData)
        self.event_resolver = EventResolver(self.globalData, self.charData)

    def run(self, max_time: int):
        while True:
            if self.sim_time > max_time or not self.event_creator.fel:
                break
            self.event_creator.create_event()
            next_event = heapq.heappop(self.event_creator.fel)
            self.sim_time = next_event.time
            self.event_resolver.handle_event(next_event)

sim = Simulation(0, [], {}, [])
sim.run(10)
