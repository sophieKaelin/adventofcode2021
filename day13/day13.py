print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
coordinates = []
instr = []

for line in inFile:
    temp = line.replace("\n","")
    temp = temp.split(",")
    if len(temp) == 2:
        temp = map(int, temp)
        coordinates.append(temp)
    elif len(temp[0]) != 0:
        temp = temp[0][11:]
        temp = temp.split("=")
        temp[1] = int(temp[1])
        instr.append(temp)

print("Coordinates: " + str(coordinates) + "\n")
print("instructions: " + str(instr) + "\n")

print("\n========== Part 1 ==========")

onlyInstruction = instr[0]
if onlyInstruction[0] is 'y':
    for i in range(len(coordinates)):
        if coordinates[i][1] > onlyInstruction[1]:
            coordinates[i][1] = onlyInstruction[1] - (coordinates[i][1] - onlyInstruction[1])
else:
    for i in range(len(coordinates)):
        if coordinates[i][0] > onlyInstruction[1]:
            coordinates[i][0] = onlyInstruction[1] - (coordinates[i][0] - onlyInstruction[1])

coordinates = list(set(tuple(sorted(sub)) for sub in coordinates))

print(len(coordinates))