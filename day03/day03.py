import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []

for line in inFile:
    output += 1
    temp = line.replace("\n","")
    myList.append(temp)
itemLen = len(myList[0])

# print("Number of Items: " + str(output))
# print("List: " + str(myList) + "\n")

# ========== COMMON FUNCTIONS ==========
def mostCommon(_range, _list):
    counter = [0]*_range
    # Combine all first values, combine all second values etc. Pos values are mostly 1's, neg values are mostly 0's
    for code in _list: 
        for i in range(_range):
            if(code[i] == '1'):
                counter[i] +=1
            else:
                counter[i] -=1
    return counter

def deleteElements(indices, _list):
    for i in reversed(indices):
        _list.pop(i)

print("\n========== Part 1 ==========")

counter = mostCommon(itemLen, myList)

# Determine Gamma and Epsilon Rate
gammaRate = ''
epsilonRate = ''
for num in counter:
    if num > 0:
        gammaRate += '1'
        epsilonRate += '0'
    else:
        gammaRate += '0'
        epsilonRate += '1'

# Generate Results
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate,2)
print("GAMMA:   " + str(gammaRate))
print("EPSILON: " + str(epsilonRate))
print("Quotient = " + str(gammaRate * epsilonRate))

print("\n========== Part 2 ==========")

OxygenList = list(myList)
OxygenRate = ''

for bit in range(12): # Position in the item
    _0Indices = [] # Positions of all items with 0 at index 'bit'
    _1Indices = [] # Ditto ^
    if len(OxygenList) == 1:
        OxygenRate = OxygenList[0]
        break
    for itemIndex in range(len(OxygenList)): # Loop through list of items
        if(OxygenList[itemIndex][bit] == '1'):
            _1Indices.append(itemIndex)
        else:
            _0Indices.append(itemIndex)
    # Find most common
    if len(_0Indices) <= len(_1Indices):
        deleteElements(_0Indices, OxygenList)
    else:
        deleteElements(_1Indices, OxygenList)
OxygenRate = int(OxygenList[0],2)

C02List = list(myList)
C02Rate = ''

for bit in range(12): # Position in the item
    _0Indices = [] # Positions of all items with 0 at index 'bit'
    _1Indices = [] # Ditto ^
    if len(C02List) == 1:
        C02Rate = C02List[0]
        break
    for itemIndex in range(len(C02List)): # Loop through list of items
        if(C02List[itemIndex][bit] == '1'):
            _1Indices.append(itemIndex)
        else:
            _0Indices.append(itemIndex)
    # Find least common
    if len(_0Indices) <= len(_1Indices):
        deleteElements(_1Indices, C02List)
    else:
        deleteElements(_0Indices, C02List)
C02Rate = int(C02List[0],2)

print("C02 Rate:    " + str(C02Rate))
print("Oxygen Rate: " + str(epsilonRate))
print("Quotient = " + str(C02Rate * epsilonRate))