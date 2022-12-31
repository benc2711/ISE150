'''
Ben Crotty
ISE150, Spring 2021
bcrotty@usc.edu
Homework 11
'''

twoD =[
        ["F","G","I","L","N","S"],
        ["","G","F","L","F","F"],
        ["G","","I","G","G","S"],
        ["F","I","","L","I","I"],
        ["L","G","L","","L","S"],
        ["F","G","I","L","","S"],
        ["F","S","I","S","S",""]
     ]
#This is where I initalize my 2D array which is crucial in maintaining efficency of code, reducing time to run
    # Class: Power
    # Purpose: acts as a super class for the powers
    # Inherritance: none
    # Side effects: many
    # Returns: when used and when fight
class Power(object):
    # Function: __init__
    # Purpose: constructor
    # Parameters: self and description
    # Side effects: sets self variables
    # Returns: none
    def __init__(self, description):
        self.__desc = description

    # Function: __str__
    # Purpose: string converter of description
    # Parameters: self
    # Side effects: none
    # Returns: string caste of description
    def __str__(self):
        return str(self.__desc)

    # Function: getName
    # Purpose: gets the name of the class
    # Parameters: self
    # Side effects: none
    # Returns: class name
    def getName(self):
        return self.__class__.__name__

    # Function: use
    # Purpose: to make sure the power superclass is not being used for use
    # Parameters: self
    # Side effects: none
    # Returns: print statement
    def use(self):
        return "The power superclass has been used"

    # Function: fight
    # Purpose: have two powers fight eachother based on the 2D array
    # Parameters: self, and second power
    # Side effects: none
    # Returns: 0
    def fight(self, power):
        return 0

class FlightPower(Power):
    # Function: __init__
    # Purpose: constructor
    # Parameters: self
    # Side effects: sets self variables using super
    # Returns: none
    def __init__(self):
        super().__init__("Flight")
    def use(self):
        return " flies away maybe far away from this place."

    # Function: win
    # Purpose: prints a message if the power wins. Mostly used when the second power beats the first power
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def win(self):
        print("Flight wins - They just fly away out of range")

    # Function: fight
    # Purpose: have two powers fight eachother based on the 2D array. Essentially I get the name of the second power. Take the first letter and find where it exists in the first row.
    #Then I look at the columns and find where the given class power in this example, flight, would fight this second power using the index to find the answer.
    # Parameters: self, and second power
    # Side effects: none
    # Returns: 0
    def fight(self, power):
        pName = power.getName()
        pLetter = pName[0]
        index = twoD[0].index(pLetter)
        if twoD[1][index] == pLetter:
            return -1
        elif twoD[1][index] == "F":
            print("Flight wins - They just fly away out of range")
            return 1
        else:
            return 0

class GadgetsPower(Power):
    # Function: __init__
    # Purpose: constructor
    # Parameters: self
    # Side effects: sets self variables using super
    # Returns: none
    def __init__(self):
        super().__init__("Gadget")

    # Function: use
    # Purpose: Prints a message when a power is used
    # Parameters: self,
    # Side effects: prints
    # Returns: 0
    def use(self):
        return " uses what's the right tool for the job"

    # Function: win
    # Purpose: prints a message if the power wins. Mostly used when the second power beats the first power
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def win(self):
        print("Gadgets WIN - Rope snares are powerful")

    # Function: fight
    # Purpose: have two powers fight eachother based on the 2D array. Essentially I get the name of the second power. Take the first letter and find where it exists in the first row.
    # Then I look at the columns and find where the given class power in this example, flight, would fight this second power using the index to find the answer.
    # Parameters: self, and second power
    # Side effects: none
    # Returns: 0
    def fight(self, power):
        pName = power.getName()
        pLetter = pName[0]
        index = twoD[0].index(pLetter)
        if twoD[2][index] == pLetter:
            return -1
        elif twoD[2][index] == "G":
            print("Gadgets WIN - Rope snares are powerful")
            return 1
        else:
            return 0
class IntelligencePower(Power):
    # Function: __init__
    # Purpose: constructor
    # Parameters: self
    # Side effects: sets self variables using super
    # Returns: none
    def __init__(self):
        super().__init__("Intel")

    # Function: use
    #Purpose: Prints a message when a power is used
    # Parameters: self,
    # Side effects: prints
    # Returns: 0
    def use(self):
        return " ponders deeply"

    # Function: win
    # Purpose: prints a message if the power wins. Mostly used when the second power beats the first power
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def win(self):
        print("Intelligence Wins - Can't do much against thinking")

    # Function: fight
    # Purpose: have two powers fight eachother based on the 2D array. Essentially I get the name of the second power. Take the first letter and find where it exists in the first row.
    # Then I look at the columns and find where the given class power in this example, flight, would fight this second power using the index to find the answer.
    # Parameters: self, and second power
    # Side effects: none
    # Returns: 0
    def fight(self, power):
        pName = power.getName()
        pLetter = pName[0]
        index = twoD[0].index(pLetter)
        if twoD[3][index] == pLetter:
            return -1
        elif twoD[3][index] == "I":
            print("Intelligence Wins - Can't do much against thinking")
            return 1
        else:
            return 0
