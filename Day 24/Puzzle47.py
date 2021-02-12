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


data = read_data()
init_tiles(data)
print(len(black_tiles), "Black Tiles")