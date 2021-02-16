def populateGroupAnswers():
    groups = []
    fh = open("Answers.txt")
    passports_txt = fh.read()
    groups = passports_txt.split("\n\n")

    for i in range(len(groups)):
        groups[i] = groups[i].replace("\n","")
    return groups

def cleanGroupAnswers(groups):

    for i in range(len(groups)):
        group = groups[i]
        group = "".join(set(group))
        groups[i] = group

    return groups

def totalYes(groups):
    total = 0

    for group in groups:
        total += len(group)

    return total

groups = populateGroupAnswers()
groups = cleanGroupAnswers(groups)
print(totalYes(groups))
