import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []

for line in inFile:
    output += 1
    temp = int(line.replace("\n",""))
    myList.append(temp)

# print("Number of Items: " + str(output))
# print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
increasedVal = 0
for i in range(1,output):
    if myList[i-1] < myList[i]:
        increasedVal +=1
print("It has increased " + str(increasedVal) + " times")

print("\n========== Part 2 ==========")
increasedValSum = 0
previous = myList[0] + myList[1] + myList[2]
for i in range(1,output-2):
    curSum = myList[i] + myList[i+1] + myList[i+2]
    if previous < curSum:
        increasedValSum +=1
    previous = curSum
print("It has increased " + str(increasedValSum) + " times")