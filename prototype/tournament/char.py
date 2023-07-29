from dataclasses import dataclass
import random


@dataclass
class Character:
    name: str
    background: str
    age: int
    skills: "Skills"
    stats: "Stats"


@dataclass
class Skills:
    combat: int
    stealth: int
    diplomacy: int
    survival: int


@dataclass
class Stats:
    strength: int
    agility: int
    intelligence: int
    charisma: int


def generate_character():
    name = input("Enter character name: ")
    background = input("Enter character background: ")
    age = random.randint(15, 50)
    skills = Skills(
        combat=random.randint(1, 10),
        stealth=random.randint(1, 10),
        diplomacy=random.randint(1, 10),
        survival=random.randint(1, 10),
    )
    stats = Stats(
        strength=random.randint(1, 10),
        agility=random.randint(1, 10),
        intelligence=random.randint(1, 10),
        charisma=random.randint(1, 10),
    )

    character = Character(name, background, age, skills, stats)
    return character


# Example usage
# new_character = generate_character()
# print("Generated Character:")
# print(f"Name: {new_character.name}")
# print(f"Background: {new_character.background}")
# print(f"Age: {new_character.age}")
# print(f"Skills: Combat={new_character.skills.combat}, Stealth={new_character.skills.stealth}, Diplomacy={new_character.skills.diplomacy}, Survival={new_character.skills.survival}")
# print(f"Stats: Strength={new_character.stats.strength}, Agility={new_character.stats.agility}, Intelligence={new_character.stats.intelligence}, Charisma={new_character.stats.charisma}")

