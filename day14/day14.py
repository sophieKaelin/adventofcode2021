from collections import Counter
print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = {}
template = inFile.readline().replace("\n","")

for line in inFile:
    temp = line.replace("\n","")
    temp = temp.split(" -> ")
    if len(temp) > 1:
        myList[temp[0]] = temp[1]

# Store number of times a character appears
instances = dict(Counter(template))

valuesForInstances = list(set(myList.values()))

for item in valuesForInstances:
    if item not in instances:
        instances[item] = 0

print("List: " + str(myList) + "\n")
print("Template: " + str(template) + "\n")
print("Instances: " + str(instances) + "\n")

print("\n========== Part 1 ==========")
steps = 10
for loop in range(steps):
    print(loop)
    tempList = list(template)
    newTemplate = ""
    for i in range(0, len(template)-1):
        newTemplate += tempList[i] + myList[template[i:i+2]]
        instances[myList[template[i:i+2]]] += 1
    newTemplate += tempList[len(tempList)-1]
    template = newTemplate

_min = min(instances, key=instances.get)
_max = max(instances, key=instances.get)

print(instances[_max] - instances[_min])
