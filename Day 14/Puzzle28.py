import re
import itertools

def read_data():
    data = []
    fh = open("Data.txt")
    block = dict()
    for line in fh:
        if line.startswith("mask"):
            data.append(block)
            block = dict()
            block["mask"] = line.split("=")[1].strip()
            block["instructions"] = []
        elif line.startswith("mem"):
            block["instructions"].append(line.strip())
    data.append(block)
    data.pop(0)
    return data

def bit_mask(value, mask):
    masked_mem_loc = []
    x_loc = []
    value = '{0:036b}'.format(value)
    value = list(value)
    for i, c in enumerate(mask):
        if c == "1":
            value[i] = "1"
        elif c == "X":
            value[i] = "X"
            x_loc.append(i)

    values = []

    # Get all combinations of the 0s and 1s possible with the amount of Xs to fill
    combo_str = "01"*len(x_loc)
    combinations = set(itertools.combinations_with_replacement(combo_str,len(x_loc)))

    #For each combination add it to the list of output values
    for combination in combinations:
        new_value = []+value
        for p, x in enumerate(x_loc):
            new_value[x] = str(combination[p])
        values.append(new_value)

    for value in values:
        masked_value = "0b"
        for n in value:
            masked_value+=n
        masked_mem_loc.append(int(masked_value,2))

    return masked_mem_loc


def process_data(data):
    memory = dict()
    for block in data:
        mask = block["mask"]
        for instruction in block["instructions"]:
            print("Running ", instruction)
            instruction_parts = instruction.split("=")
            value = int(instruction_parts[1])
            mem_loc = re.findall("[0-9]+", instruction_parts[0])[0]
            masked_mem_loc = bit_mask(int(mem_loc), mask)

            for mem_loc in masked_mem_loc:
                memory[mem_loc] = value

        print()

    return memory


data = read_data()
memory = process_data(data)

sum = 0

for mem in memory:
    if memory[mem]!= 0:
        sum+= memory[mem]


print("Answer is ",sum)
