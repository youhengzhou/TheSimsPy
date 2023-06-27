import heapq
import random
import jsoneng
from dotenv import load_dotenv
import os

import CharGen
import PlaceGen
import RoleGen

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

class ElevatorWorld:
    def __init__(self):
        self.characters = []
        self.events = []
        self.current_time = 0

    def add_character(self, character):
        self.characters.append(character)

    def add_event(self, event):
        heapq.heappush(self.events, event)

    def idle(self, character):
        character.state = "idling"
        print(f"{character.name} is idling.")

    def speak(self, character1, character2):
        if character1.state == "idling" and character2.state == "idling":
            character1.state = "speaking"
            character2.state = "speaking"
            duration = random.randint(3, 8)
            end_time = self.current_time + duration
            end_event = Event(end_time, self.end_speak, participants=[character1, character2])
            self.add_event(end_event)
            print(f"{character1.name} and {character2.name} are speaking for {duration} seconds.")

    def end_speak(self, character1, character2):
        character1.state = "idling"
        character2.state = "idling"
        print(f"{character1.name} and {character2.name} have finished speaking.")

    def simulate(self, duration):
        end_time = self.current_time + duration
        while self.current_time < end_time:
            if not self.events:
                break

            current_event = heapq.heappop(self.events)
            self.current_time = current_event.time

            if current_event.action == "speak":
                character1, character2 = current_event.participants
                self.speak(character1, character2)
            elif current_event.action == "end_speak":
                character1, character2 = current_event.participants
                self.end_speak(character1, character2)
            elif current_event.action == "idle":
                character = current_event.participants
                self.idle(character)
            
            # Generate new events
            for character in self.characters:
                if character.state == "idling":
                    # Speaking event
                    if random.random() < 0.2:
                        other_character = random.choice(self.characters)
                        if other_character != character and other_character.state == "idling":
                            duration = random.randint(3, 8)
                            time = self.current_time + duration
                            event = Event(time, "speak", participants=[character, other_character])
                            self.add_event(event)
                    # Eating event
                    if random.random() < 0.05:
                        duration = random.randint(5, 15)
                        time = self.current_time + duration
                        event = Event(time, "idle", participants=character)
                        self.add_event(event)
                    # Sleeping event
                    if random.random() < 0.01:
                        duration = random.randint(10, 30)
                        time = self.current_time + duration
                        event = Event(time, "idle", participants=character)
                        self.add_event(event)

            print(self.current_time)

elevator_world = ElevatorWorld()

# Create characters
character1 = Character("Alice")
character2 = Character("Bob")
character3 = Character("Charlie")

# Add characters to the elevator world
elevator_world.add_character(character1)
elevator_world.add_character(character2)
elevator_world.add_character(character3)

# Generate initial idle events for characters
for character in elevator_world.characters:
    event = Event(elevator_world.current_time, "idle", participants=character)
    elevator_world.add_event(event)

# Simulate the elevator world for a duration of 60 seconds
elevator_world.simulate(60)
