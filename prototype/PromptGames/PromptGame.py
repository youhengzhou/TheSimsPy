def textToDict(textFile):
    import re

    dictionary = {}
    key = ""

    with open(textFile, "r", encoding="utf-8") as file:
        for line in file:
            line = line.rstrip()  # remove trailing newline character

            # Check if the line ends with a letter indicating a new key
            if re.match(r"[0-9]+[a-z]$", line):
                key = line
                dictionary[key] = []
            else:
                # Add the line to the current key's value list
                dictionary[key].append(line.strip())

    return dictionary


def randomRoll(dictionary):
    import random

    def roll_dice():
        return random.randint(1, 10) - random.randint(1, 6)

    def assign_part(counts, roll):
        current_count = counts.get(roll, 0) + 1
        counts[roll] = current_count
        return f"{roll}{chr(ord('a')+current_count-1)}"

    counts = {}
    out = {}
    roll = 0
    while roll <= 80:
        roll = roll_dice() + roll + 10
        part = assign_part(counts, roll)

        if part in dictionary:
            out[part] = dictionary[part]

    return out


def create(textFile, game):
    import jsoneng

    jdb = jsoneng.JsonDB()
    jdb.create(textToDict(textFile), game)


def play(game, output):
    import jsoneng
    from termcolor import colored

    jdb = jsoneng.JsonDB()
    jdb.create({}, output)

    dictionary = randomRoll(jdb.retrieve(game))

    for i, (k, v) in enumerate(dictionary.items()):
        print(colored(f"prompt {k}", "light_blue"))
        print(colored(v[0], "red"))
        text = input("> ")
        jdb.patch({k: {"prompt": v[0], "answer": text}}, output)


# create("ThousandYearOldVampire.txt", "TYOV")
play("ALifeLived", "Play")
