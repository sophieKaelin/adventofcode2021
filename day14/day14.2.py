# Followed a tutorial to understand this one
# Thanks Anthony  : https://www.youtube.com/watch?v=TIL1JwLtIzw

from collections import Counter
import collections
print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = {}
template = inFile.readline().replace("\n","")

for line in inFile:
    temp = line.replace("\n","")
    temp = temp.split(" -> ")
    if len(temp) > 1:
        myList[temp[0]] = temp[1]

pairs = collections.Counter()
for i in range(len(template)-1): # Initiate with each pair from template
    pairs[template[i:i+2]] += 1

print("List: " + str(myList) + "\n")
print("Template: " + str(template) + "\n")
print("pairs: " + str(pairs) + "\n")


print("\n========== Part 2 ==========")
steps = 40

for loop in range(steps):
    newCounts = collections.Counter() # We need "pairs" for the loop, so count in here
    charCounts = collections.Counter() # Count instances of each character
    for key, value in pairs.items():      
        start = key[0] + myList[key]
        end = myList[key] + key[1]
        
        newCounts[start] += value
        newCounts[end] += value

        charCounts[key[0]] += value
        charCounts[myList[key]] += value
    pairs = newCounts
charCounts[template[-1]] += 1

c = sorted(charCounts.values())
print(c[-1] - c[0])