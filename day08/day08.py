import collections

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []


for line in inFile:
    # Input line
    temp = line.replace("\n","")
    temp = temp.split("|")
    # Signal Pattern sorting
    temp[0] = temp[0].split(" ")
    temp[0].pop(10)
    temp[0] = sorted(temp[0], key=len)

    for i in range(10): # Sort values so they are alphabetical 
        temp[0][i] = "".join(sorted(temp[0][i]))
    
    # Output value sorting
    temp[1] = temp[1].split(" ")
    temp[1].pop(0)
    for i in range(4):
        temp[1][i] = "".join(sorted(temp[1][i]))
    myList.append(temp) # Add items to list

# print("List: " + str(myList) + "\n")

# ========== SOLUTION ==========

counter1 = 0
counter2 = 0

for line in myList:
    numbers = {1:line[0][0], 7:line[0][1], 4:line[0][2], 8:line[0][9]} # Default, must be these values
    characters = {}

    # Find 'a' = chars in '7' minus chars in '1'
    characters['a'] = numbers[7].translate(None, ''.join(list(numbers[1])))

    # Find 'c' = 1 character from "1" is common in all but 1 combo ('c' not in "2")
    combined = collections.Counter("".join(line[0]))
    characters['c'] = combined.keys()[combined.values().index(9)]

    # Find 'b' = characters in "1" - 'c'
    characters['b'] = numbers[1].replace(characters['c'], "")

    # length = 5, which one doesn't have b value is 5. Other letter missing is 'e'
    for index in range(3, 6):
        if characters['b'] not in line[0][index]:
            numbers[5] = line[0][index]
            characters['e'] = "abcdefg".translate(None, ''.join(list(numbers[5]))).replace(characters['b'],"")
        elif characters['c'] not in line[0][index]:
            numbers[2] = line[0][index]
        else:
            numbers[3] = line[0][index]
    
    # Find F -> whatever is missing from "2" characters + 'c'
    characters['f'] = "abcdefg".translate(None, ''.join(list(numbers[2]))).replace(characters['c'],"")

    # length = 6, which one doesn't have b value is '6'. which one doesn't have e value is '9'. Which ever is left is '0' and the one missing is "g"
    for index in range(6, 9):
        if characters['b'] not in line[0][index]:
            numbers[6] = line[0][index]
        elif characters['e'] not in line[0][index]:
            numbers[9] = line[0][index]
        else:
            numbers[0] = line[0][index]
            characters['g'] = "abcdefg".translate(None, ''.join(list(numbers[0])))
    
    # Find D. Remove 'a' from '9'. compare '4' and '9' which ever one is different is D
    characters['d'] = numbers[9].translate(None, ''.join(list(numbers[4]))).replace(characters['a'],'')

    # PART 1 SOLUTION Check for 1,4,7,8 in the output values
    counter1 += line[1].count(numbers[4])
    counter1 += line[1].count(numbers[1])
    counter1 += line[1].count(numbers[7])
    counter1 += line[1].count(numbers[8])

    # PART 2 find number and add to counter
    output = ""
    for vals in line[1]:
        output += str(numbers.keys()[numbers.values().index(vals)])
    counter2 += int(output)

print("\n========== Part 1 ==========")
print("COUNTER: " + str(counter1))
print("\n========== Part 2 ==========")
print("COUNTER: " + str(counter2))