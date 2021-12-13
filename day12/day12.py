print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = {}

for line in inFile:
    temp = line.replace("\n","")
    temp = temp.split("-")
    if temp[0] in myList:
        myList[temp[0]].append(temp[1])
    else:
        myList[temp[0]] = [temp[1]]
    if temp[1] in myList:
        myList[temp[1]].append(temp[0])
    else:
        myList[temp[1]] = [temp[0]]

print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")

def findPaths(curKey, used):
    paths = 0
    if curKey == 'end' or curKey not in myList:
        return 1
    for item in myList[curKey]:
        if item != 'start' and item not in used:
            if str.islower(item):
                paths += findPaths(item, used+"-"+item)
            else:
                paths += findPaths(item, used)
    return paths
print(findPaths('start', ""))