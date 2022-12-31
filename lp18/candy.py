'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 18
'''

class Candy(object):
    def __init__(self, inName, inCal):
        self.__mName = inName
        self.__mCal = inCal

    def __str__(self):
        msg = self.__class__.__name__
        msg+= " : " + self.__mName
        msg+= ", " + str(self.__mCal)
        return msg

class Chocolate(Candy):
    def __init__(self, inName, inCal, inPerCoco):
        super().__init__(inName, inCal)
        self.__mPerCoco = inPerCoco

    def __str__(self):
        msg = super().__str__()
        msg += "(" + str(self.__mPerCoco) + ")"
        return msg

class FilledChocolate(Chocolate):
    def __init__(self, inName, inCal, inperCoco, inFilled):
        super().__init__(inName,inCal,inperCoco)
        self.__mFilling = inFilled

    def __str__(self):
        msg = super().__str__()
        msg += ", with a " + self.__mFilling + " center"

        return msg

class SoftCandy(Candy):
    def __init__(self, inName, inCal, inFlavor):
        super().__init__(inName,inCal)
        self.__mflavor = inFlavor
    def __str__(self):
        msg = super().__str__()
        msg  += ": " + self.__mflavor
        return msg