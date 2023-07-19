import random
import sys


def dice(num):
    if num == 0:
        print(
            "0: dead, 1: wounded, 2: injured, 3: fatigued, 4: layman, 5: trained, 6: veteran, 7: master"
        )
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
