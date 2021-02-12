def read_data():
    """A function to read the routes to the first tiles to be flipped

    :return data: list

    """
    fh = open("input.txt")
    data = []
    for line in fh.readlines():
        data.append(line.strip())
    return data

def init_tiles(data):
    """A function to flip the first tiles from white to black or black to white.
    The tiles are found using the directions given in the data lines

        ------------
        data:
        A list of strings. Each of which is a series of directions for find the tile to flip

        ------------

            :parameter data: list
            :return black_tiles: list
            :return white_tiles: list

    """

    skip = False
    black_tiles = []
    white_tiles = []

    for line in data:
        current = [0.0, 0.0]
        for i, c in enumerate(line):
            if not skip:
                if c == "e":
                    current[0] += 1
                elif c == "w":
                    current[0] -= 1
                elif c == "s":
                    skip = True
                    if line[i] + line[i + 1] == "sw":
                        current[0] -= 0.5
                        current[1] -= 0.5
                    else:
                        current[1] -= 0.5
                        current[0] += 0.5
                elif c == "n":
                    skip = True
                    if line[i] + line[i + 1] == "nw":
                        current[1] += 0.5
                        current[0] -= 0.5
                    else:
                        current[0] += 0.5
                        current[1] += 0.5
            else:
                skip = False

        if current in black_tiles:
            black_tiles.remove(current)
            white_tiles.append(current)
        elif current in white_tiles:
            white_tiles.remove(current)
            black_tiles.append(current)
        else:
            black_tiles.append(current)

    return black_tiles, white_tiles


def get_neighbours(tile):
    """A function to get the 6 adjacent tiles to the current tile

        ------------
        tile:
        A list with two values. Value one is the tile's x placement and value two is the tile's y placement

         ------------

            :parameter tile: list
            :return neighbours: list

    """
    neighbours = []
    neighbours.append([tile[0]+1, tile[1]]) #East
    neighbours.append([tile[0] - 1, tile[1]]) #West
    neighbours.append([tile[0] - 0.5, tile[1]-0.5])  #South West
    neighbours.append([tile[0] + 0.5, tile[1] - 0.5])  # South East
    neighbours.append([tile[0] - 0.5, tile[1] + 0.5])  # North West
    neighbours.append([tile[0] + 0.5, tile[1] + 0.5])  # North East
    return neighbours


def simulate_days(black, white, days):
    """A function to simulate the changing of the black and white tiles over a set number of days.
    The changes are defined as follows;
        Any black tiles which have 0 Adjacent black tiles or more than 2 adjacent black tiles must
        change to white

        Any white tiles which have exactly 2 adjacent black tiles must change to black.

    All of the changes will happen simultaneously

        ------------
        black:
        A list of lists. Each list is an x and y coordanite of a black tile

        white:
        A list of lists: Each list is an x and y coordanite of the known white tiles

        days:
        An integer that must be positive, representing the number of days to simulate the changes.

        ------------

        :parameter black: list
        :parameter white: list
        :parameter days: integer
        :return black: list
        :return white: list

    """
    for i in range(days):
        b_flip = []
        w_flip = []
        for tile in black:
            count = 0
            neighbours = get_neighbours(tile)
            for neighbour in neighbours:
                if neighbour in black:
                    count +=1
                elif neighbour not in white:
                    white.append(neighbour)
            if count == 0 or count >2:
                w_flip.append(tile)

        for tile in white:
            count = 0
            neighbours = get_neighbours(tile)
            for neighbour in neighbours:
                if neighbour in black:
                    count += 1
            if count == 2:
                b_flip.append(tile)

        for tile in w_flip:
            black.remove(tile)
            white.append(tile)

        for tile in b_flip:
            white.remove(tile)
            black.append(tile)
        print("Day", i+1, len(black), "Black Tiles")
    return black, white


data = read_data()
black_tiles, white_tiles = init_tiles(data)
black_tiles, white_tiles = simulate_days(black_tiles, white_tiles, 100)
print(len(white_tiles), "White Tiles")
print(len(black_tiles), "Black Tiles")