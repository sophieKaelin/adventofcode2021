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

# print("Number of Items: " + str(output))
# print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")

counter = [0]*12

# Combine all first values, combine all second values etc. Pos values are mostly 1's, neg values are mostly 0's
for code in myList: 
    for i in range(12):
        if(code[i] == '1'):
            counter[i] +=1
        else:
            counter[i] -=1

print(counter)

gammaRate = ''
epsilonRate = ''
for num in counter:
    if num > 0:
        gammaRate += '1'
        epsilonRate += '0'
    else:
        gammaRate += '0'
        epsilonRate += '1'
gammaRate = int(gammaRate, 2)
epsilonRate = int(epsilonRate,2)
print("GAMMA:   " + str(gammaRate))
print("EPSILON: " + str(epsilonRate))
print("Quotient = " + str(gammaRate * epsilonRate))

print("\n========== Part 2 ==========")