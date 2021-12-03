import math
import os

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []

for line in inFile:
    output += 1
    temp = line.replace("\n","").split(" ")
    temp[1] = int(temp[1])
    myList.append(temp)

# print("Number of Items: " + str(output))
# print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
horizontal = 0
depth = 0

for entry in myList:
    if entry[0] == "forward":
        horizontal += entry[1]
    elif entry[0] == "down":
        depth += entry[1]
    else:
        depth -= entry[1]

print("horizontal x depth = answer")
print(str(horizontal) + " x " + str(depth) + " = " + str(horizontal*depth))

print("\n========== Part 2 ==========")
aim = 0
horizontal = 0
depth = 0

for entry in myList:
    if entry[0] == "forward":
        horizontal += entry[1]
        depth += aim * entry[1]
    elif entry[0] == "down":
        aim += entry[1]
    else:
        aim -= entry[1]

print("horizontal x depth = answer")
print(str(horizontal) + " x " + str(depth) + " = " + str(horizontal*depth))