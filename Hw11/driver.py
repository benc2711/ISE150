'''
Ben Crotty
ISE150, Spring 2021
bcrotty@usc.edu
Homework 11
'''
import hero
import powers
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
    heroList = []
    print("The following " + str(hCount) + " heroes were loaded.")
    for h in hList:
        superhero = hero.hero(h)
        heroList.append(superhero)
        #Creates my object and titles it as a variable called superman
        print("********************************************")
        print(superhero.getName() + " has the following powers...")
        #Uses the getter function and str funciton below to print the name of the hero and their powers
        print("\t" + superhero.__str__())
    print("********************************************")
    return heroList
#Function: loadHeroes
# Purpose: Takes the a file and reads each line and converts each line into an element of a list
# Parameters: file
# Side effects: prints number of heroes / number of lines
# Returns: the above mentioned list of heroes
def loadHeros(file):
    hList = []
    try:
        fileIn = open(file, 'r')
    except:
        "The file cannot be loaded"
        return hList

    counter = 0
    #Opens the file sets an empty list and sets counter to zero
    for line in fileIn:
        hList.append(line)
        counter+=1
        #Has counter increment per hero and appends the hero line to the hero list
    print("Loaded " + str(counter) + " heroes.")
    return hList
#Function: selectHero
# Purpose: selects a hero given by the user from a list of heros
# Parameters: user input and hero list
# Side effects: none
# Returns: hero
def selectHero(hList, prompt):
    return hList[prompt]
#Function: heroCombat
# Purpose: Essentially enacts a lot of object methods to have two heros select random powers and fight
# Parameters: list of hero objects
# Side effects: prints the fight
# Returns: none
def heroCombat(hList):
    for x in range(len(hList)):
        print(str(x) + " " + hList[x].getName())
    uInput = int(input("Select your first hero "))
    uSecondInput = int(input("Select your second hero "))
    firstHero = selectHero(hList, uInput)
    secondHero = selectHero(hList, uSecondInput)
    #This is just getting our heros desginated by our user input
    while int(firstHero.getHealth())> 0 and int(secondHero.getHealth()) >0:
        #This while loop runs until the fight is over
        firstHero.printHealth()
        secondHero.printHealth()
        fHPower = firstHero.useRandomPower()
        sHPower = secondHero.useRandomPower()
        score = fHPower.fight(sHPower)
        #Here we fight using the random powers assinged above
        #Below we take damage given the result of our fight from score
        if score == 1:
            secondHero.takeDamage()
            fHPower.getName() + "Wins "
        elif score == -1:
            firstHero.takeDamage()
            sHPower.win()
        else:
            firstHero.takeDamage()
            secondHero.takeDamage()
        print("---------------------------------------------------------------------")
    #Here we see who wins and who loses
    if int(firstHero.getHealth()) == 0 and int(secondHero.getHealth()) == 0:
        print(firstHero.getName() + " and " + secondHero.getName() + " loses.")
    elif int(firstHero.getHealth()) == 0:
        print(secondHero.getName() + " wins")
    elif int(secondHero.getHealth()) == 0:
        print(firstHero.getName() + " wins")
#Here we reset health
    firstHero.resetHealth()
    secondHero.resetHealth()

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
            hlist =[]
            while len(hlist) == 0:
                file = input("Please enter the hero file ")
                hlist = loadHeros(file)
        if uInput == "2":
            heroList = printRoster(hlist)
        if uInput == "3":
            heroCombat(heroList)
        if uInput == "4":
            print("Goodbye!")

main()