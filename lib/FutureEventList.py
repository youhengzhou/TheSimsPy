import heapq
import random
from termcolor import *
from dotenv import load_dotenv

load_dotenv()


def get_next_event(chillEvents, sweatyEvents, chillEventProbability):
    if random.randint(1, 100) < chillEventProbability:
        return random.choice(chillEvents)
    return random.choice(sweatyEvents)


def run_simulation(startSimTime, endSimTime):
    simTime = startSimTime
    worldTension = 0
    futureEventList = []

    cprint(f"{'sim time'}, {'world tension'}, {'sim event'}", "yellow")

    while simTime < endSimTime:
        # create events
        # events = ['sunny day','rainy day','heavy frost','dust storm','clear day','meteor shower','auroras']
        chillEvents = ["denmark invents lego"]
        sweatyEvents = ["increased housing price", "increaed taxes"]

        newTime = simTime + random.randint(1, 25)
        if worldTension < 10:
            # probability of 75% for chill event
            chillEventProbability = 75
        else:
            # probability of 90% for sweaty event
            chillEventProbability = 10

        newEvent = get_next_event(chillEvents, sweatyEvents, chillEventProbability)

        heapq.heappush(futureEventList, [newTime, newEvent])

        # pop next event
        currTime, currEvent = heapq.heappop(futureEventList)

        # handle events
        print(f"{colored(currTime,'red')} - {worldTension} - {currEvent}")

        if currEvent in chillEvents:
            worldTension += random.randint(-5, 10)
        else:
            worldTension += random.randint(1, 10)

        simTime = currTime
