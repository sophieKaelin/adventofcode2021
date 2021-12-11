print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []

for line in inFile:
    temp = line.replace("\n","")
    myList.extend(map(int, temp))

print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")

def getAdjacent(i, myList):
    adj = [i-1, i+1, i-1, i+10, i-11, i+9, i + 11, i-9]
    return [item for item in adj if item >= 0 and item < 100]

def shineAdjacent(i, myList):
    adj = getAdjacent(i, myList)
    adj = [item for item in adj if item not in flashed]
    for index in adj:
        if myList[index] == 10:
            continue
        elif myList[index] == 9:
            myList[index] +=1
            flashed.append(index)
            shineAdjacent(index, myList)
        else:
            myList[index] += 1

flashes = 0
for loop in range(1):
    flashed = []
    for i in range(len(myList)):
        if i not in flashed: # Skip if already flashing
            myList[i] += 1
            if myList[i] == 10:
                flashed.append(i)
                shineAdjacent(i, myList)

    flashes += len(flashed)
    for i in flashed:
        myList[i] = 0   

print(sorted(flashed))
print(flashes==35)
