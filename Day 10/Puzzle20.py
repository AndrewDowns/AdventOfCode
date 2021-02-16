import itertools
import math
import operator

def readData():
    data = []
    fh = open("jolt_info.txt")
    for line in fh:
        data.append(int(line.strip()))
    return data

def getDeviceJolt(data):
    next = 0
    for i in range(len(data)):
        current = data[i]
        if i+1==len(data):
            next = current+3
        else:
            next = data[i+1]
    return next

def validStart(item):
    if item[0] != 0 and item[0]<=3:
        return True
    else:
        return False

def isValid(item, device_jolt):
    for i in range(len(item)):
        if i+1 == len(item):
            if device_jolt-item[i]>3:
                return False
        else:
            if item[i+1] - item[i]>3:
                return False

    return True

def getValidSets(data):
    #Slow as fuck method - Don't use
    valid_sets = 0
    for n in range(1, len(data) + 1):
        print(n, " of ", len(data), " : Found ", valid_sets)
        for combination in itertools.combinations(data, n):
            if validStart(combination):
                if isValid(combination, device_jolt):
                    valid_sets += 1

    return valid_sets

def count_arrangements(differences):
    return math.prod(
        (2 ** (len(m) - 1)) - (len(m) == 4)
        for k, g in itertools.groupby(differences)
        if k == 1 and len((m := list(g))) > 1
    )

def get_differences(joltages):
    return list(map(
        operator.sub,
        joltages + [joltages[-1] + 3],
        [0] + joltages
    ))

data = readData()
data.sort()
device_jolt = getDeviceJolt(data)
##print(getValidSets(data), " Valid Sets")
differences = get_differences(data)
print(count_arrangements(differences))






