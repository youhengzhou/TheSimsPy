import heapq
import random
import jsoneng
from dotenv import load_dotenv
import os
from lib import FutureEventList

if __name__ == "__main__":
    startSimTime = int(os.environ.get("START_SIM_TIME"))
    endSimTime = int(os.environ.get("END_SIM_TIME"))

    FutureEventList.run_simulation(startSimTime, endSimTime)
