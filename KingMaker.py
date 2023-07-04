import heapq

class GlobalState:
    def __init__(self, global_data: dict):
        self.global_data = global_data

class CharState:
    def __init__(self, char_data: list):
        self.char_data = char_data

class Event:
    def __init__(self, time: int, event_name: str, state_change: list):
        self.time = time
        self.event_name = event_name
        self.state_change = state_change
    
    def __repr__(self):
        return f"EVENT: time:{self.time} name:{self.name}"

    def __lt__(self, other):
        return self.time < other.time

class EventCreator:
    def __init__(self, fel: list, globalState: GlobalState, charState: CharState):
        self.fel = []
        self.globalState = globalState
        self.charState = charState

    def create_event(self, time: int, event_name: str):
        event = Event(time, event_name)
        heapq.heappush(self.fel, (event.time, event))  # Add event to the FEL

class EventResolver:
    def __init__(self, globalState: GlobalState, charState: CharState):
        self.globalState = globalState
        self.charState = charState

    def handle_event(self, event: Event):
        # Handle the event by handling the respective state changes to the character and global states
        state_changes = event.state_change
        for attribute, change_value in state_changes.items():
            self.update_state(attribute, change_value)

    def update_state(self, attribute, change_value):
        # Update the state based on the attribute and change value
        pass

class Simulation:
    def __init__(self, sim_time, fel, global_data, char_data):
        self.sim_time = sim_time
        self.fel = heapq.heapify(fel)
        self.globalState = GlobalState(global_data)
        self.charState = CharState(char_data)
        self.event_creator = EventCreator(self.fel, self.globalState, self.charState)
        self.event_resolver = EventResolver(self.globalState, self.charState)

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
