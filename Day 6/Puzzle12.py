import string

def populateGroupAnswers():
    groups = []
    fh = open("Answers.txt")
    passports_txt = fh.read()
    groups = passports_txt.split("\n\n")

    for i in range(len(groups)):
        groups[i] = groups[i].split("\n")
    return groups

def groupTotalYes(group):
    total = 0

    #Create a dictuonary of all the letters (questions) to capture answers
    d = dict.fromkeys(string.ascii_lowercase, 0)

    #Count the answers for each question from the groups people
    for person in group:
        for l in person:
            d[l] = d.get(l)+1

    #Check to see if every member in the group answered yes to each questions. Add to the total if they did
    for letter in d:
        if d[letter] == len(group):
            total += 1

    return total






groups = populateGroupAnswers()

sum = 0

for group in groups:
    sum += groupTotalYes(group)

print(sum)
