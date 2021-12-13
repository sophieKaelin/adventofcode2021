import sys, copy
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
smallest = [] # Indexes of smallest numbers

def inRange(r, c): # Checks if the index is valid
    if (r >= 0 and r < rows) and (c >= 0 and c < cols):
        return myList[r][c]
    else:
        return sys.maxint

def getSurrounding(r, c, _list): # Will get surrounding items and confirms they also exist in list
    surrounding = []
    if r-1 >= 0 and r-1 < rows and [r-1,c] in _list:
        surrounding.append([r-1,c])
    if r+1 >= 0 and r+1 < rows and [r+1,c] in _list:
        surrounding.append([r+1,c])
    if c-1 >= 0 and c-1 < cols and [r,c-1] in _list:
        surrounding.append([r,c-1])
    if c+1 >= 0 and c+1 < cols and [r,c+1] in _list:
        surrounding.append([r,c+1])
    return surrounding

# Get all the smallest by comparing neighbors
for r in range(rows):
    for c in range(cols):
        surrounding = [inRange(r-1, c),inRange(r+1, c),inRange(r, c-1),inRange(r, c+1)]
        if len(surrounding) == 1 or all(x > myList[r][c] for x in surrounding): # If [r][c] is smaller than each in the list
            smallest.append([r,c])

# Check if there are any numbers in smallest which are adjacent, and only keep the smallest of those
smallestOfSmallest = []
print(str(smallest)+"\n")
for coord in smallest:
    surrounding = getSurrounding(coord[0], coord[1], smallest)
    if len(surrounding) == 0 or all(x > myList[r][c] for x in surrounding): # If [r][c] is smaller than each in the list
        smallestOfSmallest.append([coord[0],coord[1]])

print(smallestOfSmallest)

# Calculate Risk Level Sum
riskLevelSum = 0
for i in smallestOfSmallest:
    riskLevelSum += myList[i[0]][i[1]]
riskLevelSum += len(smallestOfSmallest)

print(riskLevelSum)

print("\n========== Part 2 ==========")

def findBasin(low, marked):
    if low[0] < 0 or low[0] >= rows or low[1] < 0 or low[1] >= cols or myList[low[0]][low[1]] == 9 or low in marked:
        return -1
    marked.append(low)
    return 4 + findBasin([low[0]-1, low[1]], marked) + findBasin([low[0]+1, low[1]], marked) + findBasin([low[0], low[1]-1], marked) + findBasin([low[0], low[1]+1], marked)

# Loop through smallest of smallest and see if there
basins = []
marked = []
for coord in smallestOfSmallest:
    basins.append(1+findBasin(coord, marked))
basins = sorted(basins)
numBasins = len(basins)

print(basins[numBasins-1] * basins[numBasins-2] * basins[numBasins-3])