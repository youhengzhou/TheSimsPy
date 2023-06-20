import heapq
import random
import jsoneng

# jdb = jsoneng.JsonDB('game')

# jdb.create({'hello':'world'})

simTime = 1900
worldTension = 0
futureEventList = []

print(f"{'sim time'}, {'world tension'}, {'sim event'}")

while simTime < 2000:
    # create events
    # events = ['sunny day','rainy day','heavy frost','dust storm','clear day','meteor shower','auroras']
    chillEvents = ['denmark invents lego']
    sweatyEvents = ['increased housing price','increaed taxes']

    newTime = simTime + random.randint(1,25)
    if worldTension < 10:
        if random.randint(1,100) < 75:
            newEvent = random.choice(chillEvents)
        else:
            newEvent = random.choice(sweatyEvents)
    else:
        if random.randint(1,100) < 90:
            newEvent = random.choice(sweatyEvents)
        else:
            newEvent = random.choice(chillEvents)

    heapq.heappush(futureEventList, [newTime, newEvent])

    # pop next event
    currTime, currEvent = heapq.heappop(futureEventList)

    # handle events
    print(f"{currTime},          {worldTension},               {currEvent}")

    if currEvent in chillEvents:
        worldTension += random.randint(-5,10)
    else:
        worldTension += random.randint(1,10)

    simTime = currTime

# print(random.randint(0,1))

# while simTime < 1000:
