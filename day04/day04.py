import re

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
winningCard, winningNumber = 0, 0
bingoNumbers = [[0] * 5 for i in range(len(myList))]
bingo = False
for number in numbers:
    for row in range(len(myList)):
        if number in myList[row]:
            index = myList[row].index(number)
            bingoNumbers[row][index] = 1 # Mark off each time number is 'numbers' appears in lists
            # Check if there is 5 in a row or column
            if 0 not in bingoNumbers[row] or bingoNumbers[row - row%5][index] ==1 and bingoNumbers[row - row%5+1][index]==1  and bingoNumbers[row - row%5 + 2][index]==1  and bingoNumbers[row - row%5+3][index]==1  and bingoNumbers[row - row%5+4][index]==1:
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

print("\n========== Part 2 ==========")

def removeCard(row):
    for i in reversed(range(row, row+5)):
        myList.pop(i)
        bingoNumbers.pop(i)

winningCard, winningNumber = 0, 0
boardsRemaining = len(myList)/5
bingoNumbers = [[0] * 5 for i in range(len(myList))]
bingo = False

for number in numbers:
    cardsToDelete = []
    for row in range(len(myList)):
        if number in myList[row]:
            index = myList[row].index(number)
            bingoNumbers[row][index] = 1 # Mark off each time number is 'numbers' appears in lists
            # Check if there is 5 in a row or column
            if 0 not in bingoNumbers[row] or bingoNumbers[row - row%5][index] ==1 and bingoNumbers[row - row%5+1][index]==1  and bingoNumbers[row - row%5+2][index]==1  and bingoNumbers[row - row%5+3][index]==1  and bingoNumbers[row - row%5+4][index]==1:
                winningCard = row - row%5
                if(boardsRemaining == 1):
                    bingo = True
                    break
                boardsRemaining -=1
                cardsToDelete.append(winningCard)
                row += 5
    for item in reversed(cardsToDelete): # Remove list of cards that have bingo
        removeCard(item)
    if bingo == True:
        winningNumber = number
        break

# Find sum of unmarked numbers on winning Card
totalWinningBoard = 0
for row in range(0,5):
    for column in range(0, 5):
        if bingoNumbers[row][column] == 0:
            totalWinningBoard += myList[row][column]

# Calculation
print(winningNumber * totalWinningBoard)