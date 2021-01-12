def populateExpenses():
    expense_amounts = []
    fh = open("ExpenseReport.txt")
    for line in fh:
        expense_amounts.append(int(line))

    return expense_amounts

def getThreeValues(expenses):
    for number in expenses:
        for other_number in expenses:
            for another_number in expenses:
                if(number+other_number+another_number==2020):
                    return [number,other_number,another_number]

    return (None, None)

def multiplyThreeNumbers(numbers):
    return numbers[0]*numbers[1]*numbers[2]


expenses = populateExpenses()
numbers = getThreeValues(expenses)
if numbers[0]!=None and numbers[1]!=None and numbers[2]!=None:
    print(multiplyThreeNumbers(numbers))
else:
    print("Unable to multiply numbers")


#Alternative Method
found_numbers = []
for element in expenses:
    for element2 in expenses:
        x = 2020 - element - element2
        if x in expenses and x not in found_numbers:
            found_numbers.append(x)

if len(found_numbers) == 3:
    print("Total = ",found_numbers[0]*found_numbers[1]*found_numbers[2])
else:
    print("More than 3 numbers ERROR")