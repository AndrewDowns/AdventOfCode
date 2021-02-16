def readCode():
    code = []
    fh = open("gameCode.txt")
    for line in fh:
        d = dict()
        d["action"] = line.strip()
        d["used"] = False
        code.append(d)
    return code

def runCode(acc, code):
    infiniteLoop = False
    current = 0

    while not infiniteLoop:
        current_line = code[current]
        print(current_line["action"]," Line ", current+1)
        if current_line["used"]:
            #If the line has been run before
            infiniteLoop = True
            print("ERROR")
        else:
            #If it hasn't run the line
            code[current]["used"] = True
            current_action_info = current_line["action"].split(" ")

            if current_action_info[0] == "acc":
                # Add to the acc
                if current_action_info[1].startswith("+"):
                    acc+= int(current_action_info[1].replace("+",""))
                elif current_action_info[1].startswith("-"):
                    acc -= int(current_action_info[1].replace("-", ""))

                current+=1

            elif current_action_info[0] == "jmp":
                #Perform a jump
                if current_action_info[1].startswith("+"):
                    current+= int(current_action_info[1].replace("+",""))
                elif current_action_info[1].startswith("-"):
                    current-= int(current_action_info[1].replace("-", ""))

            elif current_action_info[0] == "nop":
                current += 1

            if current >= len(code):
                print("Game Over")
                infiniteLoop = True

    return acc

acc = 0
code = readCode()
acc = runCode(acc, code)
print(acc)


