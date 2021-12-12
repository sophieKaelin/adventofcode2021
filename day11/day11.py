import sys
print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []

for line in inFile:
    temp = line.replace("\n","")
    myList.extend(map(int, temp))

print("List: " + str(myList) + "\n")

def getAdjacent(i):
    adj = []
    r = i/10
    c = i%10
    if r == 0 and c == 0: # Top Left
        adj.extend([i+1,i+11,i+10])
    elif r == 0 and c == 9: # Top Right
        adj.extend([i-1,i+9,i+10])
    elif r == 9 and c == 0: # Bottom Left
        adj.extend([i+1,i-9,i-10])
    elif r == 9 and c == 9: # Bottom Right
        adj.extend([i-1,i-11,i-10])
    elif c == 0:
        adj.extend([i+1, i-10, i+10, i-9, i + 11])
    elif c == 9:
        adj.extend([i-1, i-10, i+10, i+9, i -11])
    elif r == 0:
        adj.extend([i-1, i+1, i+10, i+9, i + 11])
    elif r == 9:
        adj.extend([i-1, i+1, i-10, i-9, i - 11])
    else:
        adj.extend([i-1, i+1, i-10, i+10, i-11, i+9, i + 11, i-9])
    return [i for i in adj if i >= 0 and i < 100]

def shineAdjacent(i, myList):
    adj = getAdjacent(i)
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

print("\n========== Part 1 ==========")

flashes = 0
for loop in range(100):
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
print(flashes)

print("\n========== Part 2 ==========")

loop = 0
while True:
    flashed = []
    for i in range(len(myList)):
        if i not in flashed: # Skip if already flashing
            myList[i] += 1
            if myList[i] == 10:
                flashed.append(i)
                shineAdjacent(i, myList)

    loop += 1

    if len(flashed) == 100:
        break
    for i in flashed:
        myList[i] = 0   

print(loop)
