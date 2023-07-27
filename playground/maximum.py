col = {"1": [100, 1], "2": [10, 2]}

print(col.get("1"))


def getKey(key):
    return col[key][1]


max_col = max(col, key=getKey)

print(max_col)


print("---fruit example---")

fruitExample = {
    "dict1": {"apple": 3, "banana": 7},
    "dict2": {"orange": 5, "grape": 7},
    "dict3": {"kiwi": 2, "mango": 1},
}

print(max(fruitExample))
a = fruitExample["dict1"].values()
b = fruitExample["dict2"].values()
c = fruitExample["dict3"].values()

print(a)
# print(max(a, b, c))
maxt = max(fruitExample, key=lambda k: max(fruitExample[k].values()))

print(maxt)

# max_key = max(fruitExample, key=lambda k: max(fruitExample[k].values()))


# def getSecond(value):
#     # value = p.get
#     return value[1]


# print(max(col))
# print(max(col, key=getSecond(col.get)))


# print(max_key)
# print(max(col, key=col.get))


def func1(data):
    return data


def func2(data):
    return data


def checkCond(cond, data):
    if cond == 0:
        func1(data)
    if cond == 1:
        func2(data)
