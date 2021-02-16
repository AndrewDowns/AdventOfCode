input = "974618352"
moves = 10000000


def display_cups(cups):
    """A function to display the current position of cups

        ------------
        cups:
        A list of integers representing the numbered cups


        ------------

        :parameter cups: list

        """
    print("Cups: ", end="")
    for j, cup in enumerate(cups):
        if j == len(cups) - 1:
            if cup == current_cup:
                print("(", cup, ")", sep="")
            else:
                print(cup)
        else:
            if cup == current_cup:
                print("(", str(cup), "), ", end="", sep="")
            else:
                print(str(cup) + ", ", end="")


cups = list()
for c in input:
    cups.append(int(c))

for i in range(max(cups)+1, 1000001):
    cups.append(i)

current = 0

for i in range(moves):
    print("-- move",i+1,"--")

    if current == len(cups):
        current = 0
    current_cup = cups[current]

    #display_cups(cups)

    pick_ups = list()
    for j in range(current+1,current+4):
        if j >= len(cups)-1:
            pick_ups.append(cups[(j-len(cups))])
        else:
            pick_ups.append(cups[j])

    print("Pick Up: ", end="")
    for j, pick_up in enumerate(pick_ups):
        if j == len(pick_ups)-1:
            print(pick_up)
        else:
            print(str(pick_up)+", ", end="")

    destination = current_cup-1
    min_cup = min(cups)
    max_cup = max(cups)
    if destination < min_cup:
        destination = max_cup

    while destination in pick_ups:
        destination -= 1
        if destination < min_cup:
            destination = max_cup
    print("Destination:", destination)

    for cup in pick_ups:
        cups.remove(cup)

    insert = 0
    for j, cup in enumerate(cups):
        if cup == destination:
            insert = j + 1
            break

    cups = cups[:insert] + pick_ups + cups[insert:]

    pos_current = 0
    for j, cup in enumerate(cups):
        if cup == current_cup:
            pos_current = j

    current = pos_current+1

    print()

print("-- final --")
if current == len(cups):
    current = 0
current_cup = cups[current]
for j, cup in enumerate(cups):
    if j == len(cups) - 1:
        if cup == current_cup:
            print("(", cup, ")", sep="")
        else:
            print(cup)
    else:
        if cup == current_cup:
            print("(", str(cup), "), ", end="", sep="")
        else:
            print(str(cup) + ", ", end="")

one_pos = 0
for i, cup in enumerate(cups):
    if cup == 1:
        one_pos = i

next = one_pos+1
if next == len(cups):
    next = 0
next_next = next+1
if next_next == len(cups):
    next_next = 0

answer = cups[next]*cups[next_next]

print()
print("The answer is",answer)