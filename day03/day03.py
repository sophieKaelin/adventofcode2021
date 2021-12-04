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

def getIndexOf0and1s(_list, bit): # Positions of all items with 0 at index 'bit'
    ones, zeroes = [],[]
    for itemIndex in range(len(_list)): # Loop through list of items
            if(_list[itemIndex][bit] == '1'):
                ones.append(itemIndex)
            else:
                zeroes.append(itemIndex)
    return zeroes, ones

def mostOrLeastCommonNarrowed(bit, _list, mode):
    if bit == 12 or len(_list) == 1:
        return int(_list[0],2)
    _0Indices, _1Indices = getIndexOf0and1s(_list, bit)
    # Delete Elements that are least or most common, depending on "mode"
    if (len(_0Indices) <= len(_1Indices) and mode == "least") or (len(_0Indices) > len(_1Indices) and mode == "most") :
        deleteElements(_1Indices, _list)
    else:
        deleteElements(_0Indices, _list)
    return mostOrLeastCommonNarrowed(bit+1, _list, mode)

OxygenRate = mostOrLeastCommonNarrowed(0, list(myList), "most")
C02Rate = mostOrLeastCommonNarrowed(0, list(myList), "least")

print("C02 Rate:    " + str(C02Rate))
print("Oxygen Rate: " + str(epsilonRate))
print("Quotient = " + str(C02Rate * epsilonRate))
print(3385170 == C02Rate * OxygenRate)