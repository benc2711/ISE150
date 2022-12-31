'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 16
'''
import die as die
    # Function: rollDice
    # Purpose: rolls a list of dice
    # Parameters: die list
    # Side effects: none
    # Returns: sum
def rollDice(dList):
    sum =0
    for x in dList:
        sum += x.roll()
    return sum
# Function: printDice
    # Purpose: Converts a die object to a string
    # Parameters: die list
    # Side effects: prints to console
    # Returns: none
def printDice(dList):
    for x in range(len(dList)):
        print("#" + str(x+1) + ":" + dList[x].__str__())
# Function: Main
    # Purpose: UI
    # Parameters: none
    # Side effects: Prints to console
    # Returns: none
def main():
    dSides = input("How many sides does your die have? ")
    dNumber = input("How many dice do you have? ")
    dList =[]
    for x in range(int(dNumber)):
        dList.append(die.die(int(dSides)))

    rollAnswer = "y"
    while rollAnswer == "y":
        rollAnswer = input("Roll (y/n) ")
        rollDice(dList)
        printDice(dList)
    print("Goodbye")

main()