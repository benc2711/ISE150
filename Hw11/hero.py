'''
Ben Crotty
ISE150, Spring 2021
bcrotty@usc.edu
Homework 11
'''

import powers
import random

class hero(object):
    # Function: init
    # Purpose: constructor
    # Parameters: self and line as hero
    # Side effects: store certain variables
    # Returns: none
    def __init__(self, line):
        nline = line.split("|")
        self.__cHealth = int(nline[2])
        self.__hName = nline[0]
        self.__mHealth = int(nline[2])
        self.__pList = nline[1]
        string = nline[1]
        self.__powerList = string.split(",")
        self.__nPowerList =[]
        for x in range(len(self.__powerList)):
            element = powers.powerFactory(self.__powerList[x])
            self.__nPowerList.append(element)




    # Function: getHealth
    # Purpose: getter function for the current health of the hero
    # Parameters: self
    # Side effects: none
    # Returns: the current health
    def getHealth(self):
        return self.__cHealth

    # Function: getName
    # Purpose: getter function for the  name of the hero
    # Parameters: self
    # Side effects: none
    # Returns: the current name
    def getName(self):
        return self.__hName

    # Function: str
    # Purpose: converts the hero's power to string
    # Parameters: self
    # Side effects: none
    # Returns: string of the power
    def __str__(self):
        nString = ""
        for x in self.__nPowerList:
           nString = "" + nString + x.__str__() + "\n\t"
        return str(nString)

    # Function: printHealth
    # Purpose: prints the current health
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def printHealth(self):
        print(self.__hName + " has " + str(self.__cHealth) + " health.")

    # Function: useRandomPower
    # Purpose: prints the name of a hero and a random power that they used from a list of power objects
    # Parameters: self
    # Side effects: prints
    # Returns: the random power they used
    def useRandomPower(self):
        random1 = random.choice(self.__nPowerList)
        print(self.getName() + random1.use())
        return random1

    # Function: takeDamage
    # Purpose: reduces health by one
    # Parameters: self
    # Side effects: reduces health
    # Returns: none
    def takeDamage(self):
        self.__cHealth = int(self.__cHealth) - 1

    # Function: resetHealth
    # Purpose: sets current health to max health
    # Parameters: self
    # Side effects: sets current health to max health
    # Returns: none
    def resetHealth(self):
        self.__cHealth = self.__mHealth



