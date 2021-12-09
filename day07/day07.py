import math, sys
print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []

for line in inFile:
    output += 1
    temp = line.replace("\n","")
    temp = temp.split(",")
    temp = map(int, temp)
    myList = temp

options = list(dict.fromkeys(myList)) # Calculate all possible positions (remove duplicates)

# print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
minFuelCost = sys.maxint
minPosition = options[0]
for option in options:
    curFuelCost = 0
    for crab in myList:
        curFuelCost += abs(option - crab)
    if curFuelCost < minFuelCost:
        minFuelCost = curFuelCost
        minPosition = crab

print(minFuelCost)

