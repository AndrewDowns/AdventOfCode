import re, math


def read_data():
    fh = open("Input.txt")
    file_data = fh.read()
    file_pieces = file_data.split("\n\n")
    pieces = dict()

    for piece in file_pieces:
        piece_data = piece.split("\n")
        for data in piece_data:
            if data.startswith("Tile"):
                tile_id = re.findall("[0-9]+", data)[0]
                pieces[tile_id] = []
            else:
                pieces[tile_id].append(data.strip())

    return pieces


def init_order(pieces):
    order = []
    for piece in pieces:
        order.append(piece)
    return order


def display_image(pieces, order):
    columns = rows = int(math.sqrt(len(pieces)))
    piece_length = len(pieces[order[0]])
    spacer = len((pieces[order[0]][0]))
    for k in range(rows):
        for tile in range(columns):
            print(order[(k*rows)+tile], " "*(spacer-len(order[(k*rows)+tile])), sep="", end=" ")
        print("\n", end="")
        for i in range(piece_length):
            for j in range(columns):
                current_piece = order[(k*rows)+j]
                print(pieces[current_piece][i], end=" ")
            print("\n", end="")
        print()


def flip(piece, o):
    new_piece = []
    if o == "v":
        #Flip Vertically
        new_piece = list(reversed(piece))
    elif o == "h":
        #Flip Horizontally
        for i, line in enumerate(piece):
            new_line = ""
            new_line_list = list(reversed(line))
            for c in new_line_list:
                new_line += c
            new_piece.append(new_line)
    elif o == "180":
        #Rotate 180 degrees
        new_piece = flip(piece, "v")
        new_piece = flip(new_piece, "h")
    elif o == "90":
        # Rotate 90 degrees
        for j in range(len(piece)):
            line = ""
            for i in range(len(piece)-1, -1, -1):
                line+=piece[i][j]
            new_piece.append(line)
    elif o == "270":
        #Rotate 270 degrees
        new_piece = flip(piece, "180")
        new_piece = flip(new_piece, "90")
    return new_piece


def generate_left(piece):
    left = ""
    for i in piece:
        left+=i[0]

    return left


def generate_right(piece):
    right = ""
    for i in piece:
        right+=i[len(piece[0])-1]
    return right

def generate_options(p_list):
    options = []
    options.append(p_list[0])
    options.append(flip(p_list,"v")[0])
    options.append(flip(p_list, "h")[0])
    options.append(flip(p_list, "90")[0])
    options.append(flip(p_list, "180")[0])
    options.append(flip(p_list, "270")[0])
    options.append(flip(flip(p_list,"v"), "h")[0])
    options.append(flip(flip(p_list, "v"), "90")[0])
    options.append(flip(flip(p_list, "v"), "180")[0])
    options.append(flip(flip(p_list, "v"), "270")[0])
    options.append(flip(flip(p_list, "h"), "v")[0])
    options.append(flip(flip(p_list, "h"), "90")[0])
    options.append(flip(flip(p_list, "h"), "180")[0])
    options.append(flip(flip(p_list, "h"), "270")[0])
    return options



def check_side(side, pieces, current):
    for p in pieces:
        if p != current:
            p_list = pieces[p]
            options = generate_options(p_list)
            if side in options:
                return True



def side_count_init(pieces):
    side_count = dict()
    for piece in pieces:
        side_count[piece] = 0
        top = pieces[piece][0]
        left = generate_left(pieces[piece])
        right = generate_right(pieces[piece])
        bottom = pieces[piece][len(pieces[piece])-1]
        sides = [top,right,bottom,left]

        for side in sides:
            if check_side(side, pieces, piece):
                side_count[piece] += 1

    return side_count


pieces = read_data()
order = init_order(pieces)
side_count = side_count_init(pieces)
sum = 1
for items in side_count:
    if side_count[items] == 2:
        print(items)
        sum *= int(items)
print("Answer is", sum)
