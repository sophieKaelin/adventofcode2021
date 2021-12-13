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

print("\n========== Part 1 & 2 ==========")

for code in instr:
    changeIdx = 0
    if code[0] is 'y':
        changeIdx = 1
    for i in range(len(coordinates)):
        if coordinates[i][changeIdx] >= code[1]:
            coordinates[i][changeIdx] = 2*code[1] - coordinates[i][changeIdx]

    coordinates = list(set(tuple(sub) for sub in coordinates)) # Eliminate duplicate entries
    coordinates = map(list, coordinates)

print(coordinates)
print(len(coordinates))