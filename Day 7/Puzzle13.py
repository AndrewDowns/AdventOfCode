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
    return list(rules[bag].keys())

def numberOfBags(look_bag,rules):
    count = 0
    for rule in rules:
        contains = False
        if rule != look_bag:
            sub_bags = getSubBags(rule,rules)
            while len(sub_bags)!= 0:
                if sub_bags[0] == look_bag:
                    contains = True
                else:
                    for bag in getSubBags(sub_bags[0], rules):
                        sub_bags.append(bag)

                sub_bags.pop(0)

        if contains:
            count+=1

    return count

rules = readRules()
rules = cleanRules(rules)
bag = "shiny gold"

print(numberOfBags(bag,rules))

