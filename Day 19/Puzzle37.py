import re

def read_data():
    data = dict()
    fh = open("Data.txt")
    file_data = fh.read()
    file_data_parts = file_data.split("\n\n")
    rules = dict()

    for rule in file_data_parts[0].split("\n"):
        rule_parts = rule.split(":")
        key = rule_parts[0]
        value = []
        for condition in rule_parts[1].split("|"):
            sub_rules = re.findall("[0-9]+", condition)
            formatted_sub_rules = ''
            for i, r in enumerate(sub_rules):
                if i != 0:
                    formatted_sub_rules += "+"
                formatted_sub_rules += r
            if len(sub_rules) == 0:
                value = condition.strip().replace('"','')
            else:
                value.append(formatted_sub_rules)

        rules[key] = value

    data["rules"] = rules
    data["messages"] = file_data_parts[1].split("\n")
    return data


def display_data(data):
    print("Rules")
    print("---------")
    for rule, v in data["rules"].items():
        print(rule, ":", v)
    print("---------")
    print()
    print("Messages")
    print("---------")
    for message in data["messages"]:
        print(message)
    print()


def get_options(input, rules):
    for options in input:
        outputs = ['']

        for option in options.split("+"):
            if type(rules[option]) == str:
                for i,output in enumerate(outputs):
                    outputs[i] += rules[option]
            else:
                new_outputs = []
                for i in range(len(outputs)):
                    original = outputs[i]
                    for extension in rules[option]:
                        new_outputs.append(original + extension)
                outputs = new_outputs

        for output in outputs:
            yield output


def init_rule_options(data):
    rules = dict()

    while len(rules) < len(data["rules"]):
        print(rules)
        for rule, value in data["rules"].items():
            if rule not in rules.keys():
                print("Checking", rule, value)
                if type(value) == str:
                    print("Rule", rule, "is ready")
                    rules[rule] = value
                else:
                    ready = True
                    for options in value:
                        for option in options.split("+"):
                            if option not in rules.keys():
                                ready = False
                    if ready:
                        print("Rule", rule, "is ready")
                        rules[rule] = list(get_options(value, rules))

    print()
    return rules


def is_valid(message, rules, rule_number):
    if message in rules[str(rule_number)]:
        return True
    else:
        return False

data = read_data()
#display_data(data)
data["rules"] = init_rule_options(data)
counter = 0
rule_number = 0

for message in data["messages"]:
    if is_valid(message, data["rules"], rule_number):
        counter+=1

print(counter,"valid messages using Rule", rule_number)

