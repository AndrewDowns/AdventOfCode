def readData():
    data = []
    fh = open("Input.txt")
    for line in fh:
        line = line.strip()
        if line[len(line)-1] == ")":
            line = line[:-1]
        ingredients, allergens = line.split("(contains")
        ingredients = str(ingredients)
        ingredients = ingredients.strip()
        ingredients = ingredients.split(" ")
        allergens = str(allergens)
        allergens = allergens.strip()
        allergens = allergens.split(", ")
        data.append({"ingredients":ingredients, "allergens":allergens})
    return data


data = readData()
allergens = dict()
ingredients = dict()
for line in data:
    for ingredient in line["ingredients"]:
        if ingredient not in ingredients.keys():
            ingredients[ingredient] = 1
        else:
            ingredients[ingredient] +=1

    for allergen in line["allergens"]:
        if allergen not in allergens.keys():
            allergens[allergen] = set(line["ingredients"])
        else:
            allergens[allergen] = allergens[allergen].intersection(set(line["ingredients"]))

danger_list = ""
confirmed_allergens = dict()
current_len = 1
while len(confirmed_allergens) != len(allergens):
    for allergen, allergen_v in allergens.items():
        if len(allergen_v) == current_len:
            if current_len == 1:
                confirmed_allergens[allergen] = allergen_v.pop()
            else:
                for i, a in enumerate(allergen_v):
                    found = False
                    for confirmed in confirmed_allergens:
                        if a == confirmed_allergens[confirmed]:
                            found = True
                    if not found:
                        confirmed_allergens[allergen] = a
    current_len += 1


for allergen in sorted(confirmed_allergens):
    danger_list += confirmed_allergens[allergen]+","
danger_list = danger_list[:-1]

print("The answer is", danger_list)