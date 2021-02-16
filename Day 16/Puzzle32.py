import re

def read_data():
    data = dict()
    fh = open("Tickets.txt")
    file_data = fh.read()

    file_parts = file_data.split("\n\n")

    field_parts = file_parts[0].split("\n")
    data["fields"] = dict()

    for field in field_parts:
        field_name = field.split(":")[0]
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
    field_validity = dict(data["fields"])
    true_count = 0

    for field in field_validity:
        field_validity[field] = False

    for field in data["fields"]:
        ranges = data["fields"][field]

        if (n>=ranges[0] and n<=ranges[1]) or (n>=ranges[2] and n<=ranges[3]):
            field_validity[field] = True
            true_count+=1

    return true_count, field_validity

def get_valid_tickets(data):
    valid_tickets = []
    for i, ticket in enumerate(data["nearby_tickets"]):
        valid = True
        ticket_holder = []
        for n in ticket:
            true_count, field_validity = valid_value(n, data)
            if true_count == 0:
                valid = False
            else:
                ticket_holder.append([n, field_validity])

        if valid:
            valid_tickets.append(ticket_holder)

    return valid_tickets

def has_blanks(order):
    for i in order:
        if i == " ":
            return True
    return False

def update_ticket(ticket_values, order):
    ticket = dict()
    for i, v in enumerate(ticket_values):
        ticket[order[i]] = v
    return ticket

def get_order_options(data, valid_tickets):
    order = []
    for i in range(0, len(data["my_ticket"])):
        options = []
        for field in data["fields"]:
            all_true = True
            for ticket in valid_tickets:
                if not ticket[i][1][field]:
                    all_true = False
            if all_true:
                options.append(field)
        print("Position", i + 1)
        print("Options: ", len(options))
        print()
        order.append(options)
    return order

def create_final_order(data, order):
    #Call Emperor Palpatine
    final_order = [None] * len(data["my_ticket"])
    current = 1
    while current < len(data["fields"]) + 1:
        for i, pos in enumerate(order):
            options = pos
            if len(options) == current:
                for candidate in options:
                    if final_order.count(candidate) == 0:
                        final_order[i] = candidate
        current += 1
    return final_order

data = read_data()
data = to_int(data)
valid_tickets = get_valid_tickets(data)
order = get_order_options(data,valid_tickets)
final_order = create_final_order(data, order)

data["my_ticket"] = update_ticket(data["my_ticket"], final_order)

sum = 1
for field in data["my_ticket"]:
    if field.startswith("departure"):
        sum = sum*data["my_ticket"][field]

print("Answer =", sum)
