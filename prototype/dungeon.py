import random
from dataclasses import dataclass
import heapq
import jsoneng

jdb = jsoneng.JsonDB()
jdb.create({})


@dataclass
class Monster:
    name: str
    strength: int

    def __init__(self, name, strength):
        self.name = name
        self.strength = strength

    def __lt__(self, other):
        return self.strength < other.strength


@dataclass
class Room:
    name: str
    monsters: list

    def __init__(self, name):
        self.name = name
        self.monsters = []

    def add_monster(self, monster):
        self.monsters.append(monster)

    def remove_monster(self, monster):
        self.monsters.remove(monster)

    def get_monsters(self):
        return self.monsters


@dataclass
class Level:
    name: str
    rooms: list

    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def remove_room(self, room):
        self.rooms.remove(room)

    def get_rooms(self):
        return self.rooms


@dataclass
class Dungeon:
    name: str
    levels: list

    def __init__(self, name):
        self.name = name
        self.levels = []

    def add_level(self, level):
        self.levels.append(level)

    def remove_level(self, level):
        self.levels.remove(level)

    def get_levels(self):
        return self.levels

    def get_level_count(self):
        return len(self.levels)


dungeon = Dungeon("Dark Dungeon")

level1 = Level("Level 1")
level2 = Level("Level 2")
level3 = Level("Level 3")

room1 = Room("Room 1")
room2 = Room("Room 2")
room3 = Room("Room 3")
room4 = Room("Room 4")
room5 = Room("Room 5")
room6 = Room("Room 6")

monster1 = Monster("Goblin", 5)
monster2 = Monster("Skeleton", 3)
monster3 = Monster("Orc", 7)
monster4 = Monster("Zombie", 4)
monster5 = Monster("Dragon", 10)

rooms = [room1, room2, room3, room4, room5, room6]
monsters = [monster1, monster2, monster3, monster4, monster5]

random.shuffle(rooms)
random.shuffle(monsters)

for i in range(len(rooms)):
    room = rooms[i]
    monster = monsters[i % len(monsters)]
    room.add_monster(monster)
    level1.add_room(room)

dungeon.add_level(level1)

for _ in range(2):
    level = Level(f"Level {_ + 2}")
    random.shuffle(rooms)
    for i in range(len(rooms)):
        room = rooms[i]
        monster = monsters[i % len(monsters)]
        room.add_monster(monster)
        level.add_room(room)
    dungeon.add_level(level)

for level in dungeon.get_levels():
    print(level.name)
    for room in level.get_rooms():
        print(f"- {room.name}")
        for monster in room.get_monsters():
            print(f"  - {monster.name} (Strength: {monster.strength}")

for level in dungeon.get_levels():
    jdb.i(str(level))