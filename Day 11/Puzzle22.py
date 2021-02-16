

def read_data():
    data = []
    fh = open("seats.txt")
    for line in fh:
        line = line.strip()
        line_data = []
        for c in line:
            line_data.append(c)
        data.append(line_data)
    return data


def visualise_seats(data):
    print()
    print()
    for row in data:
        row_display = ""
        for seat in row:
            row_display+=seat
        print(row_display)


def clone_seats(data):
    new_seats = []
    for row in data:
        row_list = []
        for seat in row:
            row_list.append(seat)
        new_seats.append(row_list)
    return new_seats


def get_adjacent(data,row,seat):
    adjacent_seats = {"left":"L", "right":"L", "up":"L", "down":"L", "up-left":"L", "up-right":"L", "down-left":"L", "down-right":"L"}

    if seat == 0:
        adjacent_seats["left"] = "-"
    else:
        first_seat = data[row][seat - 1]
        i = seat-1
        while first_seat == ".":
            if i < 0:
                first_seat = "-"
                break
            else:
                first_seat = data[row][i]
            i -= 1

        adjacent_seats["left"] = first_seat

    if seat == len(data[row])-1:
        adjacent_seats["right"] = "-"
    else:
        first_seat = data[row][seat + 1]
        i = seat + 1
        while first_seat == ".":
            if i > len(data[row])-1:
                first_seat = "-"
                break
            else:
                first_seat = data[row][i]
            i += 1
        adjacent_seats["right"] = first_seat

    if row == 0:
        adjacent_seats["up"] = "-"
    else:
        first_seat = data[row-1][seat]
        i = row-1
        while first_seat == ".":
            if i < 0:
                first_seat = "-"
                break
            else:
                first_seat = data[i][seat]
            i -= 1
        adjacent_seats["up"] = first_seat

    if row == len(data)-1:
        adjacent_seats["down"] = "-"
    else:
        first_seat = data[row + 1][seat]
        i = row + 1
        while first_seat == ".":
            if i > len(data)-1:
                first_seat = "-"
                break
            else:
                first_seat = data[i][seat]
            i += 1
        adjacent_seats["down"] = first_seat

    if seat == 0 or row == 0:
        adjacent_seats["up-left"] = "-"
    else:
        first_seat = data[row - 1][seat-1]
        i = seat - 1
        r = row - 1
        while first_seat == ".":
            if i < 0 or r < 0:
                first_seat = "-"
                break
            else:
                first_seat = data[r][i]
            i -= 1
            r -= 1
        adjacent_seats["up-left"] = first_seat

    if row == 0 or seat == len(data[row])-1:
        adjacent_seats["up-right"] = "-"
    else:
        first_seat = data[row - 1][seat + 1]
        i = seat + 1
        r = row - 1
        while first_seat == ".":
            if i > len(data[row])-1 or r < 0:
                first_seat = "-"
                break
            else:
                first_seat = data[r][i]
            i += 1
            r -= 1
        adjacent_seats["up-right"] = first_seat

    if row == len(data)-1 or seat == 0:
        adjacent_seats["down-left"] = "-"
    else:
        first_seat = data[row + 1][seat - 1]
        i = seat - 1
        r = row + 1
        while first_seat == ".":
            if i < 0 or r > len(data)-1:
                first_seat = "-"
                break
            else:
                first_seat = data[r][i]
            i -= 1
            r += 1
        adjacent_seats["down-left"] = first_seat

    if row == len(data)-1 or seat == len(data[row])-1:
        adjacent_seats["down-right"] = "-"
    else:
        first_seat = data[row + 1][seat + 1]
        i = seat + 1
        r = row + 1
        while first_seat == ".":
            if i > len(data[row])-1 or r > len(data)-1:
                first_seat = "-"
                break
            else:
                first_seat = data[r][i]
            i += 1
            r += 1
        adjacent_seats["down-right"] = first_seat

    return adjacent_seats


def seat_people(data):
    new_data = clone_seats(data)
    for row in range(len(data)):
        seats = data[row]
        for seat in range(len(seats)):
            current_seat = seats[seat]
            adjacent_seats = get_adjacent(data, row, seat)
            if current_seat == "L":
                # If a seat is empty
                adjacent = False
                for adjacent_seat in adjacent_seats:
                    if adjacent_seats[adjacent_seat] == "#":
                        adjacent = True
                if not adjacent:
                    new_data[row][seat] = "#"
            elif current_seat == "#":
                adjacent_count = 0
                for adjacent_seat in adjacent_seats:
                    if adjacent_seats[adjacent_seat] == "#":
                        adjacent_count+=1
                if adjacent_count>=5:
                    new_data[row][seat] = "L"
    visualise_seats(new_data)
    return new_data


def count_occupied(data):
    empty_count = 0
    for row in data:
        for seat in row:
            if seat == "#":
                empty_count+=1
    return empty_count


def compare_seats(data,new_data):
    same = True
    for row in range(len(data)):
        for seat in range(len(data[row])):
            if data[row][seat] != new_data[row][seat]:
                same = False
                break
    return same


data = read_data()
visualise_seats(data)
new_data = seat_people(data)

while not compare_seats(data, new_data):
    data = new_data
    new_data = seat_people(data)

print("\n\n", count_occupied(new_data), "Occupied Seats")
