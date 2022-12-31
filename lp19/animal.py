'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 19 animal
'''

class Animal(object):
    def __init__(self, inDesc):
        self.__description = inDesc
#Creating the animal object using the constructor and below creating a string function
    def __str__(self):
        return self.__description
    #This is used in the lady file to essentially just use text
    def catch(self, other):
        msg = "She swallowed the " + str(self)
        msg += " to catch the " + str(other)
        return msg
    def getType(self):
        return self.__class__.__name__
    def verse(self):
        return "hi"
#There are all rougly the same where they use a super class and have an individual verse
class Fly(Animal):
    def __init__(self):
        super().__init__("Fly")
    def verse(self):
        return "I don't know why she swallowed the fly!"
class Spider(Animal):
    def __init__(self):
        super().__init__("Spider")
    def verse(self):
        return "It wriggled, and jiggled and tickled insider her!"

class Bird(Animal):
    def __init__(self):
        super().__init__("Bird")
    def verse(self):
        return "How absurd to swallow that bird"
class Cat(Animal):
    def __init__(self):
        super().__init__("Cat")
    def verse(self):
        return ""
class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")
    def verse(self):
        return ""
class Goat(Animal):
    def __init__(self):
        super().__init__("Goat")
    def verse(self):
        return ""
class Cow(Animal):
    def __init__(self):
        super().__init__("Cow")
    def verse(self):
        return ""
class Horse(Animal):
    def __init__(self):
        super().__init__("Horse")
    def verse(self):
        return ""