def readData():
    data = []
    fh = open("data.txt")
    for line in fh:
        data.append(int(line.strip()))
    return data

def findWeakness(data):
    weakness = 0

    for i in range(25,len(data)):
        current = data[i]
        sub_data = data[i-25:i]

        isWeak = True

        for datas in sub_data:
            for other_datas in sub_data:
                if datas+other_datas == current:
                    isWeak = False
                    break

        if isWeak:
            weakness = current
            break

    return weakness

data = readData()
print("The Weakness is ", findWeakness(data))


