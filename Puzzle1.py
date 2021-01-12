def populateExpenses():
    expense_amounts = []
    fh = open("ExpenseReport.txt")
    for line in fh:
        expense_amounts.append(int(line))

    return expense_amounts

def getTwoValues(expenses):

    for number in expenses:
        for other_number in expenses:
            print(number, other_number)
            if(number+other_number==2020):
                print("Bingo")
                return (number,other_number)

    return (None, None)

def multiplyTwoNumbers(number1,number2):
    return number1*number2


expenses = populateExpenses()
number1,number2 = getTwoValues(expenses)
if number1!=None and number2!=None:
    print(multiplyTwoNumbers(number1,number2))
else:
    print("Unable to multiply numbers")

#Alternative Method
found_numbers = []
for element in expenses:
    x = 2020 - element
    if x in expenses:
        found_numbers.append(x)

if len(found_numbers) == 2:
    print("Total = ",found_numbers[0]*found_numbers[1])
else:
    print("More than 2 numbers ERROR")

