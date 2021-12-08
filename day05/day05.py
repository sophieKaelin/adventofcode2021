import re, math

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []
maxY, maxX = 0, 0

for line in inFile:
    output += 1
    temp = line.replace("\n","")
    temp = re.split(' -> |,', temp)
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    temp[2] = int(temp[2])
    temp[3] = int(temp[3])
    maxY = max(maxY, temp[1], temp[3])
    maxX = max(maxX, temp[0], temp[2])
    myList.append(temp)

# print("Number of Items: " + str(output))
# print("List: " + str(myList) + "\n")

# =============== COMMON FUNCTIONS ===================
def addStraightLine(coordinates, v1, v2, v3, mode): # Will enumerate through all points on straight line depending on if vertical or horizontal
    _min = min(v1, v2)
    _max = max(v1, v2)
    for xy in range(_min, _max+1):
        if mode == 'v':
            if (v3, xy) in coordinates: # Increment dict value by 1 if it exists
                coordinates[(v3, xy)] += 1 
            else: # If it doesn't exist, create a new entry
                coordinates[(v3, xy)] = 1
        else:
            if (xy, v3) in coordinates:
                coordinates[(xy, v3)] += 1
            else:
                coordinates[(xy, v3)] = 1

print("\n========== Part 1 ==========")
coordinates = {}

for points in myList:
    if points[0] == points[2]: # Vertical Line
        addStraightLine(coordinates, points[1], points[3], points[0], 'v')
    elif points[1] == points[3]: # Horizontal Line
        addStraightLine(coordinates, points[0], points[2], points[1], 'h')

# Count how many values in dictionary are greater than 2
counter = 0
for item in coordinates:
    if coordinates[item] >= 2:
        counter +=1

print(counter == 6687)

print("\n========== Part 2 ==========")
coordinates = {}

for points in myList:
    if points[0] == points[2]: # Vertical Line
        addStraightLine(coordinates, points[1], points[3], points[0], 'v')
    elif points[1] == points[3]: # Horizontal Line
        addStraightLine(coordinates, points[0], points[2], points[1], 'h')
    else: # Diagonal Line
        gradient = (points[1] - points[3]) / (points[0]-points[2])
        YSlope = 0
        if gradient > 0:
            YSlope = 1
        else:
            YSlope = -1
        if points[0] < points[2]:
            _min = points[0]
            y = points[1]
            _max = points[2]
        else:
            _min = points[2]
            y = points[3]
            _max = points[0]
        for x in range(_min, _max+1):
            if (x, y) in coordinates:
                coordinates[(x, y)] += 1
            else:
                coordinates[(x, y)] = 1              
            y +=YSlope

counter = 0
for item in coordinates:
    if coordinates[item] >= 2:
        counter +=1

print(counter == 19851)