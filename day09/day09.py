import sys
print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []

for line in inFile:
    temp = line.replace("\n","")
    temp = list(temp)
    temp = map(int, temp)
    myList.append(temp)

cols = len(myList[0])
rows = len(myList)
print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
smallest = []
def inRange(r, c):
    if (r >= 0 and r < rows) and (c >= 0 and c < cols):
        return myList[r][c]
    else:
        return sys.maxint

riskLevelSum = 0
# Get all the smallest by comparing neighbors
for r in range(rows):
    for c in range(cols):
        surrounding = [inRange(r-1, c), inRange(r+1, c), inRange(r, c-1), inRange(r, c+1)]
        if all(x > myList[r][c] for x in surrounding): # If [r][c] is smaller than each in the list
            smallest.append(r*10 + c)

print(smallest)

# Check if there are any numbers in smallest which are adjacent
# for i in reversed(smallest):
    # smallest = True
    # if smallest[i] - 1 in smallest:
        
    # Check if there are any values smallest[i] - 1, smallest[i] + 1, smallest[i]-rows, smallest[i]+rows
    # if not smallest:
    #     smallest.remove(i)
    # If item is not smallest, delete.
    # print("doing something later")

# Calculate Risk Level Sum
for i in smallest:
    riskLevelSum += myList[i/10][i%10]
riskLevelSum += len(smallest)

print(riskLevelSum == 15)

# Get list of smallest values
# Then, loop through list of indexes, check if there is any adjacent, if there is, only keep the smallest