import re

def read_data():
    data = []
    fh = open("directions.txt")
    for line in fh:
        data.append(line.strip())
    return data

def move(x,y,facing,action,amount):
    if action == "N":
        y-=amount
    elif action == "S":
        y+=amount
    elif action == "E":
        x+=amount
    elif action == "W":
        x-=amount
    elif action == "F":
        if facing == 0:
            y-=amount
        elif facing == 90:
            x+=amount
        elif facing == 180:
            y+=amount
        elif facing == 270:
            x-=amount
    elif action == "L":
        if facing-amount<0:
            facing = 360+(facing - amount)
        else:
            facing-=amount
    elif action == "R":
        if facing + amount >= 360:
            facing = (facing+amount)-360
        else:
            facing += amount
    return(x,y, facing)



data = read_data()
x = 0
y = 0
facing = 90

for instruction in data:
    action = re.findall("[N,S,E,W,F,L,R]", instruction).__getitem__(0)
    value = int(instruction.replace(action,""))
    x,y,facing = move(x,y,facing,action,value)
    print(instruction, " ", "(" ,x,",",y,") Facing ", facing)

print()
print("Manhattan Distance = ", x+y)
