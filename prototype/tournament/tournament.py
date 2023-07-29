import random


class Character:
    def __init__(self, name, skills, stats):
        self.name = name
        self.skills = skills
        self.stats = stats


class Skills:
    def __init__(self, combat, stealth, diplomacy, survival):
        self.combat = combat
        self.stealth = stealth
        self.diplomacy = diplomacy
        self.survival = survival


class Stats:
    def __init__(self, strength, agility, intelligence, charisma):
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.charisma = charisma


def create_character(name):
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
    return Character(name, skills, stats)


def simulate_combat(character1, character2):
    # Simulate combat between two characters
    # You can define your own combat logic here
    character1_score = character1.skills.combat + character1.stats.strength
    character2_score = character2.skills.combat + character2.stats.strength

    if character1_score > character2_score:
        return character1, character2
    elif character2_score > character1_score:
        return character2, character1
    else:
        return None, None


def build_tournament(characters):
    winners = characters[:]
    fights = []
    losers = []

    while len(winners) > 1:
        next_round = []
        for i in range(0, len(winners), 2):
            character1 = winners[i]
            character2 = winners[i + 1]
            fights.append((character1, character2))
            winner, loser = simulate_combat(character1, character2)
            if winner is not None:
                next_round.append(winner)
                losers.append(loser)

        winners = next_round

        if len(winners) > 1:
            ready = input("Are you ready for the next fight? (Press Enter to continue)")
            if ready != "":
                break

    return winners[0] if winners else None, losers, fights


# Example usage
characters = [
    create_character("Character 1"),
    create_character("Character 2"),
    create_character("Character 3"),
    create_character("Character 4"),
]
winner, losers, fights = build_tournament(characters)

if winner:
    print("Tournament Winner:")
    print(f"Name: {winner.name}")
    print(
        f"Skills: Combat={winner.skills.combat}, Stealth={winner.skills.stealth}, Diplomacy={winner.skills.diplomacy}, Survival={winner.skills.survival}"
    )
    print(
        f"Stats: Strength={winner.stats.strength}, Agility={winner.stats.agility}, Intelligence={winner.stats.intelligence}, Charisma={winner.stats.charisma}"
    )
else:
    print("No winner in the tournament.")

print("\nTournament Fights:")
for i, (character1, character2) in enumerate(fights, start=1):
    print(f"\nFight {i}:")
    print(f"{character1.name} vs {character2.name}")
    print(
        f"{character1.name} - Skills: Combat={character1.skills.combat}, Stealth={character1.skills.stealth}, Diplomacy={character1.skills.diplomacy}, Survival={character1.skills.survival}"
    )
    print(
        f"{character2.name} - Skills: Combat={character2.skills.combat}, Stealth={character2.skills.stealth}, Diplomacy={character2.skills.diplomacy}, Survival={character2.skills.survival}"
    )
    print(
        f"{character1.name} - Stats: Strength={character1.stats.strength}, Agility={character1.stats.agility}, Intelligence={character1.stats.intelligence}, Charisma={character1.stats.charisma}"
    )
    print(
        f"{character2.name} - Stats: Strength={character2.stats.strength}, Agility={character2.stats.agility}, Intelligence={character2.stats.intelligence}, Charisma={character2.stats.charisma}"
    )

    ready = input("Are you ready for the next fight? (Press Enter to continue)")
    if ready != "":
        break

    if winner and losers[i - 1]:
        loser = losers[i - 1]  # Get the corresponding loser for the fight
        print(f"\nFight {i} Result:")
        print(f"Winner: {winner.name}")
        print(f"Loser: {loser.name}")
        print(
            f"{winner.name} - Skills: Combat={winner.skills.combat}, Stealth={winner.skills.stealth}, Diplomacy={winner.skills.diplomacy}, Survival={winner.skills.survival}"
        )
        print(
            f"{loser.name} - Skills: Combat={loser.skills.combat}, Stealth={loser.skills.stealth}, Diplomacy={loser.skills.diplomacy}, Survival={loser.skills.survival}"
        )
        print(
            f"{winner.name} - Stats: Strength={winner.stats.strength}, Agility={winner.stats.agility}, Intelligence={winner.stats.intelligence}, Charisma={winner.stats.charisma}"
        )
        print(
            f"{loser.name} - Stats: Strength={loser.stats.strength}, Agility={loser.stats.agility}, Intelligence={loser.stats.intelligence}, Charisma={loser.stats.charisma}"
        )
    else:
        print(f"\nFight {i} Result:")
        print("The fight was a draw.")
