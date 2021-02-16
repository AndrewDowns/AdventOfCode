import itertools


def read_data():
    data = []
    fh = open("Data.txt")
    for line in fh:
        data.append(line.strip())
    return data


def init_on(data):
    on_values = set()
    for i, row in enumerate(data):
        for j, item in enumerate(row):
            if item == "#":
                on_values.add((i,j,0))
    return on_values


def run_cycle(on_values, number):
    for i in range(number):
        print("Cycle", i+1)

        checked = dict()
        stay_on = set()
        turn_on = set()

        for location in on_values:
            for option in itertools.product([-1,0,1], repeat=3):
                neighbour = tuple(map(sum, zip(location,option)))

                if neighbour != location:
                    if neighbour not in checked:
                        checked[neighbour] = 1
                    else:
                        checked[neighbour] += 1

        for location in on_values:
            if location in checked and checked[location] in [2, 3]:
                stay_on.add(location)

        for location in checked:
            if location not in on_values and checked[location] == 3:
                turn_on.add(location)

        on_values = stay_on | turn_on
        print(on_values)
        print()

    print()
    print("Answer is", len(on_values))


data = read_data()
on_values = init_on(data)
run_cycle(on_values, 6)