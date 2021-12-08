import math

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []

for line in inFile:
    myList = line.replace("\n","")
    myList = myList.split(",")
    myList = map(int, myList)
    myList.sort()

# Sort list into dict of values
values = {}
for key in range(9):
    values[key] = myList.count(key)

# print("List: " + str(values) + "\n")

print("\n========== Part 1&2 ==========")

days = 256 # Adjust this depending on if it's day 1 or 2
for day in range(days):
    newFish = values[0]
    for vals in range(8): # Shift values down one day
        values[vals] = values[vals+1]
    values[6] += newFish
    values[8] = newFish

totalFish =0
for key in values:
    totalFish += values[key]
print(totalFish)