class LaserPower(Power):
    # Function: __init__
    # Purpose: constructor
    # Parameters: self
    # Side effects: sets self variables using super
    # Returns: none
    def __init__(self):
        super().__init__("Laser")

    # Function: use
    # Purpose: Prints a message when a power is used
    # Parameters: self,
    # Side effects: prints
    # Returns: 0
    def use(self):
        return " uses laser eyes"

    # Function: win
    # Purpose: prints a message if the power wins. Mostly used when the second power beats the first power
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def win(self):
        print("LASER WINS - These are just too powerful")

    # Function: fight
    # Purpose: have two powers fight eachother based on the 2D array. Essentially I get the name of the second power. Take the first letter and find where it exists in the first row.
    # Then I look at the columns and find where the given class power in this example, flight, would fight this second power using the index to find the answer.
    # Parameters: self, and second power
    # Side effects: none
    # Returns: 0
    def fight(self, power):
        pName = power.getName()
        pLetter = pName[0]
        index = twoD[0].index(pLetter)
        if twoD[4][index] == pLetter:
            return -1
        elif twoD[4][index] == "L":
            print("LASER WINS - These are just too powerful")
            return 1
        else:
            return 0
class NationalismPower(Power):
    # Function: __init__
    # Purpose: constructor
    # Parameters: self
    # Side effects: sets self variables using super
    # Returns: none
    def __init__(self):
        super().__init__("Nationalism")

    # Function: use
    # Purpose: Prints a message when a power is used
    # Parameters: self,
    # Side effects: prints
    # Returns: 0
    def use(self):
        return " screams AMERICA F*** Yeah"

    # Function: win
    # Purpose: prints a message if the power wins. Mostly used when the second power beats the first power
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def win(self):
        print("Nationalism WINS - A proud soldier will always pull through.")

    # Function: fight
    # Purpose: have two powers fight eachother based on the 2D array. Essentially I get the name of the second power. Take the first letter and find where it exists in the first row.
    # Then I look at the columns and find where the given class power in this example, flight, would fight this second power using the index to find the answer.
    # Parameters: self, and second power
    # Side effects: none
    # Returns: 0
    def fight(self, power):
        pName = power.getName()
        pLetter = pName[0]
        index = twoD[0].index(pLetter)
        if twoD[5][index] == pLetter:
            return -1
        elif twoD[5][index] == "N":
            print("Nationalism WINS - A proud soldier will always pull through.")
            return 1
        else:
            return 0
class StrengthPower(Power):
    # Function: __init__
    # Purpose: constructor
    # Parameters: self
    # Side effects: sets self variables using super
    # Returns: none
    def __init__(self):
        super().__init__("Strength")

    # Function: use
    # Purpose: Prints a message when a power is used
    # Parameters: self,
    # Side effects: prints
    # Returns: 0
    def use(self):
        return " SMASH"

    # Function: win
    # Purpose: prints a message if the power wins. Mostly used when the second power beats the first power
    # Parameters: self
    # Side effects: prints
    # Returns: none
    def win(self):
        print("Strength WINS - Sometimes brute force is the way")

    # Function: fight
    # Purpose: have two powers fight eachother based on the 2D array. Essentially I get the name of the second power. Take the first letter and find where it exists in the first row.
    # Then I look at the columns and find where the given class power in this example, flight, would fight this second power using the index to find the answer.
    # Parameters: self, and second power
    # Side effects: none
    # Returns: 0
    def fight(self, power):
        pName = power.getName()
        pLetter = pName[0]
        index = twoD[0].index(pLetter)
        if twoD[6][index] == pLetter:
            return -1
        elif twoD[6][index] == "S":
            print("Strength WINS - Sometimes brute force is the way")
            return 1
        else:
            return 0
    # Function: powerFactory
    #Purpose: converts strings to powers
    # Parameters: string,
    # Side effects: none
    # Returns: power
def powerFactory(string):
    if string == "strength":
        power = StrengthPower()
        return power
    elif string == "flight":
        power = FlightPower()
        return power
    elif string == "intel":
        power = IntelligencePower()
        return power
    elif string == "gadget":
        power = GadgetsPower()
        return power
    elif string == "national":
        power = NationalismPower()
        return power
    elif string == "laser":
        power = LaserPower()
        return power
