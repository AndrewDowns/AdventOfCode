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

def findSum(weakness,data):

    for i in range(len(data)):
        con_nums = []
        sum = 0
        current = i
        found = False

        while sum<weakness:
            current+=1
            con_nums.append(data[current])
            sum+=data[current]

            if sum == weakness:
                found = True
                break

        if found:
            break


    return con_nums

data = readData()
weakness = findWeakness(data)
print(weakness)
con_nums = findSum(weakness,data)
con_nums.sort()
print(con_nums[0]+con_nums[len(con_nums)-1])



