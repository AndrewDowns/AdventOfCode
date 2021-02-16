import re

def read_data():
    data = dict()
    fh = open("sample.txt")
    file_data = fh.read()

    file_parts = file_data.split("\n\n")

    field_parts = file_parts[0].split("\n")
    data["fields"] = dict()

    for field in field_parts:
        field_name = re.findall("[a-z]+:", field)[0][:-1]
        range_values = re.findall("[0-9]+", field)
        data["fields"][field_name] = range_values

    data["my_ticket"] = re.findall("[0-9]+", file_parts[1])

    data["nearby_tickets"] = []
    nearby_tickets = file_parts[2].split(":\n")[1].split("\n")

    for ticket in nearby_tickets:
        data["nearby_tickets"].append(re.findall("[0-9]+", ticket))

    return data

def to_int(data):
    for field in data["fields"]:
        for i, n in enumerate(data["fields"][field]):
            data["fields"][field][i] = int(n)

    for i, n in enumerate(data["my_ticket"]):
        data["my_ticket"][i] = int(n)

    for i, ticket in enumerate(data["nearby_tickets"]):
        for j, n in enumerate(ticket):
            data["nearby_tickets"][i][j] = int(n)

    return data

def valid_value(n, data):
    valid = False
    for field in data["fields"]:
        ranges = data["fields"][field]

        if (n>=ranges[0] and n<=ranges[1]) or (n>=ranges[2] and n<=ranges[3]):
            valid = True
            break
    return valid

data = read_data()
data = to_int(data)
invalid_numbers = []

for ticket in data["nearby_tickets"]:
    for n in ticket:
        if not valid_value(n, data):
            invalid_numbers.append(n)

print(invalid_numbers)
sum = 0
for n in invalid_numbers: sum+=n
print("Scanning Error Rate =",sum)