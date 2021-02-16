import math

def populateBoardingPasses():
    boardingPasses = []
    fh = open("BoadingPasses.txt")
    for line in fh:
        boardingPasses.append(line.strip())
    return boardingPasses

def populateSeats():
    seats = []
    for i in range(0,128):
        row = []
        for j in range(0,8):
            seat = dict()
            seat["seat_id"] = (i*8)+j
            seat["taken"] = False
            row.append(seat)
        seats.append(row)
    return seats

def visualisePlane(seats):
    print("  | C0 | C1 | C2 | C3 | C4 | C5 | C6 | C7 |")
    for i in range(128):
        row = "R"+str(i) + " |"
        for j in range(8):
            if seats[i][j]["taken"]:
                row = row + " "+str(seats[i][j]["seat_id"])+" |"
            else:
                row = row + " O |"
        print(row)

def allocateBoardingPass(boardingPass,seats):

    row = [0,127]
    column = [0,7]

    counter = 0
    for l in boardingPass:
        if l == "F":
            row[1] = int(math.floor((row[0]+row[1])/2))
        elif l == "B":
            row[0] = int(math.ceil((row[0]+row[1])/2))
        elif l == "L":
            column[1] = int(math.floor((column[0]+column[1])/2))
        elif l == "R":
            column[0] = int(math.ceil((column[0]+column[1])/2))
        counter += 1

    if row[0] == row[1]:
        row = row[0]
        if column[0] == column[1]:
            column = column[0]
            seats[row][column]["taken"] = True
            seats[row][column]["Boarding_Pass"] = boardingPass
        else:
            print("Column Error - ", boardingPass)
    else:
        print("Row Error - ", boardingPass)

    return seats

def boardPlane(boardingPasses,seats):
    for boardingPass in boardingPasses:
        seats = allocateBoardingPass(boardingPass, seats)
    return seats

boardingPasses = populateBoardingPasses()
seats = populateSeats()
seats = boardPlane(boardingPasses,seats)

visualisePlane(seats)

