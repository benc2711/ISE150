'''
Ben Crotty
ISE150, Spring 2021
bcrotty@usc.edu
Homework 10
'''
import hero

#Function: printMenu
# Purpose: Prints a set men
# Parameters: none
# Side effects: prints to console
# Returns: none
def printMenu():
    print("Choose an option: \n1. Load Heros \n2. Print Hero Roster \n3. Hero Fight! \n4. Quit")

#Function: printRoster
# Purpose: Prints all of the heroes and their powers
# Parameters: hero list
# Side effects: prints to console
# Returns: none
def printRoster(hList):
    hCount = len(hList)
    print("The following " + str(hCount) + " heroes were loaded.")
    for h in hList:
        superman = hero.hero(h)
        #Creates my object and titles it as a variable called superman
        print("********************************************")
        print(superman.getName() + " has the following powers...")
        #Uses the getter function and str funciton below to print the name of the hero and their powers
        print("\t" + superman.__str__())
    print("********************************************")

#Function: loadHeroes
# Purpose: Takes the a file and reads each line and converts each line into an element of a list
# Parameters: file
# Side effects: prints number of heroes / number of lines
# Returns: the above mentioned list of heroes
def loadHeros(file):
    fileIn = open(file, 'r')
    hList = []
    counter = 0
    #Opens the file sets an empty list and sets counter to zero
    for line in fileIn:
        hList.append(line)
        counter+=1
        #Has counter increment per hero and appends the hero line to the hero list
    print("Loaded " + str(counter) + " heros.")
    return hList



#Function: main
# Purpose: Serves as the UI
# Parameters: none
# Side effects: prints to console
# Returns: none
def main():

    uInput = ""
    while uInput != "4":
        printMenu()
        uInput = input()
        if uInput == "1":
            file = input("Please enter the hero file")
            hlist = loadHeros(file)
        if uInput == "2":
            printRoster(hlist)
        if uInput == "3":
            print("Stay tuned for the fight of the century")
        if uInput == "4":
            print("Goodbye!")

main()