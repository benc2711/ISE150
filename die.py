'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 16 Die
'''
import random
class die(object):
    # Function: init
    # Purpose: constructs die object
    # Parameters: default die as 6 and self
    # Side effects: none
    # Returns: none
    def __init__(self, sides=6):
        self.__psides = sides
        self.__rollResult = 0

    # Function: roll
    # Purpose: rolls a die object
    # Parameters: self
    # Side effects: none
    # Returns: roll result
    def roll(self):
        self.__rollResult = random.randint(1, self.__psides)
        return self.__rollResult

    # Function: str
    # Purpose: converts die object to string
    # Parameters: self
    # Side effects: none
    # Returns: string of roll result
    def __str__(self):
        return str(self.__rollResult)
