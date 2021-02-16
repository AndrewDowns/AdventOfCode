def readData():
    data = []
    fh = open("jolt_info.txt")
    for line in fh:
        data.append(int(line.strip()))
    return data

def combineAdapters(data):
    jolt_differences = dict()
    jolt_differences["1"] = 0
    jolt_differences["3"] = 0

    data.sort()

    if data[0] == 1:
        jolt_differences["1"]+=1
    elif data[0] == 3:
        jolt_differences["3"]+=1

    for i in range(len(data)):
        current = data[i]
        if i+1==len(data):
            next = current+3
        else:
            next = data[i+1]

        if next - current == 1:
            jolt_differences["1"]+=1
        elif next-current == 3:
            jolt_differences["3"]+=1

    return jolt_differences

data = readData()
jolt_differences = combineAdapters(data)
print(jolt_differences["1"]*jolt_differences["3"])



