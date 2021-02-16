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
    return buses


def find_bus(buses, timestamp):
    our_bus = dict()

    for bus in buses:
        departure = int((timestamp+bus)/bus)
        departure = departure*bus
        if our_bus.get("bus_id") == None or (departure-timestamp)<our_bus.get("wait"):
            our_bus["bus_id"] = bus
            our_bus["departure"] = departure
            our_bus["wait"] = departure-timestamp
            print(bus, " departs", departure)
    return our_bus

data = read_data()
earliest_timestamp = int(data[0])
available_buses = get_buses(data[1].split(","))
available_buses.sort()

bus = find_bus(available_buses, earliest_timestamp)

print("Answer is", bus["bus_id"]*bus["wait"])
