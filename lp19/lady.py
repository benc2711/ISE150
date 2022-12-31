'''
Ben Crotty
ISE 150, Spring 2022
bcrotty@usc.edu
Lab 19 Lady
'''

import animal

class Lady(object):
    def __init__(self, inName):
        self.__name = inName.title()
        self.__tummy = []
        print("There was an old lady named" + self.__name)
#This is the constructor
    def swallow(self, inAnimal):
        self.__tummy.append(inAnimal)
#This is used in the main class to add an animal to this list
    def singSong(self):
        for i in range(len(self.__tummy)):
            print("There was an old lady who swallowed a " + str(self.__tummy[i]))
            print(self.__tummy[i].verse())
            for j in range(i,0,-1):
                #This takes the previous input with the j-1 which allows you to say the lady swallowed one animal to swallow the previous
                print(str(self.__tummy[j].catch(self.__tummy[j-1])))
                #I added the animal part because it simply was giving me an error without it
                #really unsure why this part is not working I copied directly from Nathan but it doesn't seem to acknowledge that the list is populated wiht animals
            if i>0:
                #This is where you print the verse for that sepecific animal
                print(self.__tummy[0].verse())
            print("Perhaps she'll die! \n")