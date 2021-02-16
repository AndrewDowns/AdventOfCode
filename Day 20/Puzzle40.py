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


def display_order(pieces, order):
    columns = rows = int(math.sqrt(len(order)))
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
    elif o == "i90":
        # Rotate 90 degrees
        for j in range(len(piece)):
            line = ""
            for i in range(len(piece)-1, -1, -1):
                line+=piece[i][j]
            print(line)
            new_piece.append(line)
    elif o == "270":
        #Rotate 270 degrees
        new_piece = flip(piece, "180")
        new_piece = flip(new_piece, "90")
    elif o == "n":
        #Do Nothing
        new_piece = piece
    elif o == "v90":
        #Flip Vert then rotate 90
        new_piece = flip(piece, "v")
        new_piece = flip(new_piece, "90")
    elif o == "v270":
        #Flip Vert then rotate 270
        new_piece = flip(piece, "v")
        new_piece = flip(new_piece, "270")
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


def generate_options(p_list, side):
    options = []
    if side == "Bottom":
        options.append(p_list[0])
        options.append(flip(p_list,"v")[0])
        options.append(flip(p_list, "h")[0])
        options.append(flip(p_list, "90")[0])
        options.append(flip(p_list, "180")[0])
        options.append(flip(p_list, "270")[0])
        options.append(flip(flip(p_list, "v"), "90")[0])
        options.append(flip(flip(p_list, "v"), "270")[0])
    elif side == "Top":
        options.append(p_list[len(p_list)-1])
        options.append(flip(p_list, "v")[len(p_list)-1])
        options.append(flip(p_list, "h")[len(p_list)-1])
        options.append(flip(p_list, "90")[len(p_list)-1])
        options.append(flip(p_list, "180")[len(p_list)-1])
        options.append(flip(p_list, "270")[len(p_list)-1])
        options.append(flip(flip(p_list, "v"), "90")[len(p_list)-1])
        options.append(flip(flip(p_list, "v"), "270")[len(p_list)-1])
    elif side == "Right":
        options.append(generate_left(p_list))
        options.append(generate_left(flip(p_list, "v")))
        options.append(generate_left(flip(p_list, "h")))
        options.append(generate_left(flip(p_list, "90")))
        options.append(generate_left(flip(p_list, "180")))
        options.append(generate_left(flip(p_list, "270")))
        options.append(generate_left(flip(flip(p_list, "v"), "90")))
        options.append(generate_left(flip(flip(p_list, "v"), "270")))
    elif side == "Left":
        options.append(generate_right(p_list))
        options.append(generate_right(flip(p_list, "v")))
        options.append(generate_right(flip(p_list, "h")))
        options.append(generate_right(flip(p_list, "90")))
        options.append(generate_right(flip(p_list, "180")))
        options.append(generate_right(flip(p_list, "270")))
        options.append(generate_right(flip(flip(p_list, "v"), "90")))
        options.append(generate_right(flip(flip(p_list, "v"), "270")))
    return options


def get_match(side, pieces, current, checking):
    for p in pieces:
        if p != current:
            p_list = pieces[p]
            options = generate_options(p_list, checking)
            moves = ["n", "v", "h", "90", "180", "270", "v90", "v270"]
            for i, option in enumerate(options):
                if side == option:
                    return p, moves[i]

    return None


def matches_init(pieces):
    piece_matches = dict()
    for piece in pieces:
        sides = dict()
        sides["Top"] = pieces[piece][0]
        sides["Left"] = generate_left(pieces[piece])
        sides["Right"] = generate_right(pieces[piece])
        sides["Bottom"] = pieces[piece][len(pieces[piece])-1]
        matches = dict()
        for side in sides:
            matches[side] = get_match(sides[side], pieces, piece, side)
        piece_matches[piece] = matches

    return piece_matches


def sort_pieces(piece_matches, pieces, order):
    for item in piece_matches:
        if piece_matches[item]["Top"] is None and piece_matches[item]["Left"] is None:
            start = item

    checking = "Right"
    current = start
    new_pieces = dict()
    new_pieces[start] = pieces[start]
    new_order = [start]
    i = 2
    row = 0

    while len(new_order) != len(order):
        if i == math.sqrt(len(order)) + 1:
            i = 1
            checking = "Bottom"
            current = new_order[row * int(math.sqrt(len(order)))]
            row += 1
            side = new_pieces[current][len(new_pieces[current]) - 1]
        else:
            checking = "Right"
            side = generate_right(new_pieces[current])

        match = get_match(side, pieces, current, checking)
        current = match[0]
        new_order.append(current)
        new_pieces[current] = flip(pieces[current], match[1])
        i += 1
    return new_pieces, new_order


def strip_borders(new_pieces):
    for piece, value in new_pieces.items():
        value.pop(0)
        value.pop(len(value)-1)
        new_pieces[piece] = value
        new_value = []
        for item in new_pieces[piece]:
            line = item[1:len(item)-1]
            new_value.append(line)
        new_pieces[piece] = new_value
    return new_pieces

def create_image(pieces, order):
    image = ""
    columns = rows = int(math.sqrt(len(order)))
    piece_length = len(pieces[order[0]])
    for k in range(rows):
        for i in range(piece_length):
            for j in range(columns):
                current_piece = order[(k * rows) + j]
                image +=pieces[current_piece][i]
            image+= "\n"
    return image[:-1]


def count_monsters(image):
    image_lines = image.split("\n")
    monster_count = 0
    pattern_lines = ["                  # ","#    ##    ##    ###"," #  #  #  #  #  #   "]

    for i, line in enumerate(image_lines):
        current_row = i
        for j, c in enumerate(line):
            offset = j
            try:
                top = image_lines[current_row][offset:offset + 20]
                middle = image_lines[current_row + 1][offset:offset + 20]
                bottom = image_lines[current_row + 2][offset:offset + 20]

                monster_found = True

                for k, l in enumerate(pattern_lines[0]):
                    if l == "#":
                        if top[k] != "#":
                            monster_found = False
                            break

                if monster_found:
                    for k, l in enumerate(pattern_lines[1]):
                        if l == "#":
                            if middle[k] != "#":
                                monster_found = False
                                break

                if monster_found:
                    for k, l in enumerate(pattern_lines[2]):
                        if l == "#":
                            if bottom[k] != "#":
                                monster_found = False
                                break

                if monster_found:
                    monster_count +=1
            except:
                x = 0
    return monster_count


def flip_image(image_lines, o):
    if o == "v":
        #Flip Vertically
        return list(reversed(image_lines))
    elif o == "h":
        #Flip Horizontally
        new_image_lines = []
        for i, line in enumerate(image_lines):
            new_line = ""
            new_line_list = list(reversed(line))
            for c in new_line_list:
                new_line += c
            new_image_lines.append(new_line)
        return new_image_lines
    elif o =="n":
        return image_lines
    elif o =="90":
        new_image_lines = []
        for j in range(len(image_lines)):
            line = ""
            for i in range(len(image_lines)-1, -1, -1):
                line+=image_lines[i][j]
            new_image_lines.append(line)
        return new_image_lines
    elif o =="180":
        new_image_lines = flip_image(image_lines, "90")
        new_image_lines = flip_image(new_image_lines, "90")
        return new_image_lines
    elif o == "270":
        new_image_lines = flip_image(image_lines, "90")
        new_image_lines = flip_image(new_image_lines, "90")
        new_image_lines = flip_image(new_image_lines, "90")
        return new_image_lines
    elif o == "v90":
        new_image_lines = flip_image(image_lines, "v")
        new_image_lines = flip_image(new_image_lines, "90")
        return new_image_lines
    elif o == "v270":
        new_image_lines = flip_image(image_lines, "v")
        new_image_lines = flip_image(new_image_lines, "270")
        return new_image_lines



def hunt_monsters(image):
    total_hash = image.count("#")
    flip_options = ["n", "v", "h", "90", "180", "270", "v90", "v270"]
    image_lines = image.split("\n")
    for option in flip_options:
        new_image_lines = flip_image(image_lines, option)
        new_image = ""
        for line in new_image_lines:
            new_image += line + "\n"
        count = count_monsters(new_image)
        if count != 0:
            print(option)
            print(count, "Monsters in yar waters!")
            print(total_hash - (count * 15), "Non Monster Parts")
            print()

pieces = read_data()
order = init_order(pieces)
piece_matches = matches_init(pieces)
new_pieces, new_order = sort_pieces(piece_matches, pieces, order)
new_pieces = strip_borders(new_pieces)
#display_order(new_pieces, new_order)
image = create_image(new_pieces, new_order)
hunt_monsters(image)



