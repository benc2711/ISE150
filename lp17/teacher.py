'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Teacher
'''

import random

class Teacher(object):
    def __init__(self, inName, inJokes =[]):
        self.__mName = inName
        self.__jokesList = inJokes
        for item in inJokes:
            self.__jokesList.append(item)
    def getName(self):
        return self.__mName
    def addJoke(self, inJoke):
        self.__jokesList.append(inJoke)

    def getJoke(self):
        if self.__jokesList:
            index = random.randrange(0, len(self.__jokesList))
            return self.__jokesList[index]
        else:
            return "No Jokes. Get back to class!"