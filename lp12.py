'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab Practical 12
'''

#Function: processNumberFile
# Purpose: gives the list of numbers in an array
# Parameters: takes a file to get the list
# Side effects: none
# Returns: list
def processNumberFile(fileName):
    fileIn = open(fileName, "r")
    numberlist =[]
    for line in fileIn:
        number = int(line.strip())
        numberlist.append(number)
    fileIn.close()
    return numberlist
#Function: getMax
# Purpose: finds the max of the given integer list
# Parameters: takes an integer list
# Side effects: none
# Returns: maximum value
def getMax(intList):
    max = intList[0]
    for x in range(len(intList)):
        if max < intList[x]:
            max = intList[x]
    return max

#Function: getMin
# Purpose: finds the minimum value
# Parameters: integer list
# Side effects: none
# Returns: minimum value
def getMin(intList):
    min = intList[0]
    for x in range(len(intList)):
        if min > intList[x]:
            min = intList[x]
    return min

#Function: getAbg
# Purpose: gets the average of the list
# Parameters: integer list
# Side effects: none
# Returns: returns the average of the function
def getAvg(intList):
    sum = 0
    counter = 0
    for x in range(len(intList)):
        sum += intList[x]
        counter += 1
    average = sum / counter
    return average
#Function: Main
# Purpose: acts as user input and UI
# Parameters: none
# Side effects: prints to console
# Returns: none
def main():
    userInput = input("Number File: ")
    integerList = processNumberFile(userInput)
    print("Max = " + str(getMax(integerList)))
    print("Min = " + str(getMin(integerList)))
    print("Avg = " + str(getAvg(integerList)))
main()