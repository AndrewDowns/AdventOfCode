def read_data():
    data = []
    fh = open("schedule.txt")
    for line in fh:
        data.append(line.strip())
    return data


def get_buses(bus_data):
    buses = []
    for bus in bus_data:
        if bus != "x":
            buses.append(int(bus))
        else:
            buses.append(bus)
    return buses

def find_timestamp(buses):
    '''
    My solution; more of a recursive method that takes forever to achieve the goal when the input
    is a very large number

    :param buses: the list of available bus ids or out of service buses (marked as x)
    :return: the timestamp of the departure of the first bus in the list where all subsequent buses depart
    in 1 minute intervals after
    '''


    #timestamp = buses[0]
    starting_factor = int(100002248028938/buses[0]) #for larger lists we can start at a higher factor
    timestamp = buses[0]*starting_factor
    found = False

    while not found:
        print(timestamp)
        timestamp+= buses[0]
        found_count = 1

        for i in range(1,len(buses)):
            next_timestamp = timestamp+i
            if buses[i] == "x" or next_timestamp%buses[i] == 0:
                found_count+=1

        if found_count==len(buses):
            found = True

    return timestamp


def part2(buses):
    #Credit to Seoane8 for the solution. I added my own comments to understand it.
    mods = {}



    for idx, bus in enumerate(buses):
        #enumerate works similar to range
        #enumerate returns the current index and the value of the current index item
        #idx is current index and bus is the value at that index
        if bus != 'x':
            #set the key for bus to the remainder of -1*index/bus_id
            print(35%37)
            mods[bus] = -idx % bus

    print(mods)

    iterator = 0 #This will be the timestamp of departures
    increment = 1 #The increment value should start at 1

    for bus in mods.keys():
        #For every bus_id in our mods dictionary

        while iterator % bus != mods[bus]:
            #While the remainder of the timestamp divided by the bus_id isn't equal to the current key value
            #increase the timestamp value by the increment value
            iterator += increment
        #Multiply the previous increment by the current bus id
        increment *= bus

    return iterator


data = read_data()
available_buses = get_buses(data[1].split(","))
earliest_timestamp = part2(available_buses)

print("Answer is", earliest_timestamp)
