import heapq
import random
import jsoneng
from dotenv import load_dotenv
import os

load_dotenv()

# jdb = jsoneng.JsonDB('game')

# jdb.create({'hello':'world'})

def get_next_event(chillEvents, sweatyEvents, chillEventProbability):
    if random.randint(1, 100) < chillEventProbability:
        return random.choice(chillEvents)
    return random.choice(sweatyEvents)

def run_simulation(startSimTime, endSimTime):
    simTime = startSimTime
    worldTension = 0
    futureEventList = []

    print(f"{'sim time'}, {'world tension'}, {'sim event'}")

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
        print(f"{currTime} - {worldTension} - {currEvent}")

        if currEvent in chillEvents:
            worldTension += random.randint(-5,10)
        else:
            worldTension += random.randint(1,10)

        simTime = currTime


if __name__ == "__main__":
    startSimTime = int(os.environ.get("START_SIM_TIME"))
    endSimTime = int(os.environ.get("END_SIM_TIME"))

    run_simulation(startSimTime, endSimTime)
