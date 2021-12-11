print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []

for line in inFile:
    temp = line.replace("\n","")
    myList.append(temp)

# print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
corrupt = 0
closeChars = ['}', ']', ')', '>']
points = {'}':1197, ']':57, ')':3, '>':25137}

def corruptionCalculator(line):
    for c in line:
        if c in closeChars:
            return points[c]
    return 0

for line in myList:
    lineCopy = "" + line
    prevSize = len(lineCopy)
    while len(lineCopy) > 0:
        if "{}" in lineCopy:
            lineCopy = lineCopy.replace("{}", "")
        if "()" in lineCopy:
            lineCopy = lineCopy.replace("()", "")
        if "[]" in lineCopy:
            lineCopy = lineCopy.replace("[]", "")
        if "<>" in lineCopy:
            lineCopy = lineCopy.replace("<>", "")

        if len(lineCopy) == prevSize: # There was nothing removed
            if any(sym in lineCopy for sym in closeChars):
                corrupt += corruptionCalculator(lineCopy)
            break
        prevSize = len(lineCopy)
print(corrupt)