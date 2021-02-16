import re
import math

def read_data():
    data = []
    fh = open("directions.txt")
    for line in fh:
        data.append(line.strip())
    return data

def move(x,y,action,amount, waypoint_x, waypoint_y):
    if action == "N":
        waypoint_y-=amount
    elif action == "S":
        waypoint_y+=amount
    elif action == "E":
        waypoint_x+=amount
    elif action == "W":
        waypoint_x-=amount
    elif action == "F":
        for i in range(amount):
            x += waypoint_x
            y += waypoint_y
    elif action == "L" or action == "R":

        if action=="R":
            radian_amount = math.radians(amount)
        else:
            radian_amount = math.radians(amount)*-1

        new_waypoint_x = (waypoint_x*math.cos(radian_amount)) - (waypoint_y*math.sin(radian_amount))
        new_waypoint_y = (waypoint_x*math.sin(radian_amount)) + (waypoint_y*math.cos(radian_amount))

        waypoint_x = new_waypoint_x.__round__()
        waypoint_y = new_waypoint_y.__round__()

    return(x,y, waypoint_x, waypoint_y)



data = read_data()
x = 0
y = 0
waypoint_x = 10
waypoint_y = -1

for instruction in data:
    action = re.findall("[N,S,E,W,F,L,R]", instruction).__getitem__(0)
    value = int(instruction.replace(action,""))
    x,y,waypoint_x, waypoint_y = move(x,y,action,value, waypoint_x, waypoint_y)
    print(instruction, " Ship", "(" ,x,",",y,") |   Waypoint (" ,waypoint_x,",",waypoint_y,")")

print()
print("Manhattan Distance = ", x+y)
