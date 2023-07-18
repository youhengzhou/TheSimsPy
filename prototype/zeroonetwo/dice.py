import random
import sys


def dice(num):
    curr = 0
    total = 0
    for i in range(num):
        curr = random.randint(0, 2)
        input(f"next roll... (0,1,2) at roll {i+1} out of {num}, total = {total}")
        print(f"rolled a:... {curr}")
        total += curr
    print(f"total: {total}")
    return total


dice(int(sys.argv[1]))
