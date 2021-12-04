import math, os, re

print("\n========== INPUTING FILE ==========")

inFile = open("input.txt")
myList = []
output = 0
numbers = ''

for line in inFile:
    if output == 0: # First line is the called numbers
        numbers = line.split(",")
        numbers = map(int, numbers)
    elif output == 1: # Skip second blank line
        output +=1
        continue
    else:
        if line != '\n': # Remove break lines between cards
            line = line.replace("\n","")
            sublist = list(filter(("").__ne__, re.split("  | ", line)))
            sublist = map(int, sublist)
            myList.append(sublist)
    output +=1

# print("List: " + str(myList) + "\n")

print("\n========== Part 1 ==========")
winningCard = 0
winningNumber = 0
bingoNumbers = [[0] * 5 for i in range(len(myList))]
bingo = False
for number in numbers:
    for row in range(len(myList)):
        if number in myList[row]:
            index = myList[row].index(number)
            bingoNumbers[row][index] = 1 # Mark off each time number is 'numbers' appears in lists
            # Check if there is 5 in a row
            if 0 not in bingoNumbers[row]:
                print("row success")
                bingo = True
                winningCard = row - row%5
                break
            # Check if there is 5 in a column
            if bingoNumbers[row/5][index] ==1 and bingoNumbers[row/5+1][index]==1  and bingoNumbers[row/5+2][index]==1  and bingoNumbers[row/5+3][index]==1  and bingoNumbers[row/5+4][index]==1:
                print("column success")
                bingo = True
                winningCard = row - row%5
                break
    if bingo == True:
        winningNumber = number
        break

# Find sum of unmarked numbers on winning row
totalWinningBoard = 0
for row in range(winningCard,winningCard+5):
    for column in range(5):
        if bingoNumbers[row][column] == 0:
            totalWinningBoard += myList[row][column]

# Calculation
print(winningNumber * totalWinningBoard)