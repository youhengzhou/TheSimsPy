from dataclasses import dataclass
import heapq
import random


@dataclass
class Monster:
    name: str
    health: int
    strength: int

    def attack(self, player):
        damage = self.strength
        player.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage

    def __lt__(self, other):
        return self.strength < other.strength


@dataclass
class Player:
    name: str
    health: int
    strength: int

    def attack(self, monster):
        damage = self.strength
        monster.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage


@dataclass
class Dungeon:
    name: str
    levels: list
    current_level: int

    def __init__(self, name):
        self.name = name
        self.levels = []
        self.current_level = 0

    def add_level(self, level):
        heapq.heappush(self.levels, level)

    def remove_level(self, level):
        self.levels.remove(level)

    def get_levels(self):
        return self.levels

    def get_level_count(self):
        return len(self.levels)

    def move_to_next_level(self):
        if self.current_level < len(self.levels) - 1:
            self.current_level += 1
            print(f"You have moved to level {self.current_level + 1}.")
        else:
            print("You have reached the final level of the dungeon.")

    def explore_current_level(self):
        level = self.levels[self.current_level]
        if level:
            print(f"You are exploring level {self.current_level + 1}:")
            for monster in level:
                print(f"- {monster.name} (Strength: {monster.strength})")
        else:
            print("There are no monsters in the current level.")

    def encounter_monster(self):
        level = self.levels[self.current_level]
        if level:
            monster = random.choice(level)
            print(
                f"You have encountered a {monster.name} (Strength: {monster.strength})."
            )
            self.start_combat(monster)
        else:
            print("There are no monsters in the current level.")

    def start_combat(self, monster):
        print("Combat started!")
        player = Player("Player 1", 100, 10)
        while player.health > 0 and monster.health > 0:
            print(f"{player.name} health: {player.health}")
            print(f"{monster.name} health: {monster.health}")

            # Player's turn
            player_choice = input("Choose your action (1. Attack, 2. Use item): ")

            if player_choice == "1":
                player.attack(monster)
                print(f"{player.name} attacks {monster.name}!")
            elif player_choice == "2":
                print("Using item...")
                # Implement item usage logic here
            else:
                print("Invalid choice. Try again.")

            # Monster's turn
            monster.attack(player)
            print(f"{monster.name} attacks {player.name}!")

        if player.health <= 0:
            print(f"{player.name} has been defeated. Game over.")
        else:
            print(f"{monster.name} has been defeated. You win!")


# Example usage
player = Player("Player 1", 100, 10)
monsters = [
    [Monster("Goblin", 50, 5)],
    [Monster("Skeleton", 60, 8), Monster("Zombie", 70, 7)],
    [Monster("Orc", 80, 12), Monster("Troll", 100, 15), Monster("Dragon", 150, 20)],
]

dungeon = Dungeon("My Dungeon")
dungeon.add_level(monsters[0])
dungeon.add_level(monsters[1])
dungeon.add_level(monsters[2])

dungeon.explore_current_level()
dungeon.encounter_monster()
