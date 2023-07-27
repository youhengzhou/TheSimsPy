from collections import defaultdict

nums = [1, 1, 1, 2, 2, 3]
k = 2


freqDict = defaultdict(int)

for n in nums:
    freqDict[n] += 1

out = []
while k > 0:
    nextKey = max(freqDict, key=lambda k: freqDict[k])
    out.append(nextKey)
    freqDict.pop(nextKey)
    k -= 1

print(freqDict)
print(out)
