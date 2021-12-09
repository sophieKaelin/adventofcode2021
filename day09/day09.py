print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []

for line in inFile:
    temp = line.replace("\n","")
    myList.append(temp)

print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")