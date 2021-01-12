def populateGeography():
    geography = []
    fh = open("Geography.txt")
    for line in fh:
        geography.append(line.strip())
    return geography

tree_count = 0
bottom = False
current_row = 0
current_coloumn = 0
geography = populateGeography()

while bottom == False:
    current_coloumn+=3
    current_row+=1

    if current_row==len(geography):
        bottom = True
    else:

        if current_coloumn >= len(geography[current_row]):
            current_coloumn = current_coloumn - len(geography[current_row])

        if geography[current_row][current_coloumn]=="#":
            tree_count+=1

print(tree_count, " Trees Encountered")