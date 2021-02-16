
def speak(spoken, last, turn):

    if len(spoken[last])>1:
        current = spoken[last][-1]-spoken[last][-2]
    else:
        current = 0

    print("Turn", turn, "I speak", current)

    if spoken.get(current) == None:
        spoken[current] = [turn]
    else:
        spoken[current].append(turn)

    return spoken, current


starting = [0,3,6]
spoken = dict()

for i,n in enumerate(starting):
    spoken[n] = [i+1]
    print("Turn", i+1, "I speak", n)

    if i == len(starting)-1:
        turn = i+2
        last = n

while turn != 11:
    spoken, last = speak(spoken, last, turn)
    turn += 1
