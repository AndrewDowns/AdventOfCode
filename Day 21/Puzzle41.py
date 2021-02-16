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
count = 0
for ingredient in ingredients:
    allergy = False
    for allergen in allergens:
        if ingredient in allergens[allergen]:
            allergy = True

    if not allergy:
        count += ingredients[ingredient]


for allergen in allergens:
    print(allergen, allergens[allergen])

print("The answer is", count)