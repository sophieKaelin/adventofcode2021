import math, re, os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []
maxY, maxX = 0, 0

for line in inFile:
    output += 1
    temp = line.replace("\n","")
    temp = re.split(' -> |,', temp)
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    maxY = max(maxY, temp[1], temp[3])
    maxX = max(maxX, temp[0], temp[2])
    myList.append(temp)

# print("Number of Items: " + str(output))
# print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
coordinates = {}

# TODO: Need a more efficient way of doing it!!!!
for coords in myList:
    for x in range(coords[0], coords[2]+1):
        for y in range(coords[1], coords[3]+1):
            if (x, y) in coordinates:
                coordinates[(x, y)] += 1
            else:
                coordinates[(x, y)] = 1

print(coordinates)