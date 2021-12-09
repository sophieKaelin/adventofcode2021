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
        minPosition = option

print(minFuelCost)

print("\n========== Part 2 ==========")

minFuelCost = sys.maxint
minPosition = options[0]
for option in options:
    curFuelCost = 0
    for crab in myList:
        dist = abs(option - crab)+1 # Plus one because the induction formula goes 0 + 1 + 2 + ... dist
        curFuelCost += dist*(dist-1)/2
    if curFuelCost < minFuelCost:
        minFuelCost = curFuelCost
        minPosition = option

print(minFuelCost)