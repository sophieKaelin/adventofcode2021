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

print("\n========== Part 2 ==========")
scores = []
closeChars = ['}', ']', ')', '>']

points = {'{':3, '[':2, '(':1, '<':4}

def brokenCalculator(line):
    if len(line) == 1:
        return points[line]
    return points[line[0]] + 5 * brokenCalculator(line[1:])

for line in reversed(range(len(myList))):
    lineCopy = "" + myList[line]
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
            if not any(sym in lineCopy for sym in closeChars):
                scores.append(brokenCalculator(lineCopy))
            break
        prevSize = len(lineCopy)

scores = sorted(scores)
print(scores[len(scores)/2])
