import re


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
    value = '{0:036b}'.format(value)
    value = list(value)
    for i, c in enumerate(mask):
        if c == "0":
            value[i] = "0"
        elif c == "1":
            value[i] = "1"
    masked_value = "0b"
    for n in value:
        masked_value+=n
    return int(masked_value,2)


def process_data(data):
    memory = dict()
    for block in data:
        mask = block["mask"]
        for instruction in block["instructions"]:
            instruction_parts = instruction.split("=")
            value = int(instruction_parts[1])
            value = bit_mask(value, mask)
            mem_loc = re.findall("[0-9]+", instruction_parts[0])[0]
            memory[mem_loc] = value
    return memory


data = read_data()
memory = process_data(data)

sum = 0

for mem in memory:
    if memory[mem]!= 0:
        sum+= memory[mem]


print(sum)
