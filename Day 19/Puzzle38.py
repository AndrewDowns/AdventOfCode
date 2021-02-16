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
            if option.startswith("*"):
                for i, output in enumerate(outputs):
                    outputs[i] += option
            else:
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
        for rule, value in data["rules"].items():
            if rule not in rules.keys():
                if type(value) == str:
                    rules[rule] = value
                else:
                    ready = True
                    l = False
                    for options in value:
                        for option in options.split("+"):
                            if option == rule:
                                l = True
                            else:
                                if option not in rules.keys():
                                    ready = False
                    if ready:
                        if not l:
                            rules[rule] = list(get_options(value, rules))
                        else:
                            new_value = []
                            for i in range(len(value)):
                                new_value.append(value[i].replace(rule,"*"+rule))
                            rules[rule] = list(get_options(new_value, rules))

    return rules

def check_loop_messages(subrule,rules, message_len, rule):
    max_len = False
    check_messages = [subrule]
    while max_len == False:
        for i in range(len(check_messages)):
            m = check_messages[i]
            for add_rule in re.findall("[0-9]+", m):
                for option in rules[add_rule]:
                    new_m = m.replace("*" + add_rule, option)
                    #print(new_m)
                    if len(new_m) > message_len:
                        max_len = True
                        break
                    if new_m not in check_messages:
                        if new_m.count("*"):
                            check_messages.append(new_m)
                        else:
                            #data["rules"][str(rule)].append(new_m)
                            if len(new_m) == message_len:
                                yield new_m
            check_messages.pop(i)



def is_valid(message, rules, rule_number):
    print("Checking", message)
    found = False
    if message in rules[str(rule_number)]:
        print("MATCHED WITHOUT LOOP")
        found = True
        yield True
    else:
        if len(message) > len(rules[str(rule_number)][0]):
            for subrule in rules[str(rule_number)]:
                if subrule.count("*") != 0:
                    for add in check_loop_messages(subrule,rules,len(message), rule_number):
                        if message == add:
                            print("MATCHED WITH LOOP")
                            found = True
                            yield True
    if not found:
        print("NO MATCH")
        yield False

data = read_data()
data["rules"] = init_rule_options(data)
#display_data(data)
counter = 0
rule_number = 0

for message in data["messages"]:
    for match in is_valid(message, data["rules"], rule_number):
        counter+=1
        break

print(counter,"valid messages using Rule", rule_number)

