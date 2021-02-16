import re

def read_data():
    data = []
    fh = open("Data.txt")
    for line in fh:
        data.append(line.strip().replace(" ",""))
    return data


def solve(line):
    while line.find("(") != -1:
        start = line.find("(")
        next = line.find("(", start+1)
        end = line.find(")")

        if next != -1:
            while next < end and next != -1:
                next = line.find("(", next+1)
                end = line.find(")", end+1)



        line = line[0:line.find("(")]+str(solve(line[start+1:end]))+line[end+1:]

    numbers = re.findall("[0-9]+", line)
    for i, n in enumerate(numbers):
        numbers[i] = int(n)

    order_ops = []
    for c in line:
        if c == "+" or c == "*":
            order_ops.append(c)

    sum = numbers[0]
    i = 1
    for op in order_ops:
        if op == "+":
            sum += numbers[i]
        elif op == "*":
            sum *= numbers[i]
        i+=1

    return sum


def get_line_totals(data):
    line_totals = []
    for line in data:
        line_totals.append(solve(line))
    return line_totals

data = read_data()
line_totals = get_line_totals(data)
print("Total =", sum(line_totals))