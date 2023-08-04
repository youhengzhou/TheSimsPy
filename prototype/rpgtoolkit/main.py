import random
import os
from dataclasses import dataclass, asdict
import jsoneng
from termcolor import colored

from lib.data import Char, Event, Place, view, p_map

jdb = jsoneng.JsonDB({})


def newDay(time, currentPlace):
    newDayData = f"""day: {colored(time, 'red')}
you are in {currentPlace.name}
available actions:
0. rest
1. move
2. events

enter the action you want below"""
    return view(newDayData)


def changeCurrentPlace(time, currentPlace):
    # list neighbors
    out = f"{colored('available neighbors:','red')}\n"
    for i in range(len(currentPlace.neighbors)):
        out += f"{i}. {p_map[currentPlace.neighbors[i]].name}.\n"

    choice = view(out)

    # if neighbor exist
    if choice.isdigit() and 0 <= int(choice) <= len(currentPlace.neighbors) - 1:
        chosen_neighbor = currentPlace.neighbors[int(choice)]
        # view(f"Moving to {p_map[chosen_neighbor].name}...")
        currentPlace = p_map[chosen_neighbor]
    else:
        view("Invalid neighbor choice.", "red")

    return currentPlace


def getEvent(time, currentPlace):
    if currentPlace.events:
        # get event
        currentEvent = random.choice(currentPlace.events)
        currentEvent.action()

        # ask player to describe in diary
        text = view("write down what happened please")
        jdb.patch({time: {"prompt": currentEvent.desc, "answer": text}})
    else:
        view("no available events", "red")


def main(time, currentPlace):
    while True:
        userChoice = newDay(time, currentPlace)

        if userChoice == "exit":
            view("thank you for playing")
            break

        if userChoice == "0":
            pass

        elif userChoice == "1":
            currentPlace = changeCurrentPlace(time, currentPlace)

        elif userChoice == "2":
            getEvent(time, currentPlace)

        else:
            view("invalid choice", "red")

        view("time passes...", "red")
        time += 1


if __name__ == "__main__":
    jdb.p("tyov count", 0)
    main(0, p_map["home"])
