import random
import sys


def dice(num):
    if num == 0:
        print(
            "0: dead, 1: wounded, 2: injured, 3: fatigued, 4: layman, 5: trained, 6: veteran, 7: master"
        )
        return
    out = random.randint(1, num)
    print(f"d{num}: {out}")
    return out


dice(int(sys.argv[1]))
