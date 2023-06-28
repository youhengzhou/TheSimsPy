import heapq
import random
import queue
from termcolor import *
from dotenv import load_dotenv

load_dotenv()

def organize_event_sequence(event, chillEventProbability):
    """Bomi Log:
    This is an entry point toll gate for the simulation so that we can have a way of keeping track of what has happened so that new
    event have a chance to take place
    """
    event_queue = queue.Queue()
    if event_queue.empty():
        print(f"{event} has already happpend, lets try something else")
    else:
        while not event_queue.empty():
            count = event_queue.get()
            total = 0
            print(f"{event} Just Occured")
            for x in range(count):
              total += 1
            print(f" {name} has a probability of now occuring is {chillEventProbability}% of the simulation run time")
def get_next_event(chillEvents, sweatyEvents, chillEventProbability):
    if random.randint(1, 100) < chillEventProbability:
        return random.choice(chillEvents)
    return random.choice(sweatyEvents)

def run_simulation(startSimTime, endSimTime):
    simTime = startSimTime
    worldTension = 0
    futureEventList = []

    cprint(f"{'sim time'}, {'world tension'}, {'sim event'}",'yellow')

    while simTime < endSimTime:
        # create events
        # events = ['sunny day','rainy day','heavy frost','dust storm','clear day','meteor shower','auroras']
        chillEvents = ['denmark invents lego']
        sweatyEvents = ['increased housing price','increaed taxes']

        newTime = simTime + random.randint(1,25)
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
            worldTension += random.randint(-5,10)
        else:
            worldTension += random.randint(1,10)

        simTime = currTime
