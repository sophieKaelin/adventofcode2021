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

# def getPointsOnLine(points, _list):
#     if points[0] == points[2]: # Vertical Line
#         _min = min(points[1], points[3])
#         _max = max(points[1], points[3])
#         for y in range(min, max+1):
#             if (points[0], y) in coordinates:
#                 coordinates[(points[0], y)] += 1
#             else:
#                 coordinates[(points[0], y)] = 1
#     elif points[1] == points[3]: # Horizontal Line
#         _min = min(points[0], points[2])
#         _max = max(points[0], points[2])
#         for x in range(min, max+1):
#             if (x, points[1]) in coordinates:
#                 coordinates[(x, points[1])] += 1
#             else:
#                 coordinates[(x, points[1])] = 1
#     else:
#         gradient = (points[1] - points[3]) / (points[0]-points[2])
#         if gradient > 0:
#             _min = min(points[1], points[3])
#             _max = max(points[1], points[3])
#             for y in range(min, max+1):
#                 if (points[0], y) in coordinates:
#                     coordinates[(points[0], y)] += 1
#                 else:
#                     coordinates[(points[0], y)] = 1
#             print("pos")
#         elif gradient < 0:
#             print("neg")       
#         else:
#             print("straight")
#         return [] # Return a list of tuples

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
        print("VERTICAL")
    elif coords[1] == coords[3]: # Horizontal Line
        _min = min(coords[0], coords[2])
        _max = max(coords[0], coords[2])
        for x in range(_min, _max+1):
            if (x, coords[1]) in coordinates:
                coordinates[(x, coords[1])] += 1
            else:
                coordinates[(x, coords[1])] = 1
        print("HORIZONTAL")

# print(coordinates)
counter = 0
for item in coordinates:
    # print(coordinates[item])
    if coordinates[item] >= 2:
        counter +=1

print(counter)

print("\n========== Part 2 ==========")