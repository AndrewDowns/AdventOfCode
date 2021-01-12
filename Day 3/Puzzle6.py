def populateGeography():
    geography = []
    fh = open("Geography.txt")
    for line in fh:
        geography.append(line.strip())
    return geography

def countTrees(right,down):
    tree_count = 0
    bottom = False
    current_row = 0
    current_coloumn = 0

    while bottom == False:
        current_coloumn += right
        current_row += down

        if current_row >= len(geography):
            bottom = True
        else:

            if current_coloumn >= len(geography[current_row]):
                current_coloumn = current_coloumn - len(geography[current_row])

            if geography[current_row][current_coloumn] == "#":
                tree_count += 1

    print(tree_count, " Trees Encountered")
    return tree_count


geography = populateGeography()
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
tree_sum = 1
for slope in slopes:
    right, down = slope
    tree_sum *= countTrees(right,down)

print(tree_sum)
