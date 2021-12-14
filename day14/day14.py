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

print("List: " + str(myList) + "\n")
print("Template: " + str(template) + "\n")

print("\n========== Part 1 ==========")

for loop in range(10):
    tempList = list(template)
    middle = []
    for i in range(0, len(template)-1):
        middle.append(myList[template[i:i+2]])

    template = ""
    for i in range(0, len(middle)):
        template += tempList[i] + middle[i]
    template += tempList[len(tempList)-1]
    
print(len(template))
instances = Counter(template)
_min = min(instances, key=instances.get)
_max = max(instances, key=instances.get)

print(instances[_max] - instances[_min])
