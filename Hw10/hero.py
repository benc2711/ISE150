

class hero(object):
    # Function: init
    # Purpose: constructor
    # Parameters: self and line as hero
    # Side effects: store certain variables
    # Returns: none
    def __init__(self, line):
        nline = line.split("|")
        self.__cHealth = nline[2]
        self.__hName = nline[0]
        self.__mHealth = nline[2]
        self.__pList = nline[1]
        # string = nline[1]
        # powerList = string.split(",")

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
       string = self.__pList
       nString = ""
       pList = string.split(",")
       for x in pList:
           nString = "" + nString + x + "\n\t"
       return str(nString)

    # Function: printHealth
    # Purpose: prints the current health
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def printHealth(self):
        print(str(self.__cHealth))





