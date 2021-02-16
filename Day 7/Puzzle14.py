import re

def readRules():
    rules = []
    fh = open("bagRules.txt")
    for line in fh:
        rules.append(line.strip().replace(".",""))
    return rules

def cleanRules(rules):
    clean_rules = dict()
    for rule in rules:
        parts = rule.split("contain")
        main_bag = parts[0].replace(" bags", "").strip()
        clean_rules[main_bag] = dict()
        parts[1] = parts[1].strip()
        if parts[1] != "no other bags":
            sub_bags = parts[1].split(",")
            for bag in sub_bags:
                bag_text = bag.replace(" bags", "").replace(" bag", "").strip()
                numbers = re.findall("[0-9]", bag_text)
                if len(numbers)==1:
                    count = numbers[0]
                else:
                    count_string = ""
                    for n in numbers:
                        count_string+= n
                    count = int(count_string)
                bag_text = bag_text.replace(count,"").strip()
                clean_rules[main_bag][bag_text] = count
    return clean_rules


def getSubBags(bag,rules):
    sub_bags = []

    for sub_bag in rules[bag]:
        for i in range(int(rules[bag][sub_bag])):
            sub_bags.append(sub_bag)

    return sub_bags

def countBags(look_bag,rules):
    count = 0
    sub_bags = getSubBags(look_bag,rules)

    while len(sub_bags)!= 0:
        count += 1

        for bag in getSubBags(sub_bags[0], rules):
            sub_bags.append(bag)

        sub_bags.pop(0)

    return count

rules = readRules()
rules = cleanRules(rules)
bag = "shiny gold"

print(countBags(bag,rules))

