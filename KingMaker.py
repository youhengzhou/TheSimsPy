import heapq

class Event:
    def __init__(self, time, event_name):
        self.time = time
        self.event_name = event_name
    
    def __repr__(self):
        return f"EVENT: time:{self.time} chars:{self.chars[0].name} name:{self.name}"

    def __lt__(self, other):
        return self.time < other.time

class EventCreator:
    def __init__(self):
        self.fel = []  # FEL is a heapq queue

    def create_event(self, time, event_name):
        event = Event(time, event_name)
        heapq.heappush(self.fel, (event.time, event))  # Add event to the FEL

    def simulation_cycle(self):
        if self.fel:
            next_event = heapq.heappop(self.fel)[1]  # Get the next event with the least event time
            self.update_sim_time(next_event.time)
            self.handle_event(next_event)

    def update_sim_time(self, time):
        # Update the simulation time based on the next event time
        pass

    def handle_event(self, event):
        # Handle the event by handling the respective state changes to the character and global states
        pass

class EventResolver:
    def __init__(self):
        pass

    def handle_event(self, event):
        # Handle the event by handling the respective state changes to the character and global states
        state_changes = event.get_state_changes()  # Assuming the Event class has a method to get the state changes
        for attribute, change_value in state_changes.items():
            self.update_state(attribute, change_value)

    def update_state(self, attribute, change_value):
        # Update the state based on the attribute and change value
        pass

class Simulation:
    def __init__(self):
        self.sim_time = 0
        self.event_creator = EventCreator()
        self.event_resolver = EventResolver()

    def run(self, max_time):
        while True:
            if self.sim_time > max_time or not self.event_creator.fel:
                break

            next_event = heapq.heappop(self.event_creator.fel)
            self.sim_time = next_event.time
            self.event_resolver.handle_event(next_event)
