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

print("\n========== Part 1 ==========")
coordinates = {}

for coords in myList:
    if coords[0] == coords[2]: # Vertical Line
        _min = min(coords[1], coords[3])
        _max = max(coords[1], coords[3])
        for y in range(_min, _max+1):
            if (coords[0], y) in coordinates:
                coordinates[(coords[0], y)] += 1
            else:
                coordinates[(coords[0], y)] = 1
    elif coords[1] == coords[3]: # Horizontal Line
        _min = min(coords[0], coords[2])
        _max = max(coords[0], coords[2])
        for x in range(_min, _max+1):
            if (x, coords[1]) in coordinates:
                coordinates[(x, coords[1])] += 1
            else:
                coordinates[(x, coords[1])] = 1

counter = 0
for item in coordinates:
    if coordinates[item] >= 2:
        counter +=1

print(counter)

print("\n========== Part 2 ==========")

def addStraightLine(coordinates, v1, v2, v3, mode):
    _min = min(v1, v2)
    _max = max(v1, v2)
    for xy in range(_min, _max+1):
        if mode == 'v':
            if (v3, xy) in coordinates:
                coordinates[(v3, xy)] += 1
            else:
                coordinates[(v3, xy)] = 1
        else:
            if (xy, v3) in coordinates:
                coordinates[(xy, v3)] += 1
            else:
                coordinates[(xy, v3)] = 1

coordinates = {}
for points in myList:
    if points[0] == points[2]: # Vertical Line
        addStraightLine(coordinates, points[1], points[3], points[0], 'v')
    elif points[1] == points[3]: # Horizontal Line
        addStraightLine(coordinates, points[0], points[2], points[1], 'h')
    else: # Diagonal Line
        gradient = (points[1] - points[3]) / (points[0]-points[2])
        if gradient > 0: # Positive Gradient start on lowest Y
            if points[1] < points[3]:
                _min = points[1]
                x = points[0]
                _max = points[3]
            else:
                _min = points[3]
                x = points[2]
                _max = points[1]
            for y in range(_min, _max+1):
                if (x, y) in coordinates:
                    coordinates[(x, y)] += 1
                else:
                    coordinates[(x, y)] = 1
                x +=1
        else : # Negative Gradient, Start on lowest X, decrease the Y value.
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
                y -=1
counter = 0
for item in coordinates:
    if coordinates[item] >= 2:
        counter +=1

print(counter == 19851)