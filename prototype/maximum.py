col = {"1": [100, 1], "2": [10, 2]}

print(col.get("1"))


fruitExample = {
    "dict1": {"apple": 3, "banana": 7},
    "dict2": {"orange": 5, "grape": 7},
    "dict3": {"kiwi": 2, "mango": 1},
}

max_key = max(fruitExample, key=lambda k: max(fruitExample[k].values()))


# def getSecond(value):
#     # value = p.get
#     return value[1]


# print(max(col))
# print(max(col, key=getSecond(col.get)))


# print(max_key)
# print(max(col, key=col.get))
