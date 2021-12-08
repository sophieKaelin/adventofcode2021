print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
output = 0
myList = []

for line in inFile:
    output += 1
    temp = line.replace("\n","")
    myList.append(temp)
itemLen = len(myList[0])

# print("Number of Items: " + str(output))
print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")