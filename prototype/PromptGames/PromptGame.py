def create(textFile, game):
    import jsoneng

    def textToDict(textFile):
        # for parsing the original TYOV txt file only
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

    jdb = jsoneng.JsonDB()
    jdb.create(textToDict(textFile), game)


def play(game, output):
    """
    Generates a function comment for the given function body in a markdown code block with the correct language syntax.

    Args:
        game (str): The name of the game.
        output (str): The output file path.

    Returns:
        dict: The dictionary containing the prompts and answers.
    """
    import jsoneng
    from termcolor import colored

    def randomRoll(dictionary):
        """
        Generates a dictionary with randomly assigned values based on the rolls of two dice.

        Parameters:
        - dictionary (dict): A dictionary containing the parts and their corresponding values.

        Returns:
        - out (dict): A dictionary containing the randomly assigned parts and their corresponding values.
        """
        import random

        def rollDice():
            return random.randint(1, 10) - random.randint(1, 6)

        def updateRoll(roll, increment=0):
            return rollDice() + roll + increment

        def assignPart(countsOfRoll, roll):
            """
            Assigns a part to a given roll.

            Parameters:
            - counts (dict): A dictionary containing roll as key and the current count as value.
            - roll (any): The roll to assign a part to.

            Returns:
            - str: The assigned part represented by the roll and a letter corresponding to the current count.

            """
            currentCount = countsOfRoll.get(roll, 0) + 1
            countsOfRoll[roll] = currentCount
            return f"{roll}{chr(ord('a')+currentCount-1)}"

        out = {}
        countsOfRoll = {}

        roll = 0
        while roll <= 80:
            roll = updateRoll(roll, 2)
            part = assignPart(countsOfRoll, roll)

            # This code snippet checks if the variable part is a key in the dictionary.
            # If it is, it assigns the corresponding value to the out dictionary with the same key.
            if part in dictionary:
                out[part] = dictionary[part]

        return out

    jdb = jsoneng.JsonDB()
    jdb.create({}, output)

    curr = randomRoll(jdb.retrieve(game))

    q1 = "broad summary of your previous life"
    c1 = "a character you are familiar with"
    c2 = "another character you are familiar with"
    s1 = "a skill you have"
    s2 = "another skill you have"
    r1 = "a resource you have"
    r2 = "another resource you have"
    e1 = "an experience you have relating to two of the things you described"
    i1 = "inciting incident (for TYOV, create an immortal and mark to explain how you became a vampire)"

    preGame = [q1, c1, c2, s1, s2, r1, r2, e1, i1]

    for i in range(len(preGame)):
        print(colored(preGame[i], "red"))
        text = input("> ")
        jdb.patch({i: {"prompt": preGame[i], "answer": text}}, output)

    for i, (k, v) in enumerate(curr.items()):
        print(colored(f"prompt {k}", "light_blue"))
        print(colored(v, "red"))
        text = input("> ")
        jdb.patch({k: {"prompt": v, "answer": text}}, output)


# create("ThousandYearOldVampire.txt", "TYOV")
play("TYOV", "Play")
