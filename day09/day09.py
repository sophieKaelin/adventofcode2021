import sys
print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []

for line in inFile:
    temp = line.replace("\n","")
    temp = list(temp)
    myList.append(temp)

cols = len(myList[0])
rows = len(myList)
print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
def inRange(r, c):
    if (r > 0 or r >= rows) and (c > 0 or c >= cols):
        return myList[r][c]
    else:
        return sys.maxInt

riskLevelSum = 0
for r in myList:
    for c in myList[r]:
        surrounding = [inRange(r-1, c), inRange(r+1, c), inRange(r, c-1), inRange(r, c+1)]
        # If [r][c] is smaller than each in the list
            # Save that as a small one
            # If any surrounding are marked as a small one, remove the small one field from theirs
            # skip 1 column (next won't be smaller, we just checked that)
            # THIS WONT WORK -> BEST TO MARK ALL THE SMALLER ONES, AND THEN GO THROUGH AGAIN AND NARROW THEM ALL DOWN UNTIL THERE ARE NO ADJACENT SMALL NUMBERS
print(riskLevelSum == 15